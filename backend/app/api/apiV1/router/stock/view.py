# # -*- coding: utf-8 -*
# # @Time : 2020/11/10 15:00
# import asyncio
# import json
#
#
# from typing import Union, Any
#
# from app.api import notifier
# from app.api.apiV1.spider_m.spiderStatus.getStatus import get_spider_status
# from app.api.common import deps
# from app.api.utils.response_code import resp_401, resp_422, resp_400, resp_500
#
#
#
# import time
# # from monitor.tasks import set_plat_cookie
# from fastapi import APIRouter, Depends
# from starlette.requests import Request
# from app.api.utils.rate_limit import limiter
#
# router = APIRouter()
#
#
# @limiter.limit("2/minute")
# def erp3c_spider(*, request: Request, d_obj: dict, token_data: Union[str, Any] = Depends(deps.check_jwt_token)):
#     if request.method == "POST":
#         spiderId = d_obj.get("spiderId")
#         statusDict = get_spider_status(spiderId)
#         if not statusDict.get("data"):
#             return resp_422(message='程序正在抓取中，请勿重复调度')
#         # try:
#         erp3c_stock = StockGoodsExtend(spiderId)
#         result = erp3c_stock.run()
#         return result
#         # except:
#         #     return resp_500()
#     return "d_cookie 为必传值"
#
#
# @limiter.limit("2/minute")
# def stockJdZxSpider(*, request: Request, d_obj: dict,
#                     token_data: Union[str, Any] = Depends(deps.check_jwt_token)):
#     if request.method == "POST":
#         spiderId = d_obj.get("spiderId")
#         statusDict = get_spider_status(spiderId)
#         if not statusDict.get("data"):
#             return resp_422(message='程序正在抓取中，请勿重复调度')
#         try:
#             jd_zx_stock = JdZxStockExtend(spiderId)
#             result = jd_zx_stock.run()
#             if result.get("code") == -1:
#                 return resp_400(message='登陆失效,请稍后重试 ')
#             return result
#         except TypeError:
#             return resp_500()
#     else:
#         return '缺少必要参数'
#
#
# def stockJdJhSpider(*, request: Request, token_data: Union[str, Any] = Depends(deps.check_jwt_token),
#                     d_obj: dict):
#     spiderId = d_obj.get("spiderId")
#     statusDict = get_spider_status(spiderId)
#     if not statusDict.get("data"):
#         return resp_422(message='程序正在抓取中，请勿重复调度')
#     J = JdJhStockExtend(spiderId)
#     result = J.run()
#     if result.get("code") == -1:
#         return resp_400(message='登陆失效,请稍后重试 ')
#     return result
#
#
# def stockCnSpider(*, request: Request, token_data: Union[str, Any] = Depends(deps.check_jwt_token),
#                   d_obj: dict):
#     statusDict = get_spider_status(spiderId=d_obj.get("spiderId"))
#     if not statusDict.get("data"):
#         return resp_422(message='程序正在抓取中，请勿重复调度')
#
#     C = CnStockExtend(d_obj.get("spiderId"))
#     result = C.run()
#     if result.get("code") == -1:
#         return resp_400(message='登陆失效,请稍后重试 ')
#     return result
#
#
# # ------------------------------- 路由添加 --------------------------------
#
# router.add_api_route(methods=['POST'], path="/jdZxSpider", endpoint=stockJdZxSpider,
#                      summary="京东赞晓库存更新")
# router.add_api_route(methods=['POST'], path="/jdJhSpider", endpoint=stockJdJhSpider,
#                      summary="京东佳皓库存更新")
# router.add_api_route(methods=['POST'], path="/erp3cSpider", endpoint=erp3c_spider,
#                      summary="本仓库存更新")
# router.add_api_route(methods=['POST'], path="/cnSpider", endpoint=stockCnSpider,
#                      summary="菜鸟库存更新")
