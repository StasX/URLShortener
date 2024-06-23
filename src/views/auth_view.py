from flask import Blueprint, request, render_template, session, redirect, url_for
from models.user_model import UserModel
from utils.security import Security


auth_blueprint = Blueprint("auth_view", __name__)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    # get html
    if request.method == "GET":
        return render_template("login.html")
    # login
    try:
        email = request.form["username"]
        password = request.form["password"]
        user = UserModel.objects.get(
            {"email": email, "password": Security.hash(password)})
        if user:
            session["current_user"] = user
            redirect(url_for("home_view.home"))
    except Exception as err:
        print(err)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    # get html
    if request.method == "GET":
        return render_template("register.html")
    # login
    try:
        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        password = request.form.get("password")
        UserModel(first_name=first_name, last_name=last_name,
                  email=email, password=Security.hash(password)).save()
        user= UserModel.objects.get(email=email)
        if user:
            session["current_user"] = user
            redirect(url_for("home_view.home"))
    except Exception as err:
        print(err)


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    session.clear()
    # return to home page
