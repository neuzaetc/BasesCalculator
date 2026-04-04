import flet as ft
from src.themes import colors as theme

def header(page: ft.Page):

    text = ft.Text(
        "Voltar ao Menu",
        color=theme.AppColors.TEXT_COLOR_DARK,
        weight=ft.FontWeight.W_300,
    )

    # hoover botao voltar
    def on_hover(e):
        e.control.shadow = (
            ft.BoxShadow(
                spread_radius=1,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.1, "#ffffff"),
                offset=ft.Offset(0, 0),
            )
            if e.data
            else ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.0, "#00000000"),
                offset=ft.Offset(0, 4),
            )
        )
        text.weight = ft.FontWeight.BOLD if e.data else ft.FontWeight.W_300
        text.update()
        e.control.update()

    # estrutura header lgo uni / botao voltar
    return ft.Container(
        col={"xs": 12, "sm": 12, "md": 12},
        padding=ft.padding.only(left=20, right=20),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src="icons/logotipo-ubi-2016.svg",
                    height=80,
                ),
                ft.Container(
                    on_click=lambda e: page.go("/"),
                    on_hover=on_hover,
                    animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.ARROW_BACK,
                                color=theme.AppColors.TEXT_COLOR_DARK,
                            ),
                            text,
                        ]
                    )
                ),
            ]
        )
    )