# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import sys
# import redis


# def Redis_Conn(Host, Port, Password):
#     try:
#         pool = redis.ConnectionPool(host=Host, port=Port, password=Password)
#         r = redis.Redis(connection_pool=pool)
#         return r
#     except:
#         pass

# def Redis_Memuse_Percent(Warn, Phone):
#     maxmemory = r.config_get()['maxmemory']
#     if maxmemory == '0':
#         print("Redis not set maxmemory.")
#         sys.exit(1)
#     else:
#         used_memory = r.info()['used_memory']
#         result = ("%.0f" % (float(used_memory) / float(maxmemory) * 100))
#         print("result(M): %s" % result)
#         print("used_memory(Byte): %s" % used_memory)
#         print("maxmemory(Byte): %s" % maxmemory)
#         if (int(result) > int(Warn)):
#             Message = "Redis instance %s:%s use memory percent >" % (
#             Host, Port) + " " + "%" + "%s, Current use memory:%s bytes" % (Warn, used_memory)
#         else:
#             print("Redis memroy use no except")


import hashlib
import json
from app.config import settings
import redis


class RedisQueue(object):

    def __init__(self, name: str = None, **redis_kwargs):
        self.pool = redis.ConnectionPool(host=settings.REDIS_HOST, username=settings.REDIS_USERNAME,
                                         password=settings.REDIS_PASSWORD, port=settings.REDIS_PORT,
                                         db=settings.REDIS_DATABASE, max_connections=settings.REDIS_MAX_CONNECTIONS)
        self.__db = redis.Redis(connection_pool=self.pool, decode_responses=True)
        self.key = name

    # 返回队列大小
    def qsize(self):
        return self.__db.llen(self.key)

    # 判断队列用尽
    def empty(self):
        return self.qsize() == 0

    def put_hash(self, key, value):
        self.__db.hset(self.key, key, value)

    def get_hash(self, key):
        return self.__db.hget(self.key, key)

    def get_all_hash(self):
        return self.__db.hkeys(self.key)

    def delete_hash(self, key):
        return self.__db.hdel(self.key, key)

    def info(self):
        redis_info = self.__db.info()
        info_item = {}
        info_item['redis_version'] = redis_info['redis_version']
        info_item['os'] = redis_info['os']
        info_item['tcp_port'] = redis_info['tcp_port']
        info_item['used_memory_human'] = redis_info['used_memory_human']
        info_item['used_memory_peak_human'] = redis_info['used_memory_peak_human']
        return info_item


if __name__ == '__main__':
    r = RedisQueue()
    print(r.info())
