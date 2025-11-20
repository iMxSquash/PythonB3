from .UserRepository import UserRepository
import json

class FileRepo(UserRepository):
    def __init__(self, filename: str):
        self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.users = data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = []

    def find_all(self) -> list[dict]:
        return self.users

    def save(self, user: dict) -> None:
        self.users.append(user)
        with open(self.filename, 'w') as f:
            json.dump(self.users, f)
            