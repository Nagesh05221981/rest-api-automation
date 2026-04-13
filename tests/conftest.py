"""
conftest.py
Shared pytest fixtures available to all test modules automatically.
"""
import sys
from pathlib import Path
import pytest
from helpers.api_client import APIClient
from helpers.data_loader import load

# Ensure project root is in sys.path
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


@pytest.fixture(scope="session")
def test_data() -> dict:
    """Load YAML test data once per session."""
    return load("test_data.yaml")


@pytest.fixture(scope="session")
def client(test_data) -> APIClient:
    """Return a single APIClient instance for all tests."""
    return APIClient(base_url=test_data["base_url"])


@pytest.fixture(scope="session")
def endpoints(test_data) -> dict:
    """Return endpoints from test data."""
    return test_data.get("endpoints", {})


@pytest.fixture(scope="session")
def payloads(test_data) -> dict:
    """Return payload templates from test data."""
    return test_data.get("payloads", {})