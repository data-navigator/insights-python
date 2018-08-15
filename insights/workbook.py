# coding=utf-8

"""An ArcGIS Insights Workbook"""

import enum
from typing import Iterable
from arcgis.gis import Item
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
    def __init__(self, workbook: Item) -> None:
        self._item_data = workbook.get_data()
        self._url = workbook.url
        self._owner = workbook.owner
        self._id = workbook.name
        self._workbook = workbook
        print(self._item_data.keys())

    @property
    def workspace_id(self) -> str:
        """[summary]

        [description]
        """
        return self._id

    @property
    def owner(self) -> str:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._owner

    @property
    def overview(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._workbook.overview

    @property
    def folder(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._workbook.folder

    @property
    def tags(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._workbook.tags

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
    def pages(self) -> Iterable[Page]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return [Page(**page) for page in self._item_data['pages']]

    @property
    def cards(self) -> Iterable[Card]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return [card for page in self.pages for card in page.cards]

    @property
    def title(self):
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def view(self) -> View:
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

    @property
    def datasets(self) -> Iterable[Dataset]:
        """[summary]

        [description]

        :return: [description]
        :rtype: Iterator[Dataset]
        """
        return [dataset for page in self.pages for dataset in page.datasets]
