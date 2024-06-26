from flask import Blueprint, request, render_template, session, redirect, jsonify
import requests
home_blueprint = Blueprint("home_view", __name__)


@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    return render_template("home.html")


@home_blueprint.route("/geturl", methods=["POST"])
def get_url():
    url = request.form.get("url")
    response = requests.get(url, allow_redirects=False)
    if response.is_redirect or response.status_code == 302:
        url = response.headers['Location']
    return jsonify({"url": url})
