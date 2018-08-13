# coding=utf-8

"""An ArcGIS Insights Organization."""

from typing import Iterator
from .workbook import Workbook


class Organization:
    """Represents an ArcGIS Insights Organization on either ArcGIS Online or
    ArcGIS Enterprise."""
    def __init__(self, url=None, user=None, password=None):
        self.__url = url
        self.user = user
        self.password = password

    @property
    def name(self) -> str:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def url(self) -> str:
        """[summary]

        [description]
        """
        return self.__url

    @property
    def workbooks(self) -> Iterator[Workbook]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        raise NotImplementedError

    @property
    def user(self):
        """[summary]

        [description]
        """
        return self.user
