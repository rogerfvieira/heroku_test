from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def form():
        return 'hello world'
    return app
