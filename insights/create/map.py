# coding=utf-8

"""Map-style Visualization on an ArcGIS Insights Card."""

from .. import Card, Dataset


def binned_map(data: Dataset) -> Card:
    raise NotImplementedError


def category_map(data: Dataset) -> Card:
    raise NotImplementedError


def choropleth_map(data: Dataset) -> Card:
    raise NotImplementedError


def link_map(data: Dataset) -> Card:
    raise NotImplementedError


def heat_map(data: Dataset) -> Card:
    raise NotImplementedError


def location_map(data: Dataset) -> Card:
    raise NotImplementedError


def proportional_symbol_map(data: Dataset) -> Card:
    raise NotImplementedError
