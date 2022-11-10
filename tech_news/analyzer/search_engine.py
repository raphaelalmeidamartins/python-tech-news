from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_list = search_news(query)
    return [
        (news["title"], news["url"])
        for news in news_list
    ]


# Requisito 7
def search_by_date(date):
    try:
        param_date_pattern = "%Y-%m-%d"
        db_date_pattern = "%d/%m/%Y"

        converted_date = datetime.strptime(
            date, param_date_pattern
            ).strftime(db_date_pattern)

        query = {"timestamp": converted_date}

        news_list = search_news(query)

        return [
            (news["title"], news["url"])
            for news in news_list
        ]
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    news_list = search_news(query)
    return [
        (news["title"], news["url"])
        for news in news_list
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
