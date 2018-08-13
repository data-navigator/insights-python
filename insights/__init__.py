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

__all__ = ['Card', 'Dataset', 'Field', 'Model', 'Organization', 'Page',
           'Result', 'Theme', 'Workbook', 'aggregate', 'analyze',
           'calculate', 'clean', 'enrich', 'find', 'predict', 'share']
