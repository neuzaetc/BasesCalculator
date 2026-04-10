import flet as ft
from src.themes import colors as theme
from src.components.header import header
from src.components.footer import footer
from src.components.input_bits import input_bits
from src.models.tabela_model import TabelaModel
from src.themes.style_buttons import btn_style


def tables_view(page: ft.Page):  
    
    # valida que o input so aceita digitos
    def validar_bits(e):
        e.control.value = ''.join([c for c in e.control.value if c.isdigit()])
        e.control.update()

    tabela_container = ft.Column(spacing=5)
    total_text       = ft.Text(value="", color=theme.AppColors.TEXT_COLOR_DARK, size=14, italic=True)
    selector_bits    = input_bits(on_change=validar_bits)

    # gera a tabela de gray consoante o numero de bits introduzido
    def gerar_tabela(e):
        tabela_container.controls.clear()

        # verifica se o campo esta vazio
        if not selector_bits.value:
            return

        n_bits = int(selector_bits.value)

        # valida o numero de bits no model
        valido, mensagem = TabelaModel.validar_bits(n_bits)
        if not valido:
            snack = ft.SnackBar(
            content=ft.Text(mensagem, color="#ffffff"),
            bgcolor="#c0392b",
            open=True,
            )
            page.overlay.append(snack)
            page.update()
            return

        # gera a tabela
        tabela = TabelaModel.gerar_tabela_gray(n_bits)
        total_text.value = TabelaModel.total_entradas(n_bits)

        # cabecalho da tabela
        tabela_container.controls.append(
            ft.Row([
                ft.Text("Decimal",     weight=ft.FontWeight.BOLD, width=100, color=theme.AppColors.TEXT_COLOR_DARK),
                ft.Text("Binário",     weight=ft.FontWeight.BOLD, width=150, color=theme.AppColors.TEXT_COLOR_DARK),
                ft.Text("Código Gray", weight=ft.FontWeight.BOLD, width=150, color=theme.AppColors.TEXT_COLOR_DARK),
            ])
        )

        # linhas da tabela
        for decimal, binario, gray in tabela:
            tabela_container.controls.append(
                ft.Row([
                    ft.Text(str(decimal), width=100, color=theme.AppColors.TEXT_COLOR_DARK),
                    ft.Text(binario,      width=150, color=theme.AppColors.TEXT_COLOR_DARK),
                    ft.Text(gray,         width=150, color="cyan"),
                ])
            )
        page.update()

    # limpa a tabela e o total
    def limpar(e):
        tabela_container.controls.clear()
        total_text.value = ""
        selector_bits.value = ""
        selector_bits.update()
        page.update()

    return ft.View(
        route="/table",
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
                                controls=[
                                    ft.Text("Tabelas de Código de Gray", size=24, weight=ft.FontWeight.BOLD, color=theme.AppColors.TEXT_COLOR_DARK),
                                    ft.Divider(),
                                    ft.Text("Escolha o número de bits e veja a sequência binária e o código Gray correspondente.", size=15, color=theme.AppColors.TEXT_COLOR_DARK),
                                    ft.Divider(height=5, color="transparent"),

                                    # input e botoes na mesma linha
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            selector_bits,
                                            ft.Row(
                                                spacing=10,
                                                controls=[
                                                    ft.ElevatedButton("Gerar Tabela", on_click=gerar_tabela, width=140, style=btn_style),
                                                    ft.ElevatedButton("Limpar", on_click=limpar, width=100, style=btn_style),
                                                ]
                                            ),
                                        ]
                                    ),

                                    ft.Divider(height=2, color="transparent"),
                                    total_text,

                                    # tabela com scroll
                                   ft.Container(
                                        width=600,
                                        height=200,
                                        bgcolor=ft.Colors.with_opacity(0.1, "#ffffff"),
                                        border_radius=10,
                                        padding=10,
                                        content=ft.Column(
                                            controls=[
                                                total_text,
                                                tabela_container,
                                            ],
                                            scroll=ft.ScrollMode.AUTO,
                                        ),
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