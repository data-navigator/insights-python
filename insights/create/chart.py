# coding=utf-8

"""Chart-style visualization on an ArcGIS Insights Card."""

from .. import Card, Dataset


def bar_chart(data: Dataset) -> Card:
    raise NotImplementedError


def column_chart(data: Dataset) -> Card:
    raise NotImplementedError


def donut_chart(data: Dataset) -> Card:
    raise NotImplementedError


def histogram(data: Dataset) -> Card:
    raise NotImplementedError


def scatter_plot(data: Dataset) -> Card:
    raise NotImplementedError


def time_series_graph(data: Dataset) -> Card:
    raise NotImplementedError


def treemap(data: Dataset) -> Card:
    raise NotImplementedError


def bubble_chart(data: Dataset) -> Card:
    raise NotImplementedError


def line_chart(data: Dataset) -> Card:
    raise NotImplementedError


def chord_diagram(data: Dataset) -> Card:
    raise NotImplementedError


def data_clock(data: Dataset) -> Card:
    raise NotImplementedError


def heat_chart(data: Dataset) -> Card:
    raise NotImplementedError


def box_plot(data: Dataset) -> Card:
    raise NotImplementedError


def link_chart(data: Dataset) -> Card:
    raise NotImplementedError


def scatter_plot_matrix(data: Dataset) -> Card:
    raise NotImplementedError


def combo_chart(data: Dataset) -> Card:
    raise NotImplementedError
