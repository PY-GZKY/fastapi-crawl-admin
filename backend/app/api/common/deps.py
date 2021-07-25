from typing import Any, Optional, Union

import jwt
from fastapi import Depends, Header
from sqlalchemy.orm import Session
from app.api.apiV1.router.auth import crud
from app.api.apiV1.router.auth import schemas
from app.api.db.session import get_db
from app.api.models.auth import AdminUser
from app.api.utils import customExc
from app.config import settings
from app.security import security


def check_jwt_token(
        token: Optional[str] = Header(None)
) -> Union[str, Any]:
    """
    只解析验证token
    :param token:
    :return:
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        return schemas.TokenPayload(**payload)
    except BaseException:
        raise customExc.UserTokenError(err_desc="Token 验证失败")


def get_current_user(
        db: Session = Depends(get_db), token: Optional[str] = Header(None)
) -> AdminUser:
    """
    根据header中token 获取当前用户
    :param db:
    :param token:
    :return:
    """

    print("这就是Token:", token)
    if not token:
        raise customExc.UserTokenError(err_desc='Token 未定义')

    token_data = check_jwt_token(token)
    user = crud.curd_user.get(db, id=token_data.sub)
    if not user:
        raise customExc.UserNotFound(err_desc="用户未存在")

    return user

# def get_current_active_user(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return current_user
