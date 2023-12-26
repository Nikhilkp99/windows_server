import os


class AuthService:
    def __init__(self):
        self.max_login_attempts = 3
        self.lockout_threshold = 5
        self.login_attempts = {}

    def login(self, username, password):
        if username == os.environ.get("ADMIN_USERNAME") and password == os.environ.get("ADMIN_PASSWORD"):
            return True
        else:
            self.login_attempts[username] = self.login_attempts.get(username, 0) + 1
            if self.login_attempts[username] >= self.lockout_threshold:
                raise ValueError("Account locked out")
            return False

