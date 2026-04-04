import flet as ft
from src.themes import colors as theme
from src.components.header import header
from src.components.footer import footer


def info_view(page: ft.Page):  
    
    # estrutura da pagina que e retornada
    return ft.View(
        route="/info",
        padding=ft.padding.only(left=0, right=0, top=10, bottom=0),
        bgcolor=theme.AppColors.BACKGROUND_DARK,
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    # Topo - logotipo e botao de voltar
                    header(page),
                    
                    ft.Divider(height=10, color="transparent"),
                    
                    # Container com a descricao do trabalho
                    ft.Container(
                        expand=True,
                        padding=ft.padding.only(left=100, right=100),
                        content=ft.Column(
                            expand=True,    
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Text("Enunciado do Trabalho Prático Intermédio", size=24, weight=ft.FontWeight.BOLD, color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Divider(),
                                ft.Text("1. Objetivos Gerais", size=16, weight=ft.FontWeight.W_600, color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("O objetivo geral deste trabalho prático intermédio é o desenvolvimento de um programa em Python capaz de executar conversões entre bases numéricas (2, 10 e 16), operações aritméticas de adição e subtração no sistema numérico binário e hexadecimal, multiplicação no sistema binário, e criar tabelas do códigos Gray de n bits.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Divider(),
                                ft.Text("2. Descrição do Trabalho Prático", size=16, weight=ft.FontWeight.W_600, color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("Neste trabalho prático intermédio pretende-se desenvolver uma aplicação em Python para: i) Realizar Operações de Conversão entre sistemas numéricos; e ii) Realizar operações aritméticas de adição e subtração no sistema numérico binário e hexadecimal, e de multiplicação no sistema númerico binário; e iii) Criar tabelas de Gray de n bits;", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("O programa deve implementar todas as técnicas e mecanismos discutidos nas aulas teóricas para os processos de conversão entre bases, operações aritméticas e criação das tabelas de Gray de n bits.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• Não podem ser utilizadas bibliotecas externas de apoio à construção das tabelas de Gray, conversões e/ou execução das operações aritméticas no sistema numérico binário, hexadecimal e/ou decimal. Por outras palavraa, pretende-se que implementem caso a caso os métodos/procedimentos estudados, simulando nalguns casos o comportamento do HW.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• Caso esta situação seja verificada, irá existir uma penalização na nota final do trabalho prático.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Divider(),
                                ft.Text("3. Funcionalidades Mínimas", size=16, weight=ft.FontWeight.W_600, color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("O trabalho deve implementar as seguintes funcionalidades mínimas:", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• (FM01)   Conversão entre Sistemas Numéricos: O programa deve ser capaz de converter números entre diferentes bases numéricas, como binário, decimal e hexadecimal.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• (FM02)   Operações aritméticas em diferentes bases: Implementação de operações aritméticas básicas (antes indicadas), em números representados em diferentes bases.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• (FM03)   Criação das Tabelas de Gray de n Bits: O programa deve permitir a criação de tabelas de Gray com um número especificado de bits. As tabelas devem seguir a sequência de Gray, onde cada número subsequente difere apenas num único bit.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Divider(),
                                ft.Text("4. Funcionalidades Adicionais ou Extra", size=16, weight=ft.FontWeight.W_600, color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("O trabalho pode implementar as seguintes funcionais adicionais/extra:", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• (FA01)   Menu Interativo: Adição de um menu interativo que ofereça ao utilizador uma interface intuitiva para acesso às diferentes funcionalidades do programa.\n\t\t\tNota: Nesta fase poderá ser uma interface textual.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• (FA02)   Outras: Outras a propor pelo grupo, desde que fundamentada.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Divider(),
                                ft.Text("5. Requisitos Técnicos", size=16, weight=ft.FontWeight.W_600, color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("No desenvolvimento deste projeto, deve considerar os seguintes requisitos técnicos:", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• O programa deve ser implementado em Python.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• É desejável a utilização de funções modulares para facilitar a manutenção e reutilização do código.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• O código deve ser bem documentado e conter comentários explicativos para facilitar a compreensão.", color=theme.AppColors.TEXT_COLOR_DARK),    
                                ft.Text("• Recomenda-se o uso de estruturas de controlo adequadas para garantir a eficiência e a precisão das operações.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• Recomenda-se o uso de estruturas de dados (e.g., listas) para armazenar e manipular os dados.", color=theme.AppColors.TEXT_COLOR_DARK),
                                ft.Text("• Sugere-se que para cada caso, o output possa ser do resultado final, acompanhado com a ilustração passo a passo do método/procedimento adotado. Sem prejuizo de outras em www.rapitables.com, encontra um exemplo.", color=theme.AppColors.TEXT_COLOR_DARK),    
                            ]
                        )
                    ),
                    
                    # footer - nome
                    footer(page)
                ]
            )
        ]
    )