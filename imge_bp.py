from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect
import pygal
import os
from werkzeug.utils import secure_filename

from .server.myImage import Image
from .__init__ import create_app

imageObj = Image()

img_bp = Blueprint('image', __name__, url_prefix='/images')

app = create_app()

UPLOAD_FOLDER = '/home/imtiaz/Documents/FYP/FinalYearProject'
ALLOWED_EXTENSIONS = set(['tar', 'yml'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

        elif request.form['my_btn'] == 'push':
            all_images = request.form.getlist('image')

            imageObj.pushImage(all_images)

    return render_template("images/image.html", images=imageObj)


@img_bp.route('/build/')
def build_new_image():
    return render_template('/images/build_new_image.html')


@img_bp.route('/build/', methods=('GET', 'POST'))
def build():
    if request.method == 'POST':
        if request.form['build_image'] == 'build':
            image_tag = request.form.get('image_tag')
            print('image tag goes here...')
            print(image_tag)
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(os.path.realpath(UPLOAD_FOLDER))
            imageObj.buildImage(os.path.realpath(os.path.realpath(UPLOAD_FOLDER)), tag=image_tag)

    return redirect(url_for('image.images'))
