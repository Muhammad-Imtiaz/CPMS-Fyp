from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    from .container_blueprint import bp

    app.register_blueprint(bp)

    app.debug=True
    return app
