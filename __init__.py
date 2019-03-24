from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    from .container_bp import con_bp
    from .imge_bp import img_bp

    app.register_blueprint(con_bp)

    app.register_blueprint(img_bp)

    app.debug=True
    return app
