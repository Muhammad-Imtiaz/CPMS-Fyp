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
    if request.method == 'POST':
        if request.form['my_btn'] == 'pull_image':
            image_name = request.form.get('image_name')
            imageObj.pullImage(image_name)

        elif request.form['my_btn'] == 'remove':
            all_images = request.form.getlist('image')
            for i in all_images:
                imageObj.removeImage(i, True)
        elif request.form['my_btn'] == 'export':
            all_images = request.form.getlist('image')
            imageObj.exportImage(all_images)

    return render_template("images/image.html", images=imageObj)


@img_bp.route('/build/')
def build_new_image():
    return render_template('/images/build_new_image.html')




@img_bp.route('/import/')
def import_image():
    return render_template('/images/import_image.html')
