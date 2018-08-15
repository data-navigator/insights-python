# coding=utf-8

"""A layer on an ArcGIS Insights card."""


class Layer:
    """TODO"""
    def __init__(self, **layer):
        self._dataset_id = layer['datasetId']
        self.hidden = layer.get('hidden', False)
        self.transparency = layer.get('transparency', 0)
        self.drawing_options = layer.get('drawingOptions', {})

    @property
    def id(self) -> str:
        """[summary]

        [description]

        :return: [description]
        :rtype: str
        """
        return self._dataset_id
