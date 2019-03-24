from flask import Blueprint, flash, g, redirect, render_template, session, url_for
from flask import request

from .server.myContainer import Container

containerObj = Container()

con_bp = Blueprint('container', __name__, url_prefix='/container')


@con_bp.route('/')
def containers():
    return render_template('containers/container.html', containers=containerObj)


# container buttons functions
@con_bp.route("/", methods=('GET', 'POST'))
def start_containers():
    if request.method == "GET":
        return render_template("container.html")
    elif request.method == "POST":
        if request.form['my_btn'] == 'start':
            con_ids = request.form.getlist('container')
            for i in con_ids:
                containerObj.startContainer(i)
        elif request.form['my_btn'] == 'stop':
            con_ids = request.form.getlist('container')
            for i in con_ids:
                containerObj.stopContainer(i)
        elif request.form['my_btn'] == 'remove':
            con_ids = request.form.getlist('container')
            print(con_ids)
            for i in con_ids:
                containerObj.removeContainer(i)
        elif request.form['my_btn'] == 'pause':
            con_ids = request.form.getlist('container')
            print(con_ids)
            for i in con_ids:
                containerObj.pauseContainer(i)
        elif request.form['my_btn'] == 'resume':
            con_ids = request.form.getlist('container')
            print(con_ids)
            for i in con_ids:
                containerObj.unpauseContainer(i)
        elif request.form['my_btn'] == 'kill':
            con_ids = request.form.getlist('container')
            print(con_ids)
            for i in con_ids:
                containerObj.killContainer(i)
        elif request.form['my_btn'] == 'restart':
            con_ids = request.form.getlist('container')
            print(con_ids)
            for i in con_ids:
                containerObj.restartContainer(i)

        return render_template("containers/container.html", containers=containerObj)


@con_bp.route('/<con_id>')
def get_container_by_id(con_id):
    inspect = containerObj.inspectContainer(con_id)
    log = containerObj.logprint(con_id)
    container_status = containerObj.container_status(con_id)
    return render_template('containers/container_id.html', container_inspect=inspect, container_log=log,
                           container_status=container_status)
