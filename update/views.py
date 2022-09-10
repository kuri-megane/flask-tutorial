from flask import Blueprint

ng_module = Blueprint("ng", __name__)


@ng_module.route("/get/ng", methods=["GET"])
def get_ng():
    return "NG"
