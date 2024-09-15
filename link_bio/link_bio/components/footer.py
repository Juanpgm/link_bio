import reflex as rx
import datetime
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    # Use rx.hstack to arrange elements horizontally
    return rx.box(
        rx.hstack(
            # rx.center each element individually for better control
            rx.center(
                rx.avatar(name="Darth Pablo", 
                    fallback="JP", 
                    size="9",
                    align='center'),
            ),
            rx.spacer(size=10),  # Add vertical spacing between image and text
            rx.center(
                rx.vstack(
                    rx.link(
                        f'(CC) 2010 - {datetime.date.today().year} JUAN PABLO GUZMÁN MARTÍNEZ',
                        href='https://www.linkedin.com/in/jp-guzman/',
                        is_external=True,
                        font_size=Size.MEDIUM.value
                    ),
                    rx.text(
                        'BUILDING SOFTWARE WITH ♥ FROM IBAGUÉ- TOLIMA - COLOMBIA TO THE WORLD',
                            font_size=Size.MEDIUM.value,
                            margin_top='0px !important'
                            ),
                    
                )
            ),
            margin_bottom=Size.EXTRA_BIG.value
        ),
        # Optional: center the entire footer horizontally if needed
        margin='0 auto', 
        max_width=styles.MAX_WIDTH,
        width='100%'
    )