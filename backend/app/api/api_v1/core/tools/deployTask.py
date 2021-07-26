# !/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
from concurrent.futures import ThreadPoolExecutor
import time

from app.api.api_v1.core.spider_log.save_log import add_task_log
from app.config.development_config import settings
from paramiko.ssh_exception import SSHException
from app.api.logger import logger

from app.config import settings


class SSHConnection(object):
    def __init__(self, task_id):
        self.__k = None
        self.task_id = task_id

    def connect(self, host, port, username, password):
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        return transport

    def close(self, transport):
        logger.debug(f"{transport} close ... done")
        transport.close()  # 释放资源

    def put_file(self,
                 host: str = '',
                 port: int = 22,
                 username: str = '',
                 password: str = '',
                 local_path: str = None,
                 remote_path: str = None
                 ) -> tuple:

        transport = self.connect(host, port, username, password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动设置ssh密钥对
        ssh._transport = transport  # 赋值transport

        _stat = 0

        try:
            sftp.stat(settings.REMOTE_DIR)
            logger.debug("远程目录存在")
        except (IOError, FileNotFoundError):
            logger.debug("远程目录不存在, 新建一个目录")
            # sftp.mkdir(settings.REMOTE_DIR)
            try:
                sftp.mkdir(settings.REMOTE_DIR)
            except PermissionError:
                logger.debug("权限不足, 加 Sudo")
                ssh.exec_command(settings.SUDO_PASSWORD_COMMAND.format(password, settings.REMOTE_DIR))

        try:
            sftp.put(local_path, remote_path)

            # 解压 unzip -o test.zip -d tmp/
            stdin, stdout, stderr = ssh.exec_command(settings.UNZIP_COMMAND.format(remote_path, settings.REMOTE_DIR))

            # 获取命令结果
            stdout_str = stdout.read().decode('utf8')
            stderr_str = stderr.read().decode('utf8')

            # 如果错误不为空
            if stderr_str: raise SSHException('ssh 执行错误')
            if stdout_str != '':
                _stat = 1
                logger.debug(f'执行解压结果: \n {stdout_str}')
        except:
            _stat = 0
        finally:
            self.close(transport)

        return host, _stat

    def exce_cmd(self,
                 host: str = '',
                 port: int = 22,
                 username: str = '',
                 password: str = '',
                 command: str = 'cd /home/tasks/printOut && python printOut.py') -> None:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动设置ssh密钥对

        transport = self.connect(host, port, username, password)  # 连接远程服务器
        ssh._transport = transport  # 赋值transport

        # 执行命令
        _, stdout, stderr = ssh.exec_command(command, get_pty=True)

        # 获取命令结果
        # stderr_str = stderr.read().decode('utf8')
        # # 如果错误不为空
        # if stderr_str:
        #     # raise SSHException(f'{host} -->  执行错误')
        #     logger.error(f'{host} -->  执行错误')
        while not stdout.channel.exit_status_ready():
            result = stdout.readline().strip('\n')
            if result:
                logger.debug(f"{host}终端输出:　{result}")
                add_task_log(taskId=self.task_id, taskLogMsg=result, host=host)
            # 由于在退出时，stdout还是会有一次输出
            if stdout.channel.exit_status_ready():
                break

        self.close(transport)  # 关闭连接
        # return True

    def bulk_exce_cmd(self, hosts) -> None:

        # 这个　max_workers　可以放在 setting
        with ThreadPoolExecutor(max_workers=8) as pool:
            future_task_list = [
                pool.submit(self.exce_cmd, **host_info)
                for host_info in hosts
                # [
                #     dict(host='', port=22, username='', password='', command='pwd'),
                #     dict(host='', port=22, username='', password='',command='cd /home && ls'),
                # ]
            ]

        # future_result_list = [future.result() for future in future_task_list]
        # return future_result_list

    def bulk_exce_put_file(self, hosts):

        # def get_result(future):
        #     print(future.result())

        with ThreadPoolExecutor(max_workers=8) as pool:
            future_task_list = [
                pool.submit(self.put_file, **host_info)
                # 遗憾的是这里不支持将文件 ->　/home/remote_test/
                for host_info in hosts
            ]

        future_result_list = [future.result() for future in future_task_list]
        return future_result_list


if __name__ == '__main__':
    obj = SSHConnection(task_id="6be83f39-01c1-4cef-8b87-f9d69806e5f6")
    obj.exce_cmd()
