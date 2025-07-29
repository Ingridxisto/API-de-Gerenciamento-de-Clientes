from app.models.client import Client
import math


def calculate_score(client: Client) -> float:
    sd = sum(issue.degree for issue in client.health_issues)
    score = (1 / (1 + math.exp(-(-2.8 + sd)))) * 100
    return round(score, 2)
