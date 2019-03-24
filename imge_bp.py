from flask import Flask, render_template, url_for, Blueprint

from .server.myImage import Image
imageObj = Image()


img_bp = Blueprint('image', __name__, url_prefix='/images')

@img_bp.route('/')
def images():
    render_template('/images/image.html', images=imageObj)
