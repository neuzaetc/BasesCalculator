import flet as ft
from src.themes import colors as theme
from src.components.header import header
from src.components.footer import footer
from src.components.input_field import input_field
from src.models.util_model import UtilModel
from src.models.conversor_model import ConversorModel


def conversor_view(page: ft.Page):  
    
    # atualiza todos os campos com os valores convertidos
    # exceto o campo que esta a ser editado pelo utilizador
    def atualizar_campos(valor: str, base: int, campo_ativo):
        resultados = ConversorModel.converter_para_todas(valor, base)
        if campo_ativo != campo_binario:
            campo_binario.value     = resultados["2"]
        if campo_ativo != campo_octal:
            campo_octal.value       = resultados["8"]
        if campo_ativo != campo_decimal:
            campo_decimal.value     = resultados["10"]
        if campo_ativo != campo_hexadecimal:
            campo_hexadecimal.value = resultados["16"]
        page.update()


    # validar os inputs consoante as bases
    def validar_binario(e):
        # no caso do binario sao removidos os espacos para a validacao
        valor_sem_espacos = e.control.value.replace(" ", "")
        valor_sem_espacos = UtilModel.validar_caracteres(valor_sem_espacos, 2)
        atualizar_campos(valor_sem_espacos, 2, campo_binario)

     # valida os caracteres octais (0-7) e atualiza os restantes campos
    def validar_octal(e):
        e.control.value = UtilModel.validar_caracteres(e.control.value, 8)
        atualizar_campos(e.control.value, 8, campo_octal)

    # valida os caracteres decimais (0-9) e atualiza os restantes campos
    def validar_decimal(e):
        e.control.value = UtilModel.validar_caracteres(e.control.value, 10)
        atualizar_campos(e.control.value, 10, campo_decimal)

    # valida os caracteres hexadecimais (0-9, A-F) e atualiza os restantes campos
    def validar_hexadecimal(e):
        e.control.value = UtilModel.validar_caracteres(e.control.value, 16)
        atualizar_campos(e.control.value, 16, campo_hexadecimal)


    # declarar os campos de input
    campo_binario     = input_field("binario",     "Valor Binário",     "Ex: 1010", on_change=validar_binario)
    campo_octal       = input_field("octal",       "Valor Octal",       "Ex: 17",   on_change=validar_octal)
    campo_decimal     = input_field("decimal",     "Valor Decimal",     "Ex: 255",  on_change=validar_decimal)
    campo_hexadecimal = input_field("hexadecimal", "Valor Hexadecimal", "Ex: FF",   on_change=validar_hexadecimal)


    async def limpar(e):
        UtilModel.limpar_campos(
            campo_binario,
            campo_octal,
            campo_decimal,
            campo_hexadecimal,
        )
        page.update()
        
    
    return ft.View(
        route="/conversor",
        padding=ft.padding.only(left=0, right=0, top=10, bottom=0),
        bgcolor=theme.AppColors.BACKGROUND_DARK,
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    
                    # header sempre no topo
                    header(page),

                    # conteudo main - inputs e botao limpar
                    ft.Container(
                        expand=True,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Container(
                            width=600,
                            content=ft.Column(
                                tight=True,
                                controls=[
                                    ft.Text("Calculadora de Conversão de Bases Numéricas", size=24, weight=ft.FontWeight.BOLD, color=theme.AppColors.TEXT_COLOR_DARK),
                                    ft.Divider(),
                                    ft.Text("Converte valores Binários, Octais, Decimais e Hexadecimais.", size=15, color=theme.AppColors.TEXT_COLOR_DARK),
                                    ft.Divider(height=5, color="transparent"),
                                    campo_binario,
                                    campo_octal,
                                    campo_decimal,
                                    campo_hexadecimal,
                                    ft.Divider(height=5, color="transparent"),
                                    ft.ElevatedButton("Limpar", on_click=limpar, width=100),
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