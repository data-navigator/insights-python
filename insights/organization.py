# coding=utf-8

"""An ArcGIS Insights Organization."""


class Organization:
    """Represents an ArcGIS Insights Organization on either ArcGIS Online or
    ArcGIS Enterprise."""
    def __init__(self, url=None, user=None, password=None):
        self.__url = url
        self.user = user
        self.password = password

    @property
    def name(self):
        raise NotImplementedError

    @property
    def url(self):
        return self.__url

    @property
    def workbooks(self):
        raise NotImplementedError

    @property
    def user(self):
        return self.user
