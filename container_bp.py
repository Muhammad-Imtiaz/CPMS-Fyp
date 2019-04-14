from flask import Blueprint, flash, g, redirect, render_template, session, url_for
from flask import request
import pygal
from pygal.style import DarkColorizedStyle, NeonStyle, CleanStyle, LightStyle, DefaultStyle

from .server.myContainer import Container
from .server.myImage import Image

containerObj = Container()
imageObj = Image()

con_bp = Blueprint('container', __name__, url_prefix='/container')


@con_bp.route('/')
def containers():
    graph_data1 = get_graph_1()
    graph_data2 = get_graph_2()
    graph_data3 = get_graph_3()
    graph_data4 = get_graph_4()

    return render_template('containers/container.html', containers=containerObj, graph_data1=graph_data1,
                           graph_data2=graph_data2, graph_data3=graph_data3,
                           graph_data4=graph_data4)


def get_graph_1():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
    line_chart.title = 'CPU usage evolution (in %)'
    # line_chart.x_labels = map(str, range(0, 100))
    line_chart.y_labels = map(str, range(200, 400))
    line_chart.add('CPU', [1, 3, 5, 16, 13, 3, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


def get_graph_2():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
    line_chart.title = 'Memory usage evolution (in %)'
    # line_chart.x_labels = map(str, range(0, 100))
    line_chart.y_labels = map(str, range(100, 200))
    line_chart.add('Memory', [5, 25, 73, 2, 5, 7, 17, 100, 33, 75, 16, 13, 37, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


def get_graph_3():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
    line_chart.title = 'Hard Disk usage evolution (in %)'
    line_chart.x_labels = map(str, range(0, 100))
    line_chart.y_labels = map(str, range(0, 100))
    line_chart.add('Hard Disk', [6, 10, 9, 7, 3, 1, 0, 1, 3, 5, 16, 13, 3, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


def get_graph_4():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
    line_chart.title = 'Networks usage evolution (in %)'
    line_chart.x_labels = map(str, range(0, 100))
    line_chart.y_labels = map(str, range(0, 100))
    line_chart.add('Networks', [2, 3, 5, 9, 12, 9, 5, 1, 3, 5, 16, 13, 3, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


# container buttons functions
@con_bp.route("/", methods=('GET', 'POST'))
def start_containers():
    graph_data1 = get_graph_1()
    graph_data2 = get_graph_2()
    graph_data3 = get_graph_3()
    graph_data4 = get_graph_4()

    if request.method == "GET":
        return render_template("containers/container.html", containers=containerObj, )
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
        elif request.form['my_btn'] == 'add':
            images = imageObj.listAllImages()
            return render_template('containers/add_container.html', images=images)

        return render_template("containers/container.html", containers=containerObj, graph_data1=graph_data1,
                               graph_data2=graph_data2, graph_data3=graph_data3,
                               graph_data4=graph_data4)


@con_bp.route('/<con_id>')
def get_container_by_id(con_id):
    inspect = containerObj.inspectContainer(con_id)
    log = containerObj.logprint(con_id)
    container_status = containerObj.container_status(con_id)
    return render_template('containers/container_id.html', container_inspect=inspect, container_log=log,
                           container_status=container_status)
