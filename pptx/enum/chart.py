# encoding: utf-8

"""
Enumerations used by charts and related objects
"""

from __future__ import absolute_import

from .base import (
    Enumeration, EnumMember, ReturnValueOnlyEnumMember, XmlEnumeration,
    XmlMappedEnumMember
)


class XL_CHART_TYPE(Enumeration):
    """
    Specifies the type of a chart.

    Example::

        from pptx.enum.chart import XL_CHART_TYPE

        assert chart.chart_type == XL_CHART_TYPE.BAR_STACKED
    """

    __ms_name__ = 'XlChartType'

    __url__ = (
        'http://msdn.microsoft.com/en-us/library/office/ff838409.aspx'
    )

    __members__ = (
        EnumMember(
            'THREE_D_AREA', -4098, '3D Area.'
        ),
        EnumMember(
            'THREE_D_AREA_STACKED', 78, '3D Stacked Area.'
        ),
        EnumMember(
            'THREE_D_AREA_STACKED_100', 79, '100% Stacked Area.'
        ),
        EnumMember(
            'THREE_D_BAR_CLUSTERED', 60, '3D Clustered Bar.'
        ),
        EnumMember(
            'THREE_D_BAR_STACKED', 61, '3D Stacked Bar.'
        ),
        EnumMember(
            'THREE_D_BAR_STACKED_100', 62, '3D 100% Stacked Bar.'
        ),
        EnumMember(
            'THREE_D_COLUMN', -4100, '3D Column.'
        ),
        EnumMember(
            'THREE_D_COLUMN_CLUSTERED', 54, '3D Clustered Column.'
        ),
        EnumMember(
            'THREE_D_COLUMN_STACKED', 55, '3D Stacked Column.'
        ),
        EnumMember(
            'THREE_D_COLUMN_STACKED_100', 56, '3D 100% Stacked Column.'
        ),
        EnumMember(
            'THREE_D_LINE', -4101, '3D Line.'
        ),
        EnumMember(
            'THREE_D_PIE', -4102, '3D Pie.'
        ),
        EnumMember(
            'THREE_D_PIE_EXPLODED', 70, 'Exploded 3D Pie.'
        ),
        EnumMember(
            'AREA', 1, 'Area'
        ),
        EnumMember(
            'AREA_STACKED', 76, 'Stacked Area.'
        ),
        EnumMember(
            'AREA_STACKED_100', 77, '100% Stacked Area.'
        ),
        EnumMember(
            'BAR_CLUSTERED', 57, 'Clustered Bar.'
        ),
        EnumMember(
            'BAR_OF_PIE', 71, 'Bar of Pie.'
        ),
        EnumMember(
            'BAR_STACKED', 58, 'Stacked Bar.'
        ),
        EnumMember(
            'BAR_STACKED_100', 59, '100% Stacked Bar.'
        ),
        EnumMember(
            'BUBBLE', 15, 'Bubble.'
        ),
        EnumMember(
            'BUBBLE_THREE_D_EFFECT', 87, 'Bubble with 3D effects.'
        ),
        EnumMember(
            'COLUMN_CLUSTERED', 51, 'Clustered Column.'
        ),
        EnumMember(
            'COLUMN_STACKED', 52, 'Stacked Column.'
        ),
        EnumMember(
            'COLUMN_STACKED_100', 53, '100% Stacked Column.'
        ),
        EnumMember(
            'CONE_BAR_CLUSTERED', 102, 'Clustered Cone Bar.'
        ),
        EnumMember(
            'CONE_BAR_STACKED', 103, 'Stacked Cone Bar.'
        ),
        EnumMember(
            'CONE_BAR_STACKED_100', 104, '100% Stacked Cone Bar.'
        ),
        EnumMember(
            'CONE_COL', 105, '3D Cone Column.'
        ),
        EnumMember(
            'CONE_COL_CLUSTERED', 99, 'Clustered Cone Column.'
        ),
        EnumMember(
            'CONE_COL_STACKED', 100, 'Stacked Cone Column.'
        ),
        EnumMember(
            'CONE_COL_STACKED_100', 101, '100% Stacked Cone Column.'
        ),
        EnumMember(
            'CYLINDER_BAR_CLUSTERED', 95, 'Clustered Cylinder Bar.'
        ),
        EnumMember(
            'CYLINDER_BAR_STACKED', 96, 'Stacked Cylinder Bar.'
        ),
        EnumMember(
            'CYLINDER_BAR_STACKED_100', 97, '100% Stacked Cylinder Bar.'
        ),
        EnumMember(
            'CYLINDER_COL', 98, '3D Cylinder Column.'
        ),
        EnumMember(
            'CYLINDER_COL_CLUSTERED', 92, 'Clustered Cone Column.'
        ),
        EnumMember(
            'CYLINDER_COL_STACKED', 93, 'Stacked Cone Column.'
        ),
        EnumMember(
            'CYLINDER_COL_STACKED_100', 94, '100% Stacked Cylinder Column.'
        ),
        EnumMember(
            'DOUGHNUT', -4120, 'Doughnut.'
        ),
        EnumMember(
            'DOUGHNUT_EXPLODED', 80, 'Exploded Doughnut.'
        ),
        EnumMember(
            'LINE', 4, 'Line.'
        ),
        EnumMember(
            'LINE_MARKERS', 65, 'Line with Markers.'
        ),
        EnumMember(
            'LINE_MARKERS_STACKED', 66, 'Stacked Line with Markers.'
        ),
        EnumMember(
            'LINE_MARKERS_STACKED_100', 67, '100% Stacked Line with Markers.'
        ),
        EnumMember(
            'LINE_STACKED', 63, 'Stacked Line.'
        ),
        EnumMember(
            'LINE_STACKED_100', 64, '100% Stacked Line.'
        ),
        EnumMember(
            'PIE', 5, 'Pie.'
        ),
        EnumMember(
            'PIE_EXPLODED', 69, 'Exploded Pie.'
        ),
        EnumMember(
            'PIE_OF_PIE', 68, 'Pie of Pie.'
        ),
        EnumMember(
            'PYRAMID_BAR_CLUSTERED', 109, 'Clustered Pyramid Bar.'
        ),
        EnumMember(
            'PYRAMID_BAR_STACKED', 110, 'Stacked Pyramid Bar.'
        ),
        EnumMember(
            'PYRAMID_BAR_STACKED_100', 111, '100% Stacked Pyramid Bar.'
        ),
        EnumMember(
            'PYRAMID_COL', 112, '3D Pyramid Column.'
        ),
        EnumMember(
            'PYRAMID_COL_CLUSTERED', 106, 'Clustered Pyramid Column.'
        ),
        EnumMember(
            'PYRAMID_COL_STACKED', 107, 'Stacked Pyramid Column.'
        ),
        EnumMember(
            'PYRAMID_COL_STACKED_100', 108, '100% Stacked Pyramid Column.'
        ),
        EnumMember(
            'RADAR', -4151, 'Radar.'
        ),
        EnumMember(
            'RADAR_FILLED', 82, 'Filled Radar.'
        ),
        EnumMember(
            'RADAR_MARKERS', 81, 'Radar with Data Markers.'
        ),
        EnumMember(
            'STOCK_HLC', 88, 'High-Low-Close.'
        ),
        EnumMember(
            'STOCK_OHLC', 89, 'Open-High-Low-Close.'
        ),
        EnumMember(
            'STOCK_VHLC', 90, 'Volume-High-Low-Close.'
        ),
        EnumMember(
            'STOCK_VOHLC', 91, 'Volume-Open-High-Low-Close.'
        ),
        EnumMember(
            'SURFACE', 83, '3D Surface.'
        ),
        EnumMember(
            'SURFACE_TOP_VIEW', 85, 'Surface (Top View).'
        ),
        EnumMember(
            'SURFACE_TOP_VIEW_WIREFRAME', 86, 'Surface (Top View wireframe).'
        ),
        EnumMember(
            'SURFACE_WIREFRAME', 84, '3D Surface (wireframe).'
        ),
        EnumMember(
            'XY_SCATTER', -4169, 'Scatter.'
        ),
        EnumMember(
            'XY_SCATTER_LINES', 74, 'Scatter with Lines.'
        ),
        EnumMember(
            'XY_SCATTER_LINES_NO_MARKERS', 75, 'Scatter with Lines and No Da'
            'ta Markers.'
        ),
        EnumMember(
            'XY_SCATTER_SMOOTH', 72, 'Scatter with Smoothed Lines.'
        ),
        EnumMember(
            'XY_SCATTER_SMOOTH_NO_MARKERS', 73, 'Scatter with Smoothed Lines'
            ' and No Data Markers.'
        ),
    )


