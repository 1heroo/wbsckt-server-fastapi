from fastapi import FastAPI
from typing import Union
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from .manager import manager
from .utils import is_speaker


app = FastAPI()


@app.get('/')
def main():
    return {"message": 'success'}


@app.websocket("/ws/{name}")
async def websocket_endpoint(websocket: WebSocket, name: Union[str, int]):
    await websocket.accept()
    mac = await websocket.receive_text()
    if is_speaker(mac):
        mac = manager.connect_speaker(websocket, mac)

    else:
        mac = manager.connect_listener(websocket, mac)
    await manager.send_personal_message('you joined the chat', websocket)

    print(manager.active_connections, 'all the activa connections')
    print(manager.macs, 'all the macs')
    try:
        if not mac:
            raise WebSocketDisconnect

        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f'{name}: {data}')

    except WebSocketDisconnect:
        if is_speaker(mac):
            manager.disconnect_speaker(websocket)
            await manager.broadcast(f"{name} left the chat")
        else:
            manager.disconnect_listener(websocket, mac)

