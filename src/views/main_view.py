import flet as ft
from src.themes import colors as theme
from src.components.footer import footer
from src.components.button_option import button_option

def main_view(page: ft.Page):

    # eventos dos botoes
    def go_table(e):
        page.go("/table")

    def go_conversor(e):
        page.go("/conversor")

    def go_calculator(e):
        page.go("/calculator")

    def go_info(e):
        page.go("/info")

    async def sair(e):
        await page.window.close()

    # elementos dentro da grelha / botoes
    grid = ft.ResponsiveRow(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            button_option("icons/tabela.png", "Tabela", on_click = go_table),
            button_option("icons/convert.png", "Conversor", on_click = go_conversor),
            button_option("icons/operacoes.png", "Calculadora", on_click = go_calculator),
            button_option("icons/info.png", "Info", on_click = go_info),
            button_option("icons/desligar.png", "Sair", on_click = sair),
        ]
    )

    # estrutura da pagina que retornada
    return ft.View(
        route="/",
        padding=ft.padding.only(left=0, right=0, top=10, bottom=0),
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
                    # footer - nome
                    footer(page),
                ]
            )
        ]
    )