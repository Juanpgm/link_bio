import reflex as rx
from enum import Enum

#Constants
MAX_WIDTH='600px'


#Sizes
class Size(Enum):
    SMALL='0.5em',
    MEDIUM='0.8em'
    DEFAULT='1em'
    BIG='1.5em'
    EXTRA_BIG='2em'
    
    
#Styles

BASE_STYLE={
    rx.button:{
        'width':'100%',
        'height':'100%',
        'display':'block',
        'padding':Size.SMALL.value,
        'border_radius': Size.DEFAULT.value
    },
    
    rx.link:{
        'text_decoration':'none',
        '_hover': {},
        'as_child': True
    },
    
    rx.center:{
        'align': 'center',
        'justify': 'center'
    }
    
}


#Estilos propios

title_style = dict(
    width='100%',
    size='md',
    padding_top=Size.DEFAULT.value,
    
)

button_title_style = dict(
    is_external=True,
    font_size=Size.BIG.value
)


button_body_style = dict(
    font_size=Size.MEDIUM.value
)
