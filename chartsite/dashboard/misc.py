from math import pi
import numpy as np
from bokeh.models import Arc, Circle, ColumnDataSource, Plot, Range1d, Ray, Text

def gauge(risk):
    def data(value):
        return dict(value=value, units="data")
    # Зона для рисования
    plot = Plot( plot_width=500, plot_height=240)
    radius = 0.7
    row_len = radius*0.95
    y_ = -100

    ##Зоны монометра
    # Зелёная зона
    glyph = Arc(x=0, y=y_, radius=radius, start_angle=pi, end_angle=pi * 2 / 3,
                direction="clock", line_color='green',line_width=40)
    plot.add_glyph(glyph)
    # Жёлтая зона
    glyph = Arc(x=0, y=y_, radius=radius, start_angle=pi * 2 / 3, end_angle=pi * 1 / 3, direction="clock",
                line_color='yellow', line_width=40)
    plot.add_glyph(glyph)
    # Красная зона
    glyph = Arc(x=0, y=y_, radius=radius, start_angle=pi * 1 / 3, end_angle=0, direction="clock", line_color='red',
                line_width=40)
    plot.add_glyph(glyph)

    ##стрелка
    angle = (1-risk)*pi
    plot.add_glyph(Ray(x=0, y=y_, length=data(row_len), angle=angle, line_color="black", line_width=3))
    plot.add_glyph(Ray(x=0, y=0, length=data(row_len), angle=0, line_color="black", line_width=3, line_alpha=0.1   ))
    return plot



