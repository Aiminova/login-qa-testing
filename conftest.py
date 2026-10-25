import os
import pytest

# Application under test: a public login page built for practicing test automation
BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")

VALID_USER = "tomsmith"
VALID_PASS = "SuperSecretPassword!"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
