import os

from waitress import serve

from app import app, db

def find_or_create_database():
    for file in os.listdir("./"):
        if file.endswith(".db"):
            return
    db.create_all()


if __name__ == '__main__':
    find_or_create_database()
    serve(app, host="0.0.0.0", port=9000)
