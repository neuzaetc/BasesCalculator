import flet as ft
from src.themes import colors as theme
from src.components.header import header
from src.components.footer import footer


def calculator_view(page: ft.Page):  
    
    # estrutura da pagina que e retornada
    return ft.View(
        route="/calculator",
        padding=ft.padding.only(left=0, right=0, top=10, bottom=0),
        bgcolor=theme.AppColors.BACKGROUND_DARK,
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    # Topo - logotipo e botao de voltar
                    header(page),
                    
                    ft.Divider(height=10, color="transparent"),
                    
                    ft.Container(
                        padding=ft.padding.only(left=80, right=80),
                        alignment=ft.Alignment(0, 0),
                        # content=grid,
                    ),
                    
                    ft.Container(expand=True),
                    # footer - nome
                    footer(page),
                ]
            )
        ]
    )