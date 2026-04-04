import flet as ft
from src.views.main_view import main_view 

async def main(page: ft.Page):
    page.title = "Calculadora de Conversão de Bases Numéricas"
    page.padding = 0
    page.window.width = 900
    page.window.height = 650
    page.window.min_width = 900
    page.window.min_height= 650
    page.fonts = {
         "OpenSans": "fonts/OpenSans-VariableFont_wdth,wght.ttf",
    }
    page.theme = ft.Theme(font_family="OpenSans")

    async def on_route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(main_view(page))
        page.update()

    async def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.update()

    page.on_route_change = on_route_change
    page.on_view_pop = view_pop

    await on_route_change(None)

ft.run(main)