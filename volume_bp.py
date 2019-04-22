from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.myVolume import Volume

vol_bp = Blueprint('volume', __name__, url_prefix='/volumes')

volumeObj = Volume()


@vol_bp.route('/')
def list_all_volumes():
    volumes = volumeObj.list_all_volumes()
    return render_template('/volumes/volume.html', volumes=volumes)

@vol_bp.route('/add_volume')
def add_volume():
    return render_template('/volumes/add_volume.html')
