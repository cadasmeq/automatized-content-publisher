from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Post:
    content: Content
    msg: Message
    social_network: SocialNetwork


@dataclass(frozen=True, order=True)
class Content:
    content: str


@dataclass(frozen=True, order=True)
class Message:
    message: str


@dataclass(frozen=True, order=True)
class SocialNetwork:
    social_network: str


@dataclass(frozen=True, order=True)
class Account:
    username: str
    password: str
