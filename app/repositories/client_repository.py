from typing import List, Optional
from app.models.client import Client


class ClientRepository:
    def __init__(self):
        self.clients: List[Client] = []

    def add(self, client: Client):
        self.clients.append(client)

    def list(self) -> List[Client]:
        return self.clients

    def get(self, index: int) -> Optional[Client]:
        if 0 <= index < len(self.clients):
            return self.clients[index]
        return None

    def update(self, index: int, client: Client):
        if 0 <= index < len(self.clients):
            self.clients[index] = client
