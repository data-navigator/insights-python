# coding=utf-8

"""A Page within an ArcGIS Insights Workbook."""

import enum
from typing import Iterable
from .card import Card
from .dataset import Dataset
from .model import Model
from .theme import Theme


class Size(enum.Enum):
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
    def __init__(self, **page: dict) -> None:
        self._cards = page['cards']
        self._contents = page['contents']
        self._model = page['model']
        self._title = page['title']
        self._layout = page['layout']
        self._page = page

    @property
    def cards(self) -> Iterable[Card]:
        """[summary]

        [description]

        """
        # TODO zip Cards with layout
        return [Card(**card) for card in self._cards]

    @property
    def datasets(self) -> Iterable[Dataset]:
        """[summary]

        [description]

        :return: [description]
        :rtype: Iterable[Dataset]
        """
        return [Dataset(**dataset) for dataset in self._contents]

    @property
    def model(self) -> Model:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._model

    @property
    def size(self) -> Size:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def orientation(self) -> Orientation:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def theme(self) -> Theme:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def title(self) -> str:
        """[summary]

        [description]

        :return: [description]
        :rtype: str
        """
        return self._title
