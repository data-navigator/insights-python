# coding=utf-8

"""Creates a Layer service from an in-memory dataset."""

from .. import Dataset, Result


def layer(result: Result) -> Dataset:
    raise NotImplementedError
