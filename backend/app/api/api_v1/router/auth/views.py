
# -*- coding: utf-8 -*-

from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api.db.session import get_db
from app.api.common import deps
from app.api.logger import logger
from app.api.models import auth
from app.api.utils import responseCode
from app.config import settings
from app.security import security
from .crud import curd_role, curd_user
from .schemas import user

router = APIRouter()


@router.post("/login/access-token", summary="用户登录认证")
async def login_access_token(
        *,
        request: Request,
        response: Response,
        db: Session = Depends(get_db),
        user_info: user.UserEmailAuth,
) -> Any:
    """
    用户登录
    :param db:
    :param user_info:
    :return:
    """

    # 验证用户
    user = curd_user.authenticate(db, email=user_info.username, password=user_info.password)
    if not user:
        logger.info(f"用户邮箱认证错误: email{user_info.username} password:{user_info.password}")
        return responseCode.resp_500(message="用户名或者密码错误")
    elif not curd_user.is_active(user):
        return responseCode.resp_500(message="用户邮箱未激活")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 登录token 只存放了user.id
    # access_token = security.create_access_token(user.id, expires_delta=access_token_expires)
    # response.set_cookie("access_token", access_token)

    # request.session["username"] = user.email

    return responseCode.resp_200(data={
        "token": security.create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "Bearer",
    })


@router.get("/user/info", summary="获取用户信息", response_model=user.UserInfo)
async def get_user_info(
        *,
        db: Session = Depends(get_db),
        current_user: auth.AdminUser = Depends(deps.get_current_user)
) -> Any:
    """
    获取用户信息
    :param db:
    :param current_user:
    :return:
    """
    role_info = curd_role.query_role(db, role_id=current_user.role_id)

    return responseCode.resp_200(data={
        "role_id": current_user.role_id,
        "role": role_info.role_name,
        "nickname": current_user.nickname,
        "avatar": current_user.avatar
    })


@router.post("/user/logout", summary="用户退出")
async def user_logout(current_user: auth.AdminUser = Depends(deps.get_current_user)):
    """
    用户退出
    :param current_user:
    :return:
    """
    return responseCode.resp_200(data="ok")
