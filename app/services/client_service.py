from app.repositories.client_repository import ClientRepository
from app.models.client import Client, HealthIssue
from app.utils.health_score import calculate_score


class ClientService:
    def __init__(self, respository: ClientRepository):
        self.repositorie = respository

    def create_client(self, data) -> Client:
        health_issues = [HealthIssue(name=hi.name, degree=hi.degree) for hi in data.health_issues]
        client = Client(data.name, data.date_nasc, data.gender, health_issues)
        self.repositorie.add(client)
        return client

    def update_client(self, index: int, data) -> Client:
        health_issues = [HealthIssue(**hi) for hi in data.health_issues]
        client = Client(data.name, data.date_nasc, data.gender, health_issues)
        self.repositorie.update(index, client)
        return client

    def list_clients(self):
        return self.repositorie.list()

    def get_client(self, index: int):
        return self.repositorie.get(index)

    def get_risk_clients(self):
        clients = self.repositorie.list()
        sorted_clients = sorted(clients, key=calculate_score, reverse=True)
        return sorted_clients[:10]
