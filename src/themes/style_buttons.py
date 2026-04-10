import flet as ft
from src.themes import colors as theme

# num ficheiro theme.py ou no topo do ficheiro
btn_style = ft.ButtonStyle(
    overlay_color={
        ft.ControlState.HOVERED: ft.Colors.with_opacity(0.9, theme.AppColors.BTN_NUMBER_BG),
        ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
    },
    color={
        ft.ControlState.HOVERED: ft.Colors.WHITE,
        ft.ControlState.DEFAULT: ft.Colors.BLACK,
    },
    animation_duration=200,
)