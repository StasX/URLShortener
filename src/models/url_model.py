from mongoengine import Document, StringField, ReferenceField
from .user_model import UserModel


class UrlModel(Document):
    short_url = StringField(required=True)
    full_url = StringField(required=True)
    user = ReferenceField(UserModel, required=True)
