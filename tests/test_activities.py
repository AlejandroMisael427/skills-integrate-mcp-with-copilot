import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app import app


client = TestClient(app)


def test_github_skills_activity_is_available():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "GitHub Skills" in response.json()
