from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.myService import Service

serviceObj = Service()

service_bp = Blueprint('service', __name__, url_prefix='/services')

@service_bp.route('/')
def services():
    return render_template('/services/services.html')




