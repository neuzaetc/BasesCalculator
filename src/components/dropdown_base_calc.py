import flet as ft
from src.themes import colors as theme


def dropdown_base_calc(value: str = "10", on_change=None):
    return ft.Dropdown(
        label="Base",
        value=value,
        width=220,       
        on_select=on_change,
        content_padding=ft.padding.symmetric(horizontal=12, vertical=7),
        options=[
            ft.dropdown.Option(key="2",  text="Binário (base 2)"),
            ft.dropdown.Option(key="8",  text="Octal (base 8)"),
            ft.dropdown.Option(key="10", text="Decimal (base 10)"),
            ft.dropdown.Option(key="16", text="Hexadecimal (base 16)"),
        ],
        border_color=theme.AppColors.INPUT_FIELD_BORDER,
        focused_border_color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        bgcolor=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        text_style=ft.TextStyle(color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS),
        label_style=ft.TextStyle(color=ft.Colors.with_opacity(0.7, theme.AppColors.INPUT_FIELD_BORDER_FOCUS)),
    )