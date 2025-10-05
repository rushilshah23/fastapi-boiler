# tests/conftest.py
import pytest
import warnings
from fastapi.testclient import TestClient
from src.app import create_app

# Suppress Starlette multipart deprecation warnings
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    client = TestClient(app)
    yield client
