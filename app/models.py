from datetime import datetime

from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_publication = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    text = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    date_parsing = db.Column(db.DateTime(timezone=True), default=datetime.now)


class ExceptionLoad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    traceback = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    date_parsing = db.Column(db.DateTime(timezone=True), default=datetime.now)
