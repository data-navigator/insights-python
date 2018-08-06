"""Possible visualizations to be set on an ArcGIS Insights Card."""

import enum


class Categories(enum.Enum):
    Measurement = 0
    Relationship = 1
    Change = 2
    Interaction = 3
    Distribution = 4
    PartToWhole = 5
