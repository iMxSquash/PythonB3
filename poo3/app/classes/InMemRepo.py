from .UserRepository import UserRepository

class InMemRepo(UserRepository):
    def __init__(self):
        self.users = []

    def find_all(self) -> list[dict]:
        return self.users

    def save(self, user: dict) -> None:
        self.users.append(user)
        