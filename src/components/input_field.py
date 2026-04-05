import flet as ft
from src.themes import colors as theme

# text input para as conversoes das bases

def input_field(field_id: str, label: str, hint: str, on_change=None):
    
    field = ft.TextField(
        data=field_id,
        label=label,
        height=45,
        width=600,
        hint_text=hint,
        on_change=on_change,
        bgcolor="transparent",
        border_color=theme.AppColors.INPUT_FIELD_BORDER,
        focused_border_color=theme.AppColors.INPUT_FIELD_BORDER_FOCUS,
        border_radius=10,
        border_width=1,
        text_style=ft.TextStyle(color=theme.AppColors.TEXT_COLOR_DARK),
        label_style=ft.TextStyle(
            color=ft.Colors.with_opacity(0.7, theme.AppColors.TEXT_COLOR_DARK),
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.with_opacity(0.7, theme.AppColors.TEXT_COLOR_DARK),
        ),
    )
    
    return field