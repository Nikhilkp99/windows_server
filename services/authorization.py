class AuthorizationService:
    def __init__(self, roles=None):
        # Use a default set of roles if none is provided
        self.roles = roles or self.get_default_roles()

    @staticmethod
    def get_default_roles():
        return {
            "admin": {"read": True, "write": True, "delete": True},
            "editor": {"read": True, "write": True, "delete": False},
            "viewer": {"read": True, "write": False, "delete": False},
        }

    def check_access(self, role, resource, action):
        return self.roles.get(role, {}).get(action, False)

