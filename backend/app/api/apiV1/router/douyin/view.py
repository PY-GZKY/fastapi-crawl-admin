# # -*- coding: utf-8 -*
# # @Time : 2020/11/10 14:51
"""
这可能是另一种任务调度的思路
直接将任务、爬虫类方法写死，然后直接通过路由调用
适用于短时间内无需改动的任务
"""

# # from app.api.apiV1.spider_m.douyin.getAjaxData import Dy
# from app.api.apiV1.spider_m.spiderStatus.getStatus import get_spider_status
# from app.api.utils.response_code import resp_422, resp_401, resp_500
# from fastapi import APIRouter
# from starlette.requests import Request
# from app.api.utils.rate_limit import limiter
# from typing import List, Union
# router = APIRouter()
#
#
# @limiter.limit("4/minute")
# def dySpider(*, request: Request, d_obj: dict):
#     if request.method == "POST":
#         spiderId = d_obj.get("spiderId")
#         statusDict = get_spider_status(spiderId)
#         if not statusDict.get("data"):
#             return resp_422(message='程序正在抓取中，请勿重复调度')
#         # try:
#         dy = Dy(spiderId)
#         result = dy.run()
#         return result
#         # except:
#         #     return resp_500()
#     return "d_cookie 为必传值"
#
#
#
# # ------------------------------- 路由添加 --------------------------------
#
# router.add_api_route(methods=['POST'], path="/dySpider",
#                      endpoint=dySpider, summary="抖音爬虫任务")
