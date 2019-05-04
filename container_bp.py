from flask import Blueprint, flash, g, redirect, render_template, session, url_for
from flask import request
from flask import jsonify
import pygal
from pygal.style import DarkColorizedStyle, NeonStyle, CleanStyle, LightStyle, DefaultStyle

from .server.myContainer import Container
from .server.myImage import Image
from .server.myVolume import Volume

containerObj = Container()
imageObj = Image()
volumeObj = Volume()

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


@con_bp.route('/cpu', methods=('GET', 'POST'))
def get_cpu():
    return jsonify(cpu=containerObj.calculate_cpu_percent('15ec352cd1e1'))


@con_bp.route('/test')
def getCPU():
    return render_template('test.html')


def get_graph_1():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
    line_chart.title = 'CPU usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2012))
    # line_chart.y_labels = map(str, range(200, 400))
    line_chart.add('CPU', [1, 3, 5, 16, 13, 3, 7, 1, 3, 5, 16, 13, 3, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


def get_graph_2():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=CleanStyle)
    line_chart.title = 'Memory usage evolution (in %)'
    line_chart.x_labels = map(str, range(0, 100))
    line_chart.y_labels = map(str, range(100, 200))
    line_chart.add('Memory', [5, 25, 73, 2, 5, 7, 17, 100, 33, 75, 16, 13, 37, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


def get_graph_3():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)
    line_chart.title = 'Hard Disk usage evolution (in %)'
    line_chart.x_labels = map(str, range(0, 100))
    # line_chart.y_labels = map(str, range(0, 100))
    line_chart.add('Hard Disk', [6, 10, 9, 7, 3, 1, 0, 1, 3, 5, 16, 13, 3, 7])
    line_chart.render()
    graph_data = line_chart.render_data_uri()
    return graph_data


def get_graph_4():
    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DarkColorizedStyle)
    line_chart.title = 'Networks usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2012))
    # line_chart.y_labels = map(str, range(0, 100))
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

        return render_template("containers/container.html", containers=containerObj, graph_data1=graph_data1,
                               graph_data2=graph_data2, graph_data3=graph_data3,
                               graph_data4=graph_data4)


@con_bp.route('/add_container/')
def add_container():
    images = imageObj.listAllImages()
    volumes = volumeObj.list_all_volumes()
    return render_template('containers/add_container.html', images=images, volumes=volumes)


@con_bp.route("/add_container/", methods=('GET', 'POST'))
def deploy_container():
    images = imageObj.listAllImages()
    if request.method == "POST":
        if request.form['deploy'] == 'deploy_container':
            con_name = request.form.get('container_name')
            image_name = request.form.get('selected_image')  # still not working
            print(image_name)

            # Ports
            con_port = request.form.get('container_port')
            host_port = request.form.get('host_port')
            ports = {con_port + '/tcp': host_port}

            # commands and logging
            command = request.form.get('command')
            entry = request.form.get('entry')
            workingdir = request.form.get('working')
            user = request.form.get('user')
            console = request.form.get('console')
            print('tty gonna be bool ' + console)

            # volumes
            con_vol = request.form.get('volume_c')
            vol = request.form.get('selected_volume')
            print(vol)
            volumes = {vol: {'bind': con_vol, 'mode': 'rw'}}
            # networks
            network = request.form.get('network_dropdown')  # will get item from list...still not working
            print(network)
            net_host = request.form.get('network_host')
            net_domain = request.form.get('network_domain')
            net_mac = request.form.get('network_mac')

            # ENV
            env1 = request.form.get('env_1')
            env2 = request.form.get('env_2')
            env3 = request.form.get('env_3')
            env4 = request.form.get('env_4')
            environment = [str(env1) + "=" + str(env2), str(env3) + "=" + str(env4)]

            # labels
            lable1 = request.form.get('lable1')
            lable2 = request.form.get('lable2')
            lable3 = request.form.get('lable3')
            lable4 = request.form.get('lable4')
            labels = {lable1.upper(): lable2, lable3.upper(): lable4}

            # Restart policy
            restart = request.form.get('restart_btn')
            restart_policy = {'Name': restart}

            # Resources allocation
            memory_limit = request.form.get('memory_limit')
            cpuset_cpus = request.form.get('cpu_limit')
            #
            output = containerObj.deployContainer(name=con_name, image=image_name,
                                                  hostname=net_host, user=user,
                                                  ports=ports, environment=environment, volume=volumes,
                                                  entrypoint=entry, working_dir=workingdir, domainname=net_domain,
                                                  network=network, mac_address=net_mac, labels=labels,
                                                  restart_policy=restart_policy,
                                                  cpu_limit=cpuset_cpus, memory_limit=memory_limit)
            #
            # flash(output)
        return redirect(url_for('container.containers'))


@con_bp.route('/<con_id>')
def get_container_by_id(con_id):
    inspect = containerObj.inspectContainer(con_id)
    log = containerObj.logprint(con_id)
    container_status = containerObj.container_status(con_id)
    return render_template('containers/container_id.html', container_inspect=inspect, container_log=log,
                           container_status=container_status)
