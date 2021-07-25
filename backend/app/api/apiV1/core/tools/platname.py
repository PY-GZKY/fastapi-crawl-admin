# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/28 9:03
@Auth ： wutong
@File ：platname.py
@IDE ：PyCharm
"""
import platform
import re, os
import sys

try:
    from fabric.api import *
except ImportError:
    try:
        command_to_execute = "pip install fabric3"
        os.system(command_to_execute)
    except OSError:
        sys.exit(1)
finally:
    from fabric.api import *
    from fabric.main import main
    from fabric.colors import *
    from fabric.context_managers import *
    from fabric.contrib.console import confirm

try:
    import pytz
except ImportError:
    try:
        command_to_execute = "pip install pytz"
        os.system(command_to_execute)
    except OSError:
        sys.exit(1)

try:
    import shutil
except ImportError:
    try:
        command_to_execute = "pip install shutil"
        os.system(command_to_execute)
    except OSError:
        sys.exit(1)

try:
    import certifi
except ImportError:
    try:
        command_to_execute = "pip install certifi"
        os.system(command_to_execute)
    except OSError:
        sys.exit(1)


def win_or_linux():
    # os.name ->(sames to) sys.builtin_module_names
    if 'posix' in sys.builtin_module_names:
        return 'Linux'
    elif 'nt' in sys.builtin_module_names:
        return 'Windows'


def is_windows():
    if "windows" in win_or_linux().lower():
        return True
    else:
        return False


def is_linux():
    if "linux" in win_or_linux().lower():
        return True
    else:
        return False


# @parallel is not supported on Windows System


def terminal_debug_win32():
    command = "dir"
    os.system(command)


def terminal_debug_posix():
    command = "ls -l"
    os.system(command)


if __name__ == '__main__':
    # if is_windows():
    #     terminal_debug_win32()
    #     sys.exit(0)
    # if is_linux():
    #     terminal_debug_posix()
    #     sys.exit(0)

    os_release = platform.system()
    # print(platform.uname())
    if os_release == "Windows":
        print(f"系统版本 {platform.platform()}")
    elif os_release == "Linux":
        if "ubuntu" in platform.platform().lower():
            print("ubuntu系统")
        elif "centos" in platform.platform().lower():
            print("centos系统")
    else:
        print("Error => 未知的系统类型")
        sys.exit(1)



