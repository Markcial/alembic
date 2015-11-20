from flask import Blueprint

router = Blueprint(
    'pages',
    __name__
)

@router.route('/')
def index():
    return 'indice de la seccion de paginas'