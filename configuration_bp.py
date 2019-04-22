from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.myConfiguration import Configuration

configurationObj = Configuration()

configuration_bp = Blueprint('configuration', __name__, url_prefix='/configurations')

@configuration_bp.route('/')
def services():
    return render_template('/configurations/configurations.html')




