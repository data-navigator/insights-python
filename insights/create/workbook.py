"""Create ArcGIS Insights workbooks."""

from arcgis.gis import Item
from .. import Workbook


def workbook(item: Item) -> Workbook:
    """[summary]

    [description]

    :param title: [description]
    :type title: str
    :raises NotImplementedError: [description]
    :return: [description]
    :rtype: Workbook
    """
    print(title)
    raise NotImplementedError
