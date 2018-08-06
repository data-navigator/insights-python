# coding=utf-8

"""Various sources of data."""


def csv(path: str) -> str:
    raise NotImplementedError


def excel(path: str) -> str:
    raise NotImplementedError


def group(url: str) -> str:
    raise NotImplementedError


def organization(url: str) -> str:
    raise NotImplementedError


def user(url: str) -> str:
    raise NotImplementedError
