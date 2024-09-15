import reflex as rx
from link_bio.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.icon(
              tag='square-dashed-mouse-pointer'  
            ),
        rx.text(
            '{Juan_Guzmán}',
            height='15px'
        ),
        position='sticky',
        bg = '#FA5858',
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        z_index='999',
        top='0'
    )