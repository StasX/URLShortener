from flask import Blueprint, request, render_template, session, redirect, jsonify, Response
import requests
from random import choice
from string import ascii_letters, digits
from models.url_model import UrlModel
from models.user_model import UserModel
from mongoengine import DoesNotExist


pages_blueprint = Blueprint("pages_view", __name__)


@pages_blueprint.route("/")
@pages_blueprint.route("/home")
def home():
    return render_template("home.html")


@pages_blueprint.route("/geturl", methods=["POST"])
def get_url():
    url = request.form.get("url")
    response = requests.get(url, allow_redirects=False)
    if response.is_redirect or response.status_code == 302:
        url = response.headers['Location']
    return jsonify({"url": url})


@pages_blueprint.route("/short", methods=["POST"])
def short_it():
    user_id = session["current_user"]["id"]
    user_model = UserModel.objects.get(id=user_id)
    full_url = request.form.get("url")
    chars = ascii_letters+digits
    short_url = None
    run_again = True
    while run_again:
        short_string = ''.join(choice(chars) for _ in range(6))
        short_url = f"http://{request.host}/{short_string}"
        if (len(UrlModel.objects(short_url=short_url)) == 0):
            url_model = UrlModel(short_url=short_url,
                                 full_url=full_url, user=user_model).save()
            run_again = False
    return jsonify({"url": short_url})


@pages_blueprint.route("/<url_part>")
def redirect_to(url_part):
    try:
        if url_part != "favicon.ico":
            short_url = f"http://{request.host}/{url_part}"
            url_model = UrlModel.objects.get(short_url=short_url)
            return redirect(url_model.full_url)
        return Response(status=200)
    except DoesNotExist:
        return render_template("404.html")
