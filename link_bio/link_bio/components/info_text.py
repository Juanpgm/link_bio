import reflex as rx
from link_bio.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(title, style=dict(font_weight="bold", color="red")),
        rx.text(body, style=dict(font_size=Size.DEFAULT.value)),
        )