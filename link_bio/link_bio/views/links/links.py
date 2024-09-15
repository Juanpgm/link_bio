import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.styles.styles as styles

def links() -> rx.Component:
    return rx.vstack(
        
        
        title('Redes Sociales'),
        link_button('LinkedIn', 
                    'Sígueme en LinkedIn', 
                    'https://www.linkedin.com/in/jp-guzman/'),
        
        link_button('GitHub', 
                    'Sígueme en GitHub', 
                    'https://www.github.com/'),
                
        link_button('Youtube', 
                    'Subscríbete al canal', 
                    'https://www.youtube.com/@juanpablomartinez4105'),
        
        link_button('Discord',
                    'Este es mi servidor de Discord',
                    'https://www.youtube.com/@juanpablomartinez4105'),
        
        link_button('Intagram', 
                    '@juanp_ax', 
                    'https://www.instagram.com/juanp_ax?igsh=bDhua3JvcDR1d3I3'),
        
        link_button('Threads', 
                    '@juanp_ax', 
                    'https://www.instagram.com/'),
        
        width='100%',
        max_width=styles.MAX_WIDTH,
    ),
    
                
 

