"""A field present on ArcGIS Insights Data."""

import enum


class Type(enum.Enum):
    """[summary]

    [description]

    :param enum: [description]
    :type enum: [type]
    """
    Number = 0
    Text = 1
    Date = 2


class Field:
    """TODO"""

    @property
    def name(self) -> str:
        """TODO"""
        raise NotImplementedError

    @property
    def type(self) -> Type:
        """TODO"""
        raise NotImplementedError
