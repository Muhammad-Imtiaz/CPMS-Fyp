import docker
from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.myNetwork import Network

networkObj = Network()

net_bp = Blueprint('network', __name__, url_prefix='/networks')


@net_bp.route('/')
def networks():
    list = networkObj.list_all_networks()
    return render_template('/networks/networks.html', list=list)


@net_bp.route('/', methods=['GET', 'POST'])
def network_operations():
    if request.method == "POST":
        if request.form['my_btn'] == 'remove':
            net_ids = request.form.getlist('network')
            for i in net_ids:
                networkObj.remove_network(i)
    return redirect(url_for('network.networks'))


@net_bp.route('/add_network/')
def add_network():
    return render_template('/networks/add_network.html')


@net_bp.route('/add_network/', methods=['GET', 'POST'])
def add_more_network():
    output = None
    if request.method == "POST":
        if request.form['deploy'] == 'deploy_network':
            name = request.form.get('network_name')
            driver = request.form.get('network_dropdown')
            subnet = request.form.get('subnet')
            gateway = request.form.get('gateway')
            iprange = request.form.get('ip_range')
            exIP = request.form.get('ex_ips')
            print(subnet, gateway, iprange, exIP)
            if subnet != '' and gateway != '':
                ipam_pool = docker.types.IPAMPool(
                    subnet=subnet,
                    gateway=gateway
                )
                ipam_config = docker.types.IPAMConfig(
                    driver=driver,
                    pool_configs=[ipam_pool])
                print(ipam_config)
                try:
                    output = networkObj.create_network(name, driver, ipam_config)
                    print(output)
                except:
                    flash(output)
                    return render_template('/networks/add_network.html')
            else:
                try:
                    output = networkObj.create_network(name, driver)
                    print(output)
                except:
                    flash(output)
                    return render_template('/networks/add_network.html')
    return redirect(url_for('network.networks'))


@net_bp.route('/<net_id>')
def get_network_by_id(net_id):
    inspect = networkObj.get_network_by_id(net_id)
    return render_template('networks/network_id.html', inspect=inspect)
