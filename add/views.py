from flask import Blueprint

ok_module = Blueprint("ok", __name__)


@ok_module.route("/get/ok", methods=["GET"])
def get_ok():
    return "OK"
