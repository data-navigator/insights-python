# coding=utf-8

"""An ArcGIS Insights Workbook"""

import enum
from typing import Iterator
from .card import Card
from .dataset import Dataset
from .page import Page


class View(enum.Enum):
    page = 0
    model = 1


class Workbook:
    """Represents a hosted ArcGIS Insights Workbook."""
    def __init__(self):
        pass

    @property
    def owner(self):
        raise NotImplementedError

    @property
    def overview(self):
        raise NotImplementedError

    @property
    def folder(self):
        raise NotImplementedError

    @property
    def tags(self):
        raise NotImplementedError

    @property
    def credits(self):
        raise NotImplementedError

    @property
    def settings(self):
        raise NotImplementedError

    @property
    def usage(self):
        raise NotImplementedError

    @property
    def pages(self) -> Iterator[Page]:
        raise NotImplementedError

    @property
    def title(self):
        raise NotImplementedError

    @property
    def view(self):
        raise NotImplementedError

    @property
    def basemap(self):
        raise NotImplementedError

    @property
    def details(self):
        raise NotImplementedError

    def add_data(self, data: Dataset):
        raise NotImplementedError

    def add_page(self, page: Page):
        raise NotImplementedError

    def duplicate(self) -> Workbook:
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError
