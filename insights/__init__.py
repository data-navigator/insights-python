"""Scriptable interactions with ArcGIS Insights."""

from typing import Iterator
from arcgis import GIS
from arcgis.gis import User

from .card import Card
from .dataset import Dataset
from .field import Field
from .model import Model
from .page import Page
from .result import Result
from .theme import Theme
from .workbook import Workbook


class Organization:
    """Represents an ArcGIS Insights Organization on either ArcGIS Online or
    ArcGIS Enterprise."""
    def __init__(self, url, username, password):
        gis = GIS(url, username, password)
        content = gis.content
        users = gis.users
        user = users.me
        query = f'+type:"Insights Workbook" +orgid:{user.orgId}'
        self._url = url
        self._user = user
        self._users = users.search("")
        self._org_id = user.orgId
        self._workbooks = [Workbook(item) for item in content.search(query)]
        self._gis = gis

    @property
    def org_id(self) -> str:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._org_id

    @property
    def url(self) -> str:
        """[summary]

        [description]
        """
        return self._url

    @property
    def workbooks(self) -> Iterator[Workbook]:
        """[summary]

        [description]

        :raises NotImplementedError: [description]
        """
        return self._workbooks

    @property
    def user(self) -> User:
        """[summary]

        [description]

        :return: [description]
        :rtype: User
        """
        return self._user

    @property
    def users(self) -> Iterator[User]:
        """[summary]

        [description]

        :return: [description]
        :rtype: Iterator[User]
        """
        return self._users



def sign_in(url: str = "https://insights.mapsdevext.arcgis.com",
            username: str = "clint.dow",
            password: str = "@1492DataInsights") -> Organization:
    """[summary]

    [description]

    :param url: [description]
    :type url: str
    :param username: [description]
    :type username: str
    :param password: [description]
    :type password: str
    :return: [description]
    :rtype: User
    """
    organization = Organization(url, username, password)
    return organization


__all__ = ['Card', 'Dataset', 'Field', 'Model', 'Organization', 'Page',
           'Result', 'Theme', 'Workbook', 'sign_in']
