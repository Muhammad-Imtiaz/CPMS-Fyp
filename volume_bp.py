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


@vol_bp.route('/<volumeID>')
def get_volume_by_id(volumeID):
    inspect_vol = volumeObj.inspect_volume(volumeID)
    return render_template('/volumes/volume_id.html', inspect_vol=inspect_vol)
