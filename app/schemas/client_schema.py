from pydantic import BaseModel
from typing import List
from datetime import datetime


class HealthIssueSchema(BaseModel):
    name: str
    degree: int


class ClientCreateSchema(BaseModel):
    name: str
    date_nasc: str
    gender: str
    health_issues: List[HealthIssueSchema]


class ClientSchema(ClientCreateSchema):
    created_at: datetime
    updated_at: datetime
