import flet as ft
from src.themes import colors as theme

def footer(page: ft.Page):
    return ft.Stack(
        height=120,
        controls=[
            # imagem no fundo extendida horizontalmente
            ft.Image(
                src="img/illustration.png",
                expand=True,
            ),
            # lado esquerdo
            ft.Container(
                expand=True,
                # colado ao fundo esquerdo
                alignment=ft.Alignment(-1, 1),
                padding=ft.padding.only(left=20, bottom=10),
                content=ft.Column(
                    spacing=2,
                    tight=True,
                    controls=[
                        ft.Text(
                            "INFORMATICA WEB MOVEL E NA NUVEM",
                            size=12,
                            font_family="OpenSans",
                            weight=ft.FontWeight.BOLD,
                            color=theme.AppColors.TEXT_COLOR_DARK,
                        ),
                        ft.Text(
                            "ECOSSISTEMA WEB MOVEL E NUVEM - 2025/26",
                            size=10,
                            font_family="OpenSans",
                            weight=ft.FontWeight.NORMAL,
                            color=theme.AppColors.TEXT_COLOR_DARK,
                        ),
                    ]
                )
            ),
            # lado direito
            ft.Container(
                expand=True,
                alignment=ft.Alignment(1, 1),
                padding=ft.padding.only(right=20, bottom=10),
                content=ft.Text(
                    "Neuza Crisóstomo nº 53482",
                    size=12,
                    font_family="OpenSans",
                    weight=ft.FontWeight.NORMAL,
                    color=theme.AppColors.TEXT_COLOR_DARK,
                ),
            )
        ]
    )