# coding=utf-8

"""Chart-style visualization on an ArcGIS Insights Card."""

from .. import Card
from .. import Data


def bar_chart(data: Data) -> Card:
    raise NotImplementedError


def column_chart(data: Data) -> Card:
    raise NotImplementedError


def donut_chart(data: Data) -> Card:
    raise NotImplementedError


def histogram(data: Data) -> Card:
    raise NotImplementedError


def scatter_plot(data: Data) -> Card:
    raise NotImplementedError


def time_series_graph(data: Data) -> Card:
    raise NotImplementedError


def treemap(data: Data) -> Card:
    raise NotImplementedError


def bubble_chart(data: Data) -> Card:
    raise NotImplementedError


def line_chart(data: Data) -> Card:
    raise NotImplementedError


def chord_diagram(data: Data) -> Card:
    raise NotImplementedError


def data_clock(data: Data) -> Card:
    raise NotImplementedError


def heat_chart(data: Data) -> Card:
    raise NotImplementedError


def box_plot(data: Data) -> Card:
    raise NotImplementedError


def link_chart(data: Data) -> Card:
    raise NotImplementedError


def scatter_plot_matrix(data: Data) -> Card:
    raise NotImplementedError


def combo_chart(data: Data) -> Card:
    raise NotImplementedError
