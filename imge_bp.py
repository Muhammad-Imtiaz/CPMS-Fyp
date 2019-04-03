from flask import Flask, render_template, url_for, Blueprint, request
import pygal

from .server.myImage import Image
imageObj = Image()


img_bp = Blueprint('image', __name__, url_prefix='/images')

@img_bp.route('/')
def images():
    return render_template('/images/image.html', images=imageObj)

@img_bp.route('/<image_id>')
def get_image_by_id(image_id):
    get_details = imageObj.image_detail(image_id)
    return render_template('/images/image_id.html', image_details=get_details)

@img_bp.route('/', methods=('GET', 'POST'))
def remove_img():
    if request.method == "GET":
        return render_template("image.html")
    elif request.method == 'POST':
        if request.form['my_btn'] == 'remove':
            all_images = request.form.getlist('image')
            for i in all_images:
                imageObj.removeImage(i, True)
        elif request.form['my_btn'] == 'build':
            return render_template('/images/build_new_image.html')
    return render_template("images/image.html", images=imageObj)


def build_new_image():
    return render_template('/images/build_new_image.html')

