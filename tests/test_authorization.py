import pytest

from services.authorization import AuthorizationService


@pytest.fixture
def auth_service():
    return AuthorizationService()


def test_admin_access(auth_service):
    assert auth_service.check_access("admin", "document", "read")
    assert auth_service.check_access("admin", "document", "write")
    assert auth_service.check_access("admin", "document", "delete")


def test_editor_access(auth_service):
    assert auth_service.check_access("editor", "document", "read")
    assert auth_service.check_access("editor", "document", "write")
    assert not auth_service.check_access("editor", "document", "delete")


def test_viewer_access(auth_service):
    assert auth_service.check_access("viewer", "document", "read")
    assert not auth_service.check_access("viewer", "document", "write")
    assert not auth_service.check_access("viewer", "document", "delete")


def test_unknown_role_access(auth_service):
    assert not auth_service.check_access("unknown_role", "document", "read")


if __name__ == "__main__":
    pytest.main()
