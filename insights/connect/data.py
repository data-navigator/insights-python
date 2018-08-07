# coding=utf-8

"""Various sources of data."""

from .. import Dataset


def csv(path: str) -> Dataset:
    raise NotImplementedError


def excel(path: str) -> Dataset:
    raise NotImplementedError


def group(url: str) -> Dataset:
    raise NotImplementedError


def organization(url: str) -> Dataset:
    raise NotImplementedError


def user(url: str) -> Dataset:
    raise NotImplementedError
