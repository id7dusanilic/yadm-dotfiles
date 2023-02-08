# QTILE Color Definitions
# Dusan Ilic 2021

from collections import namedtuple

QtileColors = namedtuple('Colors', ['accent', 'accent_light', 'nonaccent', 'bar_fg', 'bar_bg'])


color_dark_red = '#770000'
color_dark_gray = '#222222'
color_gray = '#555555'
color_light_gray = '#aaaaaa'
color_white = '#ffffff'
color_raisin = '#1d1e2c'
color_coral = '#48545e'
color_cyan = '#005577'

colors = QtileColors(color_cyan, color_cyan,  color_gray, color_white, color_dark_gray)
