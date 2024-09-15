import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        
                rx.hstack(
                    
                    rx.image(
                    src="/jp_img.png",
                    width="150px",
                    height="auto",
                    align='center',
                    border_radius="25px 25px",
                    border="5px solid #555",
                ),
                    
                    rx.vstack(
                        rx.heading('JUAN PABLO GUZMÁN MARTÍNEZ',size='lg'),
                        rx.text('Ingeniero Civil || Fullstack AI Engineer'),
                        rx.text(
                            '@juanp_ax',
                            margin_top='0px !important'
                            ),
                        rx.hstack(
                            link_icon('https://www.threads.net/@juanp_ax?xmt=AQGziYdUq76nJy2JxlP9hGG2GgtDJBPo0P-QoxOgagRAvgQ'),
                            link_icon('https://www.threads.net/@juanp_ax?xmt=AQGziYdUq76nJy2JxlP9hGG2GgtDJBPo0P-QoxOgagRAvgQ'),
                            link_icon('https://www.threads.net/@juanp_ax?xmt=AQGziYdUq76nJy2JxlP9hGG2GgtDJBPo0P-QoxOgagRAvgQ'),
                        ),
                        
                        align_items='start',
                                                
                    )
                    
                ),
                
                rx.flex(
                    info_text('+8', 'Años de experiencia'),
                    rx.spacer(),
                    info_text('+2', 'Esquemas de ordenamiento territorial'),
                    rx.spacer(),
                    info_text('+4', 'Proyectos de consultoría de escala nacional'),
                    rx.spacer(),
                    width='100%',
                    ),
                
                
                rx.text('''Soy Ingeniero civil y Especialista en Inteligencia Artificial, poseo más de 8 años de experiencia
                                Actualmente estoy posicionado como Ingeniero Experto en Building Information Modeling y tengo basta
                                experiencia en proyectos de infraestructura a nivel de consultoría, diseños y formulación de proyectos,
                                además soy investigador Jr en materia de Inteligencia Artificial aplicada a sistemas embebidos, Internet de las cosas,
                                y Gestión del riesgo, emergencias y desastres.'''),
                spacing=Size.EXTRA_BIG.value,
                align_items='start',
                max_width=styles.MAX_WIDTH,
                width='100%'
    )

