import flet as ft
from src.themes import colors as theme
from src.components.header import header
from src.components.footer import footer
from src.components.input_field_calc import input_field_calc
from src.components.dropdown_base_calc import dropdown_base_calc
from src.components.dropdown_base_saida import dropdown_base_saida
from src.components.resultado_calc import resultado_calc
from src.models.calculadora_model import CalculadoraModel
from src.models.util_model import UtilModel


def calculator_view(page: ft.Page):

    # guarda o ultimo resultado decimal para reconversao
    resultado_decimal = [None]

    # componentes
    base_num1  = dropdown_base_calc(value="10")
    base_num2  = dropdown_base_calc(value="10")
    base_saida = dropdown_base_saida()
    container, resultado_bin, resultado_oct, resultado_dec, resultado_hex = resultado_calc()

    # validacao dos inputs consoante a base selecionada
    def validar_num1(e):
        base = int(base_num1.value or "10")
        e.control.value = UtilModel.validar_caracteres(e.control.value, base)
        e.control.update()

    def validar_num2(e):
        base = int(base_num2.value or "10")
        e.control.value = UtilModel.validar_caracteres(e.control.value, base)
        e.control.update()

    num1_input = input_field_calc("num1", "Valor 1", "Ex: 1010", on_change=validar_num1)
    num2_input = input_field_calc("num2", "Valor 2", "Ex: 1010", on_change=validar_num2)

    # limpa o input quando a base muda e altera os hints
    def on_change_base_num1(e):
        num1_input.value     = ""
        num1_input.hint_text = UtilModel.HINTS.get(base_num1.value, "Ex: 0")
        num1_input.update()

    def on_change_base_num2(e):
        num2_input.value     = ""
        num2_input.hint_text = UtilModel.HINTS.get(base_num2.value, "Ex: 0")
        num2_input.update()

    base_num1.on_select = on_change_base_num1
    base_num2.on_select = on_change_base_num2

    # atualiza os textos de resultado
    def atualizar_resultados(resultados: dict):
        resultado_bin.value = resultados["2"]
        resultado_oct.value = resultados["8"]
        resultado_dec.value = resultados["10"]
        resultado_hex.value = resultados["16"]
        page.update()

    # executa a operacao e atualiza os resultados
    def calcular(operacao: str):
        if not num1_input.value or not num2_input.value:
            return
        base1 = int(base_num1.value or "10")
        base2 = int(base_num2.value or "10")

        resultados = CalculadoraModel.calcular_para_todas(
            num1_input.value.strip(),
            num2_input.value.strip(),
            base1,
            base2,
            operacao,
        )

        if resultados["erro"]:
            resultado_bin.value = f"Erro: {resultados['erro']}"
            resultado_oct.value = ""
            resultado_dec.value = ""
            resultado_hex.value = ""
            page.update()
            return

        resultado_decimal[0] = resultados["decimal"]
        resultados_filtrados = CalculadoraModel.resultado_para_base(
            resultado_decimal[0], base_saida.value
        )
        atualizar_resultados(resultados_filtrados)

    def somar(e):
        calcular("+")

    def subtrair(e):
        calcular("-")

    def multiplicar(e):
        calcular("*")

    def dividir(e):
        calcular("/")

    # limpa todos os campos e resultados
    def limpar(e):
        num1_input.value     = ""
        num2_input.value     = ""
        resultado_bin.value  = ""
        resultado_oct.value  = ""
        resultado_dec.value  = ""
        resultado_hex.value  = ""
        resultado_decimal[0] = None
        num1_input.update()
        num2_input.update()
        page.update()

    # reconverte o resultado quando a base de saida muda
    def on_change_base_saida(e):
        if resultado_decimal[0] is None:
            return
        resultados = CalculadoraModel.resultado_para_base(
            resultado_decimal[0], base_saida.value
        )
        atualizar_resultados(resultados)

    base_saida.on_select = on_change_base_saida

    return ft.View(
        route="/calculator",
        padding=ft.padding.only(left=0, right=0, top=10, bottom=0),
        bgcolor=theme.AppColors.BACKGROUND_DARK,
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    # header sempre no topo
                    header(page),

                    # conteudo centrado
                    ft.Container(
                        expand=True,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Container(
                            width=600,
                            content=ft.Column(
                                tight=True,
                                spacing=10,
                                controls=[
                                    ft.Text("Calculadora de Bases Numéricas", size=24, weight=ft.FontWeight.BOLD, color=theme.AppColors.TEXT_COLOR_DARK),
                                    ft.Divider(),
                                    ft.Text("Indique os valores, escolha as bases de origem e a operação desejada.", size=15, color=theme.AppColors.TEXT_COLOR_DARK),

                                    # container com os resultados
                                    container,

                                    # valor 1 com base
                                    ft.Row(
                                        spacing=10,
                                        controls=[
                                            ft.Container(
                                                height=45,
                                                expand=True,
                                                content=num1_input,
                                            ),
                                            ft.Container(
                                                height=45,
                                                width=225,
                                                content=base_num1,
                                            ),
                                        ]
                                    ),

                                    # valor 2 com base
                                    ft.Row(
                                        spacing=10,
                                        controls=[
                                            ft.Container(
                                                height=45,
                                                expand=True,
                                                content=num2_input,
                                            ),
                                            ft.Container(
                                                height=45,
                                                width=225,
                                                content=base_num2,
                                            ),
                                        ]
                                    ),

                                    # base resultado + botoes na mesma linha
                                    ft.Row(
                                        spacing=10,
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            base_saida,
                                            ft.Row(
                                                spacing=5,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        content=ft.Text("+", size=20, weight=ft.FontWeight.BOLD),
                                                        on_click=somar, width=42,
                                                        style=ft.ButtonStyle(padding=ft.padding.all(0), alignment=ft.Alignment(0, 0)),
                                                    ),
                                                    ft.ElevatedButton(
                                                        content=ft.Text("-", size=20, weight=ft.FontWeight.BOLD),
                                                        on_click=subtrair, width=42,
                                                        style=ft.ButtonStyle(padding=ft.padding.all(0), alignment=ft.Alignment(0, 0)),
                                                    ),
                                                    ft.ElevatedButton(
                                                        content=ft.Text("×", size=20, weight=ft.FontWeight.BOLD),
                                                        on_click=multiplicar, width=42,
                                                        style=ft.ButtonStyle(padding=ft.padding.all(0), alignment=ft.Alignment(0, 0)),
                                                    ),
                                                    ft.ElevatedButton(
                                                        content=ft.Text("÷", size=20, weight=ft.FontWeight.BOLD),
                                                        on_click=dividir, width=42,
                                                        style=ft.ButtonStyle(padding=ft.padding.all(0), alignment=ft.Alignment(0, 0)),
                                                    ),
                                                    ft.ElevatedButton(
                                                        content=ft.Text("Limpar", size=14, weight=ft.FontWeight.W_600),
                                                        on_click=limpar, width=100,
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                ]
                            )
                        )
                    ),

                    # footer sempre no fundo
                    footer(page),
                ]
            )
        ]
    )