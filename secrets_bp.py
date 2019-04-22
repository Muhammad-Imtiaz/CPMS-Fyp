from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.mySecrets import Secrets

secretObj = Secrets()

secret_bp = Blueprint('secrets', __name__, url_prefix='/secrets')

@secret_bp.route('/')
def secrets():
    return render_template('/secrets/secrets.html')




