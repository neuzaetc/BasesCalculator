import flet as ft

from src.views.main_view import main_view 
from src.views.conversor_view import conversor_view
from src.views.info_view import info_view
from src.views.calculator_view import calculator_view
from src.views.tables_view import tables_view

async def main(page: ft.Page):
    page.title = "Calculadora de Conversão de Bases Numéricas"
    page.padding = 0
    page.window.width = 900
    page.window.height = 660
    page.window.min_width = 900
    page.window.min_height= 660
    page.fonts = {
         "OpenSans": "fonts/OpenSans-VariableFont_wdth,wght.ttf",
    }
    page.theme = ft.Theme(font_family="OpenSans")

    # Route's definicao caminhos
    async def on_route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(main_view(page))
        elif page.route == "/conversor":
            page.views.append(conversor_view(page))
        elif page.route == "/calculator":
            page.views.append(calculator_view(page))
        elif page.route == "/table":
                page.views.append(tables_view(page))
        elif page.route == "/info":
            page.views.append(info_view(page))
        page.update()

    async def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.update()

    page.on_route_change = on_route_change
    page.on_view_pop = view_pop

    await on_route_change(None)

ft.run(main)