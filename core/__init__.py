from flask import Flask

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fasldfovhlsdgbfovonssdhflavhocnlvisd'

    from .views import views

    app.register_blueprint(views)

    return app

def run_test():

    from .tests import do_tests

    do_tests()