from flask import Flask, render_template, request, redirect, url_for, flash
from bokeh.models.sources import AjaxDataSource
from .server.myContainer import Container


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    container = Container()

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/home')
    def home():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('/authentication/login.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login_user():
        if request.method == "POST":
            if request.form['login'] == 'login':
                username = request.form.get('username')
                pasword = request.form.get('password')
                if username == 'admin' and pasword == 'admin':
                    return redirect(url_for('home'))
        return render_template('/authentication/login.html')

    @app.route('/register')
    def register():
        return render_template('/authentication/register.html')

    @app.route('/register', methods=['GET', 'POST'])
    def registeration():
        if request.method == "POST":
            if request.form['signup'] == 'signup':
                username = request.form.get('username')
                email = request.form.get('email')
                password = request.form.get('pass1')
                re_password = request.form.get('pass2')
                if password != re_password:
                    print('password does not match..')
                    return render_template('/authentication/register.html')
                else:
                    write_to_file(username, email, password)
        return redirect(url_for('home'))

    @app.route('/test')
    def test():
        return render_template('/test.html')

    def write_to_file(username, email, pass1):
        registeration_file = open('register.txt', 'a')
        registeration_file.write(username + '\n')
        registeration_file.write(pass1 + '\n')
        registeration_file.write(email + '\n')
        registeration_file.write('\n')
        registeration_file.close()

    def read_from_file(username, password):
        return True

    from .container_bp import con_bp
    from .imge_bp import img_bp
    from .volume_bp import vol_bp
    from .network_bp import net_bp
    from .service_bp import service_bp
    from .configuration_bp import configuration_bp
    from .secrets_bp import secret_bp
    from .system_bp import system_bp
    from .swarm_bp import swarm_bp

    app.register_blueprint(con_bp)
    app.register_blueprint(img_bp)
    app.register_blueprint(vol_bp)
    app.register_blueprint(net_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(configuration_bp)
    app.register_blueprint(secret_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(swarm_bp)

    app.debug = True
    return app
