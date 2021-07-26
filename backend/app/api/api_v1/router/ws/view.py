import json
from typing import List
import random
from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket, WebSocketDisconnect
from app.api.api_v1.core.spider_log.save_log import query_task_log

router = APIRouter()


class Notifier():
    def __init__(self):
        self.connections: List[WebSocket] = []

    
    async def push(self, msg: list):
        await self._notify(msg)

    @staticmethod
    async def send_personal_message(message: dict, websocket: WebSocket):
        # 发送个人消息
        await websocket.send_json(message)
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    # 广播消息
    async def _notify(self, message: list):
        # 广播消息
        for connection in self.connections:
            await connection.send_json(message)


notifier = Notifier()

# ------------------------------- 路由添加 --------------------------------
# router.add_api_route(methods=['GET'], path="/1234567", endpoint=push_to_connected_websockets, summary="push_to_connected_websockets")
