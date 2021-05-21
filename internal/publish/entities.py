from dataclasses import dataclass, asdict


@dataclass(frozen=True, order=True)
class User:
    name: str
