# QTILE Layouts definition
# Dusan Ilic 2021

from libqtile import layout
from qtile_colors import colors

margin = 6
single_margin = 6

shared_config = {
    'border_width': 3,
    'margin': margin,
    'border_focus': colors.accent,
    'border_normal': colors.nonaccent,
}

layouts = [
    # Columns layout
    layout.Columns(
        margin_on_single=single_margin,
        border_focus_stack=colors.accent,
        border_normal_stack=colors.nonaccent,
        **shared_config
    ),
    # Monad Tall layout
    layout.MonadTall(
        single_margin=single_margin,
        single_border_width=0,
        ratio=0.6,
        **shared_config
    ),
    # Max layout
    layout.Max(),
    # Monad Wide layout
    layout.MonadWide(
        single_margin=single_margin,
        single_border_width=0,
        ratio=0.6,
        **shared_config
    ),
]
