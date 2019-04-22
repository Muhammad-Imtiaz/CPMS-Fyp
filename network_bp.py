from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.myNetwork import Network

networkObj = Network()

net_bp = Blueprint('network', __name__, url_prefix='/networks')


@net_bp.route('/')
def networks():
    list = networkObj.list_all_networks()
    return render_template('/networks/networks.html', list=list)

@net_bp.route('/add_network/')
def add_network():
    return render_template('/networks/add_network.html')
