# codig=utf-8

"""An ArcGIS Insights Card."""

from .dataset import Dataset


class Card:
    """TODO"""
    @property
    def dataset(self) -> Dataset:
        """TODO"""
        raise NotImplementedError

    @property
    def visualization(self):
        """TODO"""
        raise NotImplementedError
