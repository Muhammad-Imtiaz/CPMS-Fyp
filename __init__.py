from flask import Flask


def create_app():

    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'hello, world!'


    from .container_blueprint import bp

    app.register_blueprint(bp)

    app.debug=True
    return app
