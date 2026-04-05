import flet as ft
from src.themes import colors as theme


def input_bits(on_change=None):
    return ft.TextField(
        label="Número de bits (n)",
        hint_text="Ex: 4",
        value="1",
        width=150,
        height=45,
        on_change=on_change,
        bgcolor="transparent",
        border_color="#4a6fa5",
        focused_border_color="#ffffff",
        border_radius=10,
        border_width=1,
        text_style=ft.TextStyle(color="#ffffff"),
        label_style=ft.TextStyle(
            color=ft.Colors.with_opacity(0.7, "#ffffff"),
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.with_opacity(0.4, "#ffffff"),
        ),
    )