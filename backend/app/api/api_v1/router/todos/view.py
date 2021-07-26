# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import time
from typing import Any, Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from app.api.common import deps
from app.api.db.session import get_db
from app.api.models.todos import Todos
from app.api.utils.responseCode import resp_200, resp_400
router = APIRouter()

def get_todo_list(*, request: Request,
                  db: Session = Depends(get_db),
                  # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                  ):
    # 只展示最近添加的8个事件即可
    todo_list = db.query(Todos).order_by(Todos.id.desc()).limit(8).all()
    result_list_ = [{
        'id': todo.id,
        'title': todo.title,
        'status': todo.status,
        'updateTime': str(todo.update_time)
    } for todo in todo_list]
    return resp_200(data=result_list_)


def change_todo(*, request: Request,
                Param: dict,
                db: Session = Depends(get_db),
                token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                ):
    todo_info_ = db.query(Todos).filter(Todos.id == Param.get("todoId")).first()
    try:
        todo_info_.status = 0 if todo_info_.status == 1 else 1
        todo_info_.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db.commit()
        return resp_200(message='更新成功')
    except:
        db.rollback()
        return resp_400(message='ID不存在')


def edit_todo(*, request: Request,
              todoParam: dict,
              db: Session = Depends(get_db),
              token_data: Union[str, Any] = Depends(deps.check_jwt_token)
              ):
    todo_info = db.query(Todos).filter(Todos.id == todoParam.get("todoId")).first()
    try:
        if todoParam.get("todoTitle"):
            todo_info.title = todoParam.get("todoTitle")
            todo_info.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            db.commit()
            return resp_200(message='编辑成功')
    except:
        db.rollback()
        return resp_400(message='ID不存在')


def create_todo(*, request: Request,
                todo_param: dict,
                db: Session = Depends(get_db),
                # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                ):
    try:
        create_todo = Todos(title=todo_param.get("title"))
        db.add(create_todo)
        db.commit()
        return resp_200(message='添加成功')
    except:
        db.rollback()
        return resp_400(message='添加失败')


def delete_todo(*, request: Request,
                Param: dict,
                db: Session = Depends(get_db),
                token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                ):
    try:
        db.query(Todos).filter(Todos.id == Param.get("todoId")).delete(synchronize_session=False)
        db.commit()
        return resp_200(message='删除成功')
    except:
        db.rollback()
        return resp_400(message='删除失败')


# ------------------------------- 路由添加 --------------------------------
router.add_api_route(methods=['GET'], path="s", endpoint=get_todo_list, summary="TODO列表")
router.add_api_route(methods=['PUT'], path="/edit", endpoint=edit_todo, summary="编辑TODO")
router.add_api_route(methods=['PUT'], path="/update", endpoint=change_todo, summary="更新TODO")
router.add_api_route(methods=['POST'], path="/create", endpoint=create_todo, summary="添加TODO")
router.add_api_route(methods=['DELETE'], path="/delete", endpoint=delete_todo, summary="删除TODO")
