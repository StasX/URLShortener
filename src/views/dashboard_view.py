from flask import Blueprint, request, render_template, session, redirect, jsonify, Response
import requests
from models.url_model import UrlModel
from models.user_model import UserModel
from mongoengine import DoesNotExist


dashboard_blueprint = Blueprint("dashboard_view", __name__)


@dashboard_blueprint.route("/dashboard")
def render():
    return render_template("dashboard.html")
