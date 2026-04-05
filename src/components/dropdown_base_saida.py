import flet as ft
from src.themes import colors as theme


def dropdown_base_saida(value: str = "all", on_change=None, width: int = 200):
    return ft.Dropdown(
        label="Base do resultado",
        value=value,
        width=width,
        on_select=on_change,
        options=[
            ft.dropdown.Option(key="2",   text="Binário (base 2)"),
            ft.dropdown.Option(key="8",   text="Octal (base 8)"),
            ft.dropdown.Option(key="10",  text="Decimal (base 10)"),
            ft.dropdown.Option(key="16",  text="Hexadecimal (base 16)"),
            ft.dropdown.Option(key="all", text="Mostrar todos"),
        ],
        border_color=theme.AppColors.INPUT_FIELD_BORDER,
        focused_border_color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        bgcolor=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        text_style=ft.TextStyle(color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS),
        label_style=ft.TextStyle(color=ft.Colors.with_opacity(0.7, theme.AppColors.INPUT_FIELD_BORDER_FOCUS)),
    )