# tests/test_app.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app


def test_home_page():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Clothing Store" in response.data
