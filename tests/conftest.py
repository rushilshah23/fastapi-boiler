# tests/conftest.py
import pytest
import warnings
from fastapi.testclient import TestClient
from src.app import create_app
from dotenv import load_dotenv
from pathlib import Path
# Suppress Starlette multipart deprecation warnings
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "envs" / ".env")         # default
load_dotenv(BASE_DIR / "envs" / "test.env", override=True)  # override with test env

@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    client = TestClient(app)
    yield client
