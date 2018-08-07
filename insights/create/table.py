# coding=utf-8

"""Create ArcGIS Insights tables."""

from .. import Card, Dataset


def summary_table(data: Dataset) -> Card:
    raise NotImplementedError


def data_table(data: Dataset) -> Card:
    raise NotImplementedError
