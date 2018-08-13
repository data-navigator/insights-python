# coding=utf-8

"""An ArcGIS Insights Workbook"""

import enum
from typing import Iterator
from .card import Card
from .dataset import Dataset
from .page import Page


class View(enum.Enum):
    """[summary]

    [description]

    :param enum: [description]
    :type enum: [type]
    """
    page = 0
    model = 1


class Workbook:
    """Represents a hosted ArcGIS Insights Workbook."""
    def __init__(self):
        pass

    @property
    def owner(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def overview(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def folder(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def tags(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def credits(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def settings(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def usage(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def pages(self) -> Iterator[Page]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def cards(self) -> Iterator[Card]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def title(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def view(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def basemap(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def details(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    def add_data(self, data: Dataset):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    def add_page(self, page: Page):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    def duplicate(self) -> str:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    def delete(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    def save(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError
