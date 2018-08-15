# codig=utf-8

"""An ArcGIS Insights Card."""

from typing import Iterable
from .layer import Layer


class Card:
    """[summary]

    [description]
    """
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.content = kwargs['content']
        self.title = kwargs['title']

    def __str__(self):
        return f"{self.type} {self.title}"

    def __repr__(self):
        return str(self)

    @property
    def layers(self) -> Iterable[Layer]:
        """[summary]

        [description]

        :return: [description]
        :rtype: Iterable[Layer]
        """
        return [Layer(**layer) for layer in self.content['layers']]
