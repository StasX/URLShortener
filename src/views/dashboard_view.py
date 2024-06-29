from flask import Blueprint, request, render_template, session, redirect, jsonify, Response
import requests
from models.url_model import UrlModel
from models.user_model import UserModel
from mongoengine import DoesNotExist
from random import randint


dashboard_blueprint = Blueprint("dashboard_view", __name__)


@dashboard_blueprint.route("/dashboard")
def render():
    user = session["current_user"]
    urls_models=UrlModel.objects(user=user["id"])
    colors=[]
    for i in range(len(urls_models)):
        colors.append([randint(0,255),randint(0,255),randint(0,255)])
    return render_template("dashboard.html",urls_data=urls_models,colors=colors)
