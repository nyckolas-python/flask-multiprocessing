from flask import Flask, render_template, url_for, redirect, request
from olx_app.parser import parser
from config import Configuration

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(parser)

toolbar = DebugToolbarExtension(app)


if __name__ == '__main__':
    app.run()