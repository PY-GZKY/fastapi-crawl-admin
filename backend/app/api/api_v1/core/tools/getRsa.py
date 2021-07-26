# # -*- coding: utf-8 -*
# # @Time : 2021/1/9 9:21
#
# import subprocess
#
# from fabric.contrib.console import confirm
#
# from fabric.api import *
# from fabric.colors import yellow, green
# import time

# class GetRsaFile():
#     def __init__(self, ip='127.0.0.1', username='root', password='root', port=22):
#         self.ip = ip
#         self.env = env
#         self.env.warn_only = True  # 出错时跳过错误
#         self.env.deploy_ssh_path = '~/.ssh/id_rsa'
#         self.env.deploy_version = f"{time.strftime('%Y-%m-%d')}_dev_v1.0"
#         self.env.Hosts = [f"{username}@{ip}:{port}"]
#         self.env.passwords = {
#             f"{username}@{ip}:{port}": password,
#         }
#
#     def getRsa(self):
#         p = subprocess.run("cd C://Users//HP//.ssh && type id_rsa.pub", shell=True, stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE,
#                            universal_newlines=True)
#         # print(f'获取返回数据：{p.stdout}')
#         return p.stdout
#
#     # 生成 id_rsa.pub 文件，put到各个主机上
#     def getFile(self):
#         with settings(show('everything'), warn_only=True):
#             # run("cd .ssh/")
#             run("cd C://Users//HP//.ssh && cat id_rsa.pub")
#             # run("ssh-keygen -t rsa -f ~/.ssh/id_rsa -N shoufeng -C shoufeng")  # 生成 id_rsa.pub 文件
#             # run("cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys")  # 免密信息写入宿主主机验证文件
#             # result = get(self.env.deploy_ssh_path, f"./rsa/id_rsa_{self.ip}")
#             # return result
#
#     def execute(self):
#         execute(self.getFile)
#
#
# if __name__ == '__main__':
#     h = GetRsaFile(ip='127.0.0.1', username='root', password='root', port=22)
#     stdout = h.getRsa()
#     print(f'获取返回数据：{stdout}')


"""获取本地 rsa 公钥 用于免密登录"""
"""算了,还是手动添加公钥好一点"""


class GetRsa():
    pass
