"""Generic data for ArcGIS Insights."""

from typing import Iterator
from .field import Field


class Dataset:
    """TODO"""

    @property
    def fields(self) -> Iterator[Field]:
        """TODO"""
        raise NotImplementedError

    def origin(self) -> str:
        """TODO"""
        raise NotImplementedError
