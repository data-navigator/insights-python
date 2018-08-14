# coding=utf-8

"""An ArcGIS Insights Organization."""

from typing import Iterator
from arcgis import GIS
from arcgis.gis import User
from .workbook import Workbook


class Organization:
    """Represents an ArcGIS Insights Organization on either ArcGIS Online or
    ArcGIS Enterprise."""
    def __init__(self, url, username, password):
        gis = GIS(url, username, password)
        users = gis.users
        user = users.me
        query = f'+type:"Insights Workbook" +orgid:{user.orgId}'
        content = gis.content
        self._url = url
        self._user = user
        self._users = users.search("")
        self._org_id = user.orgId
        self._workbooks = content.search(query)

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
