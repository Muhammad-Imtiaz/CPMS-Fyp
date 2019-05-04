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


@net_bp.route('/<net_id>')
def get_network_by_id(net_id):
    inspect = networkObj.get_network_by_id(net_id)
    return render_template('networks/network_id.html', inspect=inspect)
