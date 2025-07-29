# app/main.py

from fastapi import FastAPI, HTTPException
from app.schemas.client_schema import ClientCreateSchema, ClientSchema
from app.services.client_service import ClientService
from app.repositories.client_repository import ClientRepository
from app.utils.health_score import calculate_score

app = FastAPI()
repo = ClientRepository()
service = ClientService(repo)


@app.post("/clients", response_model=ClientSchema)
def create_client(data: ClientCreateSchema):
    return service.create_client(data)


@app.put("/clients/{client_id}", response_model=ClientSchema)
def update_client(client_id: int, data: ClientCreateSchema):
    if not service.get_client(client_id):
        raise HTTPException(status_code=404, detail="Client not found")
    return service.update_client(client_id, data)


@app.get("/clients", response_model=list[ClientSchema])
def list_clients():
    return service.list_clients()


@app.get("/clients/top-risk")
def risk_clients():
    clients = service.get_risk_clients()
    return [
        {
            "name": c.name,
            "score": calculate_score(c)
        } for c in clients
    ]


@app.get("/clients/{client_id}", response_model=ClientSchema)
def get_client(client_id: int):
    client = service.get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client



