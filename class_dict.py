from dataclasses import dataclass
import typing

@dataclass
class Owner:
    name: str = 'Unknown name'
    age: int = 'Unknown age'
    description: typing.Any = None

    def __post_init__(self):
        self.description = self.description or f"Owner's name is {self.name} and ages is {self.age}"

