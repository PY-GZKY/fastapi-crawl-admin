import time

from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket,WebSocketDisconnect

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    _a = 0
    while 1:
        time.sleep(3)
        await websocket.send_json({"msg": "Hello WebSocket"})
        if _a > 10:
            break
        _a+=1
    await websocket.close()


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        try:
            while 1:
                data = websocket.receive_json()
                print(data)
                assert data == {"msg": "Hello WebSocket"}
        except WebSocketDisconnect:
            print("关闭")

if __name__ == '__main__':
    # test_read_main()
    test_websocket()