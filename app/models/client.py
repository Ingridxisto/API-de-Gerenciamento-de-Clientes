from datetime import datetime
from typing import List


class HealthIssue:
    def __init__(self, name: str, degree: int):
        self.name = name
        self.degree = degree


class Client:
    def __init__(self, name: str, date_nasc: str, gender: str, health_issues: List[HealthIssue]):
        self.name = name
        self.date_nasc = date_nasc
        self.gender = gender
        self.health_issues = health_issues
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, name: str, date_nasc: str, gender: str, health_issues: List[HealthIssue]):
        self.name = name
        self.date_nasc = date_nasc
        self.gender = gender
        self.health_issues = health_issues
        self.updated_at = datetime.utcnow()