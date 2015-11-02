from flask import Blueprint

router = Blueprint(
    'front_router',
    __name__,
    template_folder='templates'
)

@router.route('/')
def index():
    return 'index'

@router.route('/about')
def about():
    return 'about'