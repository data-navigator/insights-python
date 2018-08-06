# coding=utf-8

"""Create ArcGIS Insights tables."""

from .. import Card
from .. import Data


def summary_table(data: Data) -> Card:
    raise NotImplementedError


def data_table(data: Data) -> Card:
    raise NotImplementedError
