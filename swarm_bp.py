from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.mySwarm import Swarm

swarmObj = Swarm()

swarm_bp = Blueprint('swarm', __name__, url_prefix='/swarms')

@swarm_bp.route('/')
def swarm():
    return render_template('/swarm/swarm.html')




