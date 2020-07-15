from flask import Blueprint,render_template,request

index = Blueprint("index",__name__)


@index.route("/")
def indexMain():
    return render_template("index.html")


