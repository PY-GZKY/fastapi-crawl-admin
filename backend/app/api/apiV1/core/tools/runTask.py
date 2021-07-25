# -*- coding: utf-8 -*
# @Time : 2021/1/5 14:24

import platform
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm
from app.config import settings


def __init(pwdDict):
    env.warn_only = True
    env.parallel = True
    # env.roledefs = {
    #     'dev': list(pwdDict.keys()),
    #     # 'online': ['root@45.33.108.82']
    # }
    # env.key_filename = 'C:/Users/HP/.ssh/id_rsa'

    # host strings必须由username@host:port三部分构成，缺一不可，否则运行时还是会要求输入密码
    env.Hosts = list(pwdDict.keys())
    env.passwords = pwdDict


# @roles('dev')
@parallel
def runPrintOut(directoryName, command):  # 执行celery任务
    with cd(f'../home/{directoryName}'):
        run(command)


def startTask(pwdDict, directoryName, command):
    __init(pwdDict)
    execute(runPrintOut, directoryName, command)


