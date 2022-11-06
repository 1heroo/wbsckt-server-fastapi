import typing
from .utils import with_listener
from fastapi import WebSocket
from typing import List


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.macs: List[str] = []

    def connect_listener(self, websocket: WebSocket, mac: str):
        self.macs.append(mac)
        self.active_connections.append(websocket)
        return mac

    def connect_speaker(self, websocket: WebSocket, mac: str):
        if with_listener(mac, self.macs):
            self.active_connections.append(websocket)
            return mac
        return False

    def disconnect(self, websocket: WebSocket, mac: str = False):
        if mac:
            self.macs.remove(mac)
            self.active_connections.remove(websocket)

    def disconnect_listener(self, websocket: WebSocket, mac):
        self.active_connections.remove(websocket)
        self.macs.remove(mac)

    def disconnect_speaker(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
