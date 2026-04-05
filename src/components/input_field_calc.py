import flet as ft
from src.themes import colors as theme


def input_field_calc(field_id: str, label: str, hint: str, on_change=None):
    return ft.TextField(
        data=field_id,
        label=label,
        hint_text=hint,
        on_change=on_change,
        content_padding=ft.padding.symmetric(horizontal=12, vertical=7),
        width=400,          # largura fixa para a calculadora
        bgcolor="transparent",
        border_color=theme.AppColors.INPUT_FIELD_BORDER,
        focused_border_color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        border_radius=5,
        border_width=1,
        text_style=ft.TextStyle(color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS),
        label_style=ft.TextStyle(
            color=ft.Colors.with_opacity(0.7, theme.AppColors.INPUT_FIELD_BORDER_FOCUS),
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.with_opacity(0.4, theme.AppColors.INPUT_FIELD_BORDER_FOCUS),
        ),
    )