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

def getTodoList(*, request: Request,
                db: Session = Depends(get_db),
                # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                ):
    # 只展示最近添加的8个事件即可
    todoList = db.query(Todos).order_by(Todos.id.desc()).limit(8).all()
    resultList = [{
        'id': todo.id,
        'title': todo.title,
        'status': todo.status,
        'updateTime': str(todo.update_time)
    } for todo in todoList]
    return resp_200(data=resultList)


def changeTodo(*, request: Request,
               Param: dict,
               db: Session = Depends(get_db),
               token_data: Union[str, Any] = Depends(deps.check_jwt_token)
               ):
    todoInfo = db.query(Todos).filter(Todos.id == Param.get("todoId")).first()
    try:
        todoInfo.status = 0 if todoInfo.status == 1 else 1
        todoInfo.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db.commit()
        return resp_200(message='更新成功')
    except:
        db.rollback()
        return resp_400(message='ID不存在')


def editTodo(*, request: Request,
             todoParam: dict,
             db: Session = Depends(get_db),
             token_data: Union[str, Any] = Depends(deps.check_jwt_token)
             ):
    todoInfo = db.query(Todos).filter(Todos.id == todoParam.get("todoId")).first()
    try:
        if todoParam.get("todoTitle"):
            todoInfo.title = todoParam.get("todoTitle")
            todoInfo.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            db.commit()
            return resp_200(message='编辑成功')
    except:
        db.rollback()
        return resp_400(message='ID不存在')


def createTodo(*, request: Request,
            todoParam: dict,
            db: Session = Depends(get_db),
            # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
            ):
    try:
        createTodo = Todos(title=todoParam.get("title"))
        db.add(createTodo)
        db.commit()
        return resp_200(message='添加成功')
    except:
        db.rollback()
        return resp_400(message='添加失败')


def deleteTodo(*, request: Request,
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
router.add_api_route(methods=['GET'], path="s", endpoint=getTodoList, summary="TODO列表")
router.add_api_route(methods=['PUT'], path="/edit", endpoint=editTodo, summary="编辑TODO")
router.add_api_route(methods=['PUT'], path="/update", endpoint=changeTodo, summary="更新TODO")
router.add_api_route(methods=['POST'], path="/create", endpoint=createTodo, summary="添加TODO")
router.add_api_route(methods=['DELETE'], path="/delete", endpoint=deleteTodo, summary="删除TODO")
