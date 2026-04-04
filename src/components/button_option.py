import flet as ft
from src.themes import colors as theme

def button_option(icon_path, label, on_click=None):
    
    def on_hover(e):
        e.control.bgcolor = (
            theme.AppColors.BTN_BACKGROUND_HOVER if e.data == True
            else theme.AppColors.BTN_BACKGROUND_DARK
        )
        e.control.shadow = (
            ft.BoxShadow(
                spread_radius=1,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.4, "#ffffff"),
                offset=ft.Offset(0, 0),
            )
            if e.data
            else ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.6, "#000000"),
                offset=ft.Offset(0, 4),
            )
        )
        e.control.update()

    return ft.Container(
        col={"xs": 6, "sm": 4, "md": 3},
        padding=10,
        on_click=on_click,
        content=ft.Container(
            bgcolor=theme.AppColors.BTN_BACKGROUND_DARK,
            border_radius=15,
            height=150,
            padding=20,
            alignment=ft.Alignment(0, 0),
            on_hover=on_hover, 
            animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT), 
            border=ft.border.all(2, theme.AppColors.BTN_STROKE_DARK),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.6, "#000000"),
                offset=ft.Offset(0, 4),
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(src=icon_path, width=60, height=60),
                    ft.Text(value=label, color=theme.AppColors.BTN_TEXT_DARK, weight=ft.FontWeight.W_600),
                ]
            )
        )
    )