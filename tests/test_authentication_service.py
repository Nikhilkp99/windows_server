import os
import pytest
import time
from dotenv import load_dotenv
from services.authentication_service import AuthService

load_dotenv()

@pytest.fixture
def auth_service():
    return AuthService()


class TestAuthService:
    def test_valid_login(self, auth_service):
        username = os.environ.get("ADMIN_USERNAME")
        password = os.environ.get("ADMIN_PASSWORD")
        assert auth_service.login(username, password) is True

    def test_invalid_login(self, auth_service):
        assert auth_service.login("msys", "Nik@123") is False

    def test_account_lockout(self, auth_service):
        for i in range(auth_service.lockout_threshold - 1):
            assert auth_service.login("Administrator", "msys@567") is False

        time.sleep(1)

        with pytest.raises(ValueError, match="Account locked out"):
            auth_service.login("Administrator", "Master#345")


if __name__ == "__main__":
    pytest.main()

