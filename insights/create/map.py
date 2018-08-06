# coding=utf-8

"""Map-style Visualization on an ArcGIS Insights Card."""

from .. import Card
from .. import Data


def binned_map(data: Data) -> Card:
    raise NotImplementedError


def category_map(data: Data) -> Card:
    raise NotImplementedError


def choropleth_map(data: Data) -> Card:
    raise NotImplementedError


def link_map(data: Data) -> Card:
    raise NotImplementedError


def heat_map(data: Data) -> Card:
    raise NotImplementedError


def location_map(data: Data) -> Card:
    raise NotImplementedError


def proportional_symbol_map(data: Data) -> Card:
    raise NotImplementedError
