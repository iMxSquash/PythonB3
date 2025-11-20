from typing import Protocol

class IParle(Protocol):
    def parler(self) -> str:
        ...