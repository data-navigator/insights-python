"""Generic data for ArcGIS Insights."""

from typing import Iterator
from .field import Field


class Dataset:
    @property
    def fields(self) -> Iterator[Field]:
        raise NotImplementedError
