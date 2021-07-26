
# -*- coding: utf-8 -*-

"""
权限表
"""
from typing import Optional

from pydantic import BaseModel


class RoleCreate(BaseModel):
    """
    创建角色字段
    """
    role_id: int
    role_name: str
    permission_id: int
    re_mark: Optional[str] = None


class RoleUpdate(BaseModel):
    """
    角色更新字段
    """
    role_name: Optional[str] = None
    re_mark: Optional[str] = None
