import asyncio
import random
import time
from typing import List

from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    @staticmethod
    async def send_personal_message(message: dict, ws: WebSocket):
        # 发送个人消息
        await ws.send_json(message)

    async def broadcast(self, message: dict):
        # 广播消息
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()


@app.websocket("/ws/{user}")
async def websocket_endpoint(websocket: WebSocket, user):
    print('a new websocket to create.')
    await manager.connect(websocket)
    # await websocket.accept()
    _a = 0
    while True:
        try:
            if _a > 10:
                # manager.disconnect(websocket)
                raise WebSocketDisconnect
                # print("关闭连接")
                # break
            # Wait for any message from the client
            # await websocket.receive_text()
            # Send message to the client
            resp = {'value': time.strftime("%Y-%m-%d %H:%M:%S ")}
            await asyncio.sleep(1)
            # await websocket.send_json(resp)
            await manager.send_personal_message(resp, websocket)

            # 广播出去
            # await manager.broadcast(resp)
            _a += 1
            print(_a)
        except WebSocketDisconnect:
            manager.disconnect(websocket)
            print("抛出　WebSocketDisconnect　关闭连接")
            break
    print('Bye..')


# @app.websocket("/ws/{user}")
# async def websocket_endpoint(websocket: WebSocket, user: str):
#
#     await manager.connect(websocket)
#
#     # await manager.broadcast(f"用户{user}进入聊天室")
#     _a = 0
#     is_run = 1
#     try:
#         if is_run:
#             while True:
#                 if _a > 10:
#                     manager.disconnect(websocket)
#                     print("关闭连接")
#                     break
#                 await manager.send_personal_message(f"fuck {random.random()}..... ", websocket)
#                 _a+=1
#                 time.sleep(1)
#                 # await manager.broadcast(f"用户:{user} 说: {data}")
#         else:
#             await manager.send_personal_message(f"已经结束运行 ..... ", websocket)
#
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         print("关闭连接")
#         # await manager.broadcast(f"用户-{user}-离开")

if __name__ == "__main__":
    import uvicorn

    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8010 --reload
    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True, debug=True)
