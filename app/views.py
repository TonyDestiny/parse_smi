from datetime import datetime, timedelta

from flask import jsonify

from app import app, db, models


def format_data(data):
    return {
        'id': data.id,
        'date_publication': data.date_publication,
        'title': data.title,
        'text': data.text,
        'url': data.url
    }


def get_news_from_db(days):
    now = datetime.now()
    n_days_ego = (now - timedelta(days=days)).strftime('%Y-%m-%d')
    result = db.session \
        .query(models.News) \
        .filter(models.News.date_publication > n_days_ego) \
        .filter(models.News.date_publication <= now).all()
    list_news = []
    for n in result:
        list_news.append(format_data(n))
    return list_news


@app.route('/metro/news=<days>', methods=['GET'])
def index(days):
    message_list = get_news_from_db(int(days))

    return jsonify(message_list), 200
