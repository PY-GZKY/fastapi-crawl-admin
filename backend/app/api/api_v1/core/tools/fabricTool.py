# -*- coding: utf-8 -*
# @Time : 2021/1/5 14:24

import platform
import sys

from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm
from app.config import settings


class PlatForm():
    def win_or_linux(self):
        # os.name ->(sames to) sys.builtin_module_names
        if 'posix' in sys.builtin_module_names:
            return 'Linux'
        elif 'nt' in sys.builtin_module_names:
            return 'Windows'

    def is_windows(self):
        if "windows" in self.win_or_linux().lower():
            return True
        else:
            return False

    def is_linux(self):
        if "linux" in self.win_or_linux().lower():
            return True
        else:
            return False

    def run(self):
        os_release = platform.system()
        # print(platform.uname())
        if os_release == "Windows":
            print(f"系统版本 {platform.platform()}")
        elif os_release == "Linux":
            distname = platform.linux_distribution()[0]
            # print(distname)
            if str(distname).lower() == "ubuntu":
                print("ubuntu系统")
            elif str(distname).lower() == "centos":
                print("centos系统")
        else:
            print("Error => 未知的系统类型")
            sys.exit(1)

# if __name__ == '__main__':
#     h = PlatForm()
#     h.run()

# import time
# from fabric.api import *
# from fabric.colors import yellow, green
# env.hosts = ['root@101.']
# env.key_filename = 'C:\\Users\\HP\\Desktop\\豁\\backend\\app\\rsa\\id_rsa'
# env.warn_only = True
#
# env.deploy_project_root = '/home/'
# env.deploy_current_dir = 'current'
# env.deploy_version = f"{time.strftime('%Y-%m-%d')}_dev_v1.0"
#
# @task
# def run_task2():  # 安装
#     with cd('../home'):
#         run('pip -V')
#         run('pwd')
#         result = run('celery --version')
#         return result
#
# @task
# def put_package(package):
#     print(yellow("start put package...."))
#     with settings(warn_only=True):
#         with cd(env.deploy_project_root):
#             run("mkdir %s" % (env.deploy_version))
#
#     env.deploy_full_path = env.deploy_project_root + env.deploy_version
#
#     with settings(warn_only=True):
#         result = put(package, env.deploy_full_path)
#
#     if result.failed and not ("put file failed,Continue[Y/N]?"):
#         abort('Aborting file put task')
#
#     with cd(env.deploy_full_path):
#         # run(f"unzip {package}")
#         print(green("put package success!"))
#
#
# def gogogo():  # 上传、安装组合命令
#     result = execute(run_task2)
#     print(result)
#
#
# if __name__ == '__main__':
#     gogogo()
