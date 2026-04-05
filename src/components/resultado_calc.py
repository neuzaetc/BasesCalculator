import flet as ft
from src.themes import colors as theme


def resultado_calc():
    resultado_bin = ft.Text(color=theme.AppColors.TEXT_COLOR_DARK)
    resultado_oct = ft.Text(color=theme.AppColors.TEXT_COLOR_DARK)
    resultado_dec = ft.Text(color=theme.AppColors.TEXT_COLOR_DARK)
    resultado_hex = ft.Text(color=theme.AppColors.TEXT_COLOR_DARK)

    container = ft.Container(
        width=600,
        height=110,   # <-- diminui de 120 para 80
        bgcolor=ft.Colors.with_opacity(0.1, theme.AppColors.INPUT_FIELD_BORDER_FOCUS),
        border_radius=10,
        padding=10,
        content=ft.Column(
            spacing=3,  # <-- menos espaço entre linhas
            controls=[
                resultado_bin,
                resultado_oct,
                resultado_dec,
                resultado_hex,
            ]
        )
    )

    return container, resultado_bin, resultado_oct, resultado_dec, resultado_hex