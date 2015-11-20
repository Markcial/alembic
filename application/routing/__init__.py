from flask import Blueprint, render_template
from application.services.docker import get_mysql_boxes, inspect
from application.views import sidebar, footer

router = Blueprint(
    'base',
    __name__
)


@router.route('/')
def index():
    boxes = get_mysql_boxes()
    return render_template('pages/index.html', boxes=boxes, sidebar=sidebar, footer=footer)


@router.route('/snapshots')
def snapshots():
    return 'list snapshots'