from kaa.model import Customer
from flask import Blueprint

router = Blueprint(
    'front_router',
    __name__,
    template_folder='templates'
)

@router.route('/')
def index():
    c = Customer()
    c.name = 'Agustin'
    c.email = 'agustin@ulabox.com'
    c.save()

    return 'index' + c.uuid

@router.route('/about')
def about():
    return 'about'
