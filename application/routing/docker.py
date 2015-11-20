from flask import Blueprint, Response, redirect, url_for, render_template

from application.services.docker import get_mysql_boxes, inspect, Container
from ..services import docker
from requests.exceptions import ConnectionError
from ..services import create_snapshot_directory

router = Blueprint(
    'docker',
    __name__
)


@router.route('/status')
def status():
    """
    gets the docker daemon status via http
    :return:
    """
    response = Response()
    try:
        docker.version()
        response.status_code = 200
    except ConnectionError:
        response.status_code = 410
    return response


@router.route('/mysql/list')
def mysql_list():
    boxes = docker.get_mysql_boxes()
    return boxes

@router.route('/mysql/new')
def mysql_new():
    box = docker.new_mysql_box()
    #return redirect()
#    container = run('mysql', args={'e' : 'MYSQL_ROOT_PASSWORD=admin'})
    return redirect(url_for('docker.settings', name=box))


@router.route('/settings/<name>')
def settings(name):
    boxes = get_mysql_boxes()
    container = Container(name)
    return render_template('docker/config.html', selected_box=container, boxes=boxes)