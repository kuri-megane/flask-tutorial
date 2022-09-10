from flask import Flask

from add.views import ok_module
from update.views import ng_module

app = Flask(__name__)

app.register_blueprint(ok_module)
app.register_blueprint(ng_module)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(port=5000)
