from fastapi import APIRouter
from app.api.api_v1.router import auth, utils, task, ws, system_data, \
    file,todos, hosts,global_core

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/admin/auth", tags=["用户"])
api_v1_router.include_router(utils.router, prefix="/utils", tags=["工具类"])
api_v1_router.include_router(task.router, tags=["爬虫"])
api_v1_router.include_router(global_core.router, tags=["全局参数"])
api_v1_router.include_router(system_data.router, prefix="/system", tags=["系统参数"])
api_v1_router.include_router(ws.router, prefix="/push", tags=["WS"])
api_v1_router.include_router(file.router, prefix="/file", tags=["上传文件"])
api_v1_router.include_router(todos.router, prefix="/todo", tags=["待办事件"])
api_v1_router.include_router(hosts.router, prefix="/host", tags=["主机节点"])

