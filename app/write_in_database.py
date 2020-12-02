from sqlalchemy import func

from app import db, models


def find_dublicate_news(url):
    result = db.session.query(models.News).filter(models.News.url == url).first()
    if result:
        return True

    return False


def find_dublicate_exception(url):
    result = db.session.query(models.ExceptionLoad).filter(models.ExceptionLoad.url == url).first()
    if result:
        return True

    return False


def write_news(list_news):
    written = len(list_news)
    for news in list_news:

        if find_dublicate_news(news['url']):
            written -= 1
            continue

        max_id = db.session.query(func.max(models.News.id)).first()[0]

        if not max_id:
            max_id = 0

        new_id = max_id + 1
        new_db_object = models.News(
            id=new_id,
            date_publication=news['date_publication'],
            title=news['title'],
            text=news['text'],
            url=news['url']
        )
        db.session.add(new_db_object)
        db.session.commit()


def write_exception(list_exception):

    for excep in list_exception:

        if find_dublicate_exception(excep['url']):
            continue

        max_id = db.session.query(func.max(models.ExceptionLoad.id)).first()[0]

        if not max_id:
            max_id = 0

        new_id = max_id + 1
        print(new_id)
        new_db_object = models.ExceptionLoad(
            id=new_id,
            traceback=str(excep['traceback']),
            url=str(excep['url']),
        )
        db.session.add(new_db_object)
        db.session.commit()
