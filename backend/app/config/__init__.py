
# -*- coding: utf-8 -*-
"""
配置文件
服务器上设置 ENV 环境变量
更具环境变量 区分生产开发
"""
import os

env = os.getenv("PRODUCTION", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    from .production_config import settings
else:
    # 没有则是开发环境
    print("开发环境启动 ..... DONE")
    from .development_config import settings

