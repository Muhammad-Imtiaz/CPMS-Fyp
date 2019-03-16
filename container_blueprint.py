from flask import Blueprint, flash, g, redirect, render_template, session, url_for
from flask import request

from .server.myContainer import Container

containerObj = Container()

bp = Blueprint('process', __name__, url_prefix='/container')


@bp.route('/')
def containers():
    return render_template('containers/container.html', containers=containerObj)


# container buttons functions
@bp.route("/", methods=('GET', 'POST'))
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

@bp.route('/')
def get_attr(id):
    return id