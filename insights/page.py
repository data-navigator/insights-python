# coding=utf-8

"""A Page within an ArcGIS Insights Workbook."""

import enum
from typing import Iterator
from .card import Card
from .model import Model


class Sizes(enum.Enum):
    Letter = 0
    Legal = 1
    A3 = 2
    A4 = 3
    A5 = 4
    A6 = 5


class Orientation(enum.Enum):
    Portratit = 0
    Landscape = 1


class Page:
    """Represents an individual page within an ArcGIS Insights Workbook."""
    def __init__(self):
        pass

    @property
    def cards(self) -> Iterator[Card]:
        raise NotImplementedError

    @property
    def model(self) -> Model:
        raise NotImplementedError

    @property
    def size(self):
        raise NotImplementedError

    @property
    def orientation(self):
        raise NotImplementedError

    @property
    def background(self):
        raise NotImplementedError

    @property
    def foreground(self):
        raise NotImplementedError