class XL_LEGEND_POSITION(XmlEnumeration):
    """
    Specifies the position of the legend on a chart.

    Example::

        from pptx.enum.chart import XL_LEGEND_POSITION

        chart.has_legend = True
        chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    """

    __ms_name__ = 'XlLegendPosition'

    __url__ = (
        'http://msdn.microsoft.com/en-us/library/office/ff745840.aspx'
    )

    __members__ = (
        XmlMappedEnumMember(
            'BOTTOM', -4107, 'b', 'Below the chart.'
        ),
        XmlMappedEnumMember(
            'CORNER', 2, 'tr', 'In the upper-right corner of the chart borde'
            'r.'
        ),
        ReturnValueOnlyEnumMember(
            'CUSTOM', -4161, 'A custom position.'
        ),
        XmlMappedEnumMember(
            'LEFT', -4131, 'l', 'Left of the chart.'
        ),
        XmlMappedEnumMember(
            'RIGHT', -4152, 'r', 'Right of the chart.'
        ),
        XmlMappedEnumMember(
            'TOP', -4160, 't', 'Above the chart.'
        ),
    )


class XL_TICK_MARK(XmlEnumeration):
    """
    Specifies a type of axis tick for a chart.

    Example::

        from pptx.enum.chart import XL_TICK_MARK

        chart.value_axis.minor_tick_mark = XL_TICK_MARK.INSIDE
    """

    __ms_name__ = 'XlTickMark'

    __url__ = (
        'http://msdn.microsoft.com/en-us/library/office/ff193878.aspx'
    )

    __members__ = (
        XmlMappedEnumMember(
            'CROSS', 4, 'cross', 'Tick mark crosses the axis'
        ),
        XmlMappedEnumMember(
            'INSIDE', 2, 'in', 'Tick mark appears inside the axis'
        ),
        XmlMappedEnumMember(
            'NONE', -4142, 'none', 'No tick mark'
        ),
        XmlMappedEnumMember(
            'OUTSIDE', 3, 'out', 'Tick mark appears outside the axis'
        ),
    )


class XL_TICK_LABEL_POSITION(XmlEnumeration):
    """
    Specifies the position of tick-mark labels on a chart axis.

    Example::

        from pptx.enum.chart import XL_TICK_LABEL_POSITION

        category_axis = chart.category_axis
        category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
    """

    __ms_name__ = 'XlTickLabelPosition'

    __url__ = (
        'http://msdn.microsoft.com/en-us/library/office/ff822561.aspx'
    )

    __members__ = (
        XmlMappedEnumMember(
            'HIGH', -4127, 'high', 'Top or right side of the chart.'
        ),
        XmlMappedEnumMember(
            'LOW', -4134, 'low', 'Bottom or left side of the chart.'
        ),
        XmlMappedEnumMember(
            'NEXT_TO_AXIS', 4, 'nextTo', 'Next to axis (where axis is not at'
            ' either side of the chart).'
        ),
        XmlMappedEnumMember(
            'NONE', -4142, 'none', 'No tick labels.'
        ),
    )
