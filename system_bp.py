from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
from .server.mySystem import System

systemObj = System()

system_bp = Blueprint('system', __name__, url_prefix='/systems')

@system_bp.route('/')
def services():
    return render_template('/system/system.html')




