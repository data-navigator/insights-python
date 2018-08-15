"""Generic data for ArcGIS Insights."""


class Dataset:
    """TODO"""
    def __init__(self, **dataset):
        self.dataset = dataset['dataset']
        self.result = dataset.get('result', False)

    def __str__(self):
        return self.dataset

    def __repr__(self):
        return str(self)
