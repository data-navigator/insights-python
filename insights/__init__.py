"""Scriptable interactions with ArcGIS Insights."""

from .card import Card
from .dataset import Dataset
from .field import Field
from .model import Model
from .organization import Organization
from .page import Page
from .result import Result
from .theme import Theme
from .workbook import Workbook

from . import aggregate
from . import analyze
from . import calculate
from . import clean
from . import enrich
from . import find
from . import predict
from . import share


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
    globals()["organization"] = organization
    return organization


__all__ = ['Card', 'Dataset', 'Field', 'Model', 'Organization', 'Page',
           'Result', 'Theme', 'Workbook', 'aggregate', 'analyze',
           'calculate', 'clean', 'enrich', 'find', 'predict', 'share',
           'sign_in']
