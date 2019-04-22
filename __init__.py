from flask import Flask, render_template, request
import pygal
from pygal.style import DarkColorizedStyle, NeonStyle, CleanStyle, LightStyle, DefaultStyle
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models.sources import AjaxDataSource
from .server.myContainer import Container


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    container = Container()

    def get_graph_1():
        line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
        line_chart.title = 'CPU usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002, 2012))
        # line_chart.y_labels = map(str, range(200, 400))
        line_chart.add('CPU', [ 25, 73, 2, 5, 7, 17, 100, 33,])
        line_chart.render()
        graph_data = line_chart.render_data_uri()
        return graph_data

    def get_graph_2():
        line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=CleanStyle)
        line_chart.title = 'Memory usage evolution (in %)'
        line_chart.x_labels = map(str, range(2001, 2009))
        # line_chart.y_labels = map(str, range(100, 200))
        line_chart.add('Memory', [5, 25, 73, 2, 5, 7, 17, 100, 33, 75, 16, 13, 37, 7])
        line_chart.render()
        graph_data = line_chart.render_data_uri()
        return graph_data

    def get_graph_3():
        line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DefaultStyle)
        line_chart.title = 'Hard Disk usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002, 2018))
        # line_chart.y_labels = map(str, range(0, 100))
        line_chart.add('Hard Disk', [6, 10, 9, 7, 3, 1, 0, 1, 3, 5, 16, 13, 3, 7])
        line_chart.render()
        graph_data = line_chart.render_data_uri()
        return graph_data

    def get_graph_4():
        line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=CleanStyle)
        line_chart.title = 'Networks usage evolution (in %)'
        line_chart.x_labels = map(str, range(2000, 2010))
        # line_chart.y_labels = map(str, range(0, 100))
        line_chart.add('Networks', [2, 3, 5, 9, 12, 9, 5, 1, 3, 5, 16, 13, 3, 7])
        line_chart.render()
        graph_data = line_chart.render_data_uri()
        return graph_data

    @app.route('/')
    def index():
        graph_data1 = get_graph_1()
        graph_data2 = get_graph_2()
        graph_data3 = get_graph_3()
        graph_data4 = get_graph_4()
        return render_template('/index.html', graph_data1=graph_data1,
                               graph_data2=graph_data2, graph_data3=graph_data3,
                               graph_data4=graph_data4)

    @app.route('/login')
    def login():
        return render_template('/authentication/login.html')

    @app.route('/register')
    def register():
        return render_template('/authentication/register.html')

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
