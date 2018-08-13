# coding=utf-8

"""A Page within an ArcGIS Insights Workbook."""

import enum
from typing import Iterator
from .card import Card
from .model import Model


class Sizes(enum.Enum):
    """[summary]

    [description]

    :param enum: [description]
    :type enum: [type]
    """
    Letter = 0
    Legal = 1
    A3 = 2
    A4 = 3
    A5 = 4
    A6 = 5


class Orientation(enum.Enum):
    """[summary]

    [description]

    :param enum: [description]
    :type enum: [type]
    """
    Portratit = 0
    Landscape = 1


class Page:
    """Represents an individual page within an ArcGIS Insights Workbook."""
    def __init__(self):
        pass

    @property
    def cards(self) -> Iterator[Card]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def model(self) -> Model:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def size(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def orientation(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def background(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def foreground(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError
