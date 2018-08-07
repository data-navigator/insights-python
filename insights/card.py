# codig=utf-8

"""An ArcGIS Insights Card."""

from .dataset import Dataset


class Card:
    @property
    def dataset(self) -> Dataset:
        raise NotImplementedError
