
# -*- coding: utf-8 -*-
"""
定义返回的状态

# 看到文档说这个orjson 能压缩性能(squeezing performance)
https://fastapi.tiangolo.com/advanced/custom-response/#use-orjsonresponse

It's possible that ORJSONResponse might be a faster alternative.

# 安装
pip install --upgrade orjson

测试了下，序列化某些特殊的字段不友好，比如小数
TypeError: Type is not JSON serializable: decimal.Decimal
"""
from fastapi import status
from fastapi.responses import JSONResponse, Response  # , ORJSONResponse
from typing import Union


def resp_200(*, data: Union[list, dict, str] = "200 Success",message:str ="Success" ) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': message,
            'data': data,
        }
    )

def resp_400(*, data: str = None, message: str="400 BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'message': message,
            'data': data,
        }
    )

def resp_401(*, data: str = None, message: str="401 Unauthorized") -> Response:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            'code': 401,
            'message': message,
            'data': data,
        }
    )

def resp_403(*, data: str = None, message: str="403 Forbidden") -> Response:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            'code': 403,
            'message': message,
            'data': data,
        }
    )

def resp_404(*, data: str = None, message: str="404 Page Not Found") -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            'code': 404,
            'message': message,
            'data': data,
        }
    )

def resp_422(*, data: str = None, message: Union[list, dict, str]="422 UNPROCESSABLE_ENTITY") -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            'code': 422,
            'message': message,
            'data': data,
        }
    )

def resp_500(*, data: str = None, message: Union[list, dict, str]=" 500 Server Internal Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 500,
            'message': message,
            'data': data,
        }
    )


# 自定义
def resp_5000(*, data: Union[list, dict, str]=None, message: str="Token failure") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 5000,
            'message': message,
            'data': data,
        }
    )

def resp_5001(*, data: Union[list, dict, str]=None, message: str="User Not Found") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 5001,
            'message': message,
            'data': data,
        }
    )
