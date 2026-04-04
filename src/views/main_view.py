import flet as ft
from src.themes import colors as theme


def main_view(page: ft.Page):
    
    def menu_item(icon_path, label, on_click=None):
        return ft.Container(
            col={"xs": 6, "sm": 4, "md": 3},
            padding = 10,
            on_click = on_click,
            content = ft.Container(
                bgcolor="#2a3f7e",
                border_radius=15,
                height=150,
                padding=20,
                alignment=ft.Alignment(0, 0),
                border=ft.border.all(2, "#ffffff"),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src=icon_path,  
                            width=60,
                            height=60,
                        ),
                        ft.Text(
                            value=label,
                            color="#ffffff",
                            weight=ft.FontWeight.W_600,
                        ),
                    ]
                )
            )
        )
        
    # eventos dos botoes
    def go_tabela(e):
        page.go("/tabela")

    def go_conversor(e):
        page.go("/conversor")

    def go_calculadora(e):
        page.go("/calculadora")

    def go_info(e):
        page.go("/info")

    def sair(e):
        page.window_close()

    grid = ft.ResponsiveRow(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            menu_item("icons/tabela.png", "Tabela", on_click=go_tabela),
            menu_item("icons/convert.png", "Conversor", on_click=go_conversor),
            menu_item("icons/operacoes.png", "Calculadora", on_click=go_calculadora),
            menu_item("icons/info.png", "Info", on_click=go_info),
            menu_item("icons/desligar.png", "Sair", on_click=sair),
        ]
    )

    return ft.View(
        route="/",
        padding=ft.padding.only(left=0, right=0, top=20, bottom=0),
        bgcolor=theme.AppColors.BACKGROUND_DARK,
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=20),
                        content=ft.Image(
                        src="icons/logotipo-ubi-2016.svg",
                        height=80,
                    ),
                    ),
                    ft.Divider(height=10, color="transparent"),
                    ft.Container(
                        padding=ft.padding.only(left=80, right=80),
                        alignment=ft.Alignment(0, 0),
                        content=grid,
                    ),
                    ft.Container(expand=True),
                    ft.Stack(
                        height=110,
                        controls=[
                            ft.Image(
                                src="img/illustration.png",
                                expand=True,
                            ),
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
                ]
            )
        ]
    )