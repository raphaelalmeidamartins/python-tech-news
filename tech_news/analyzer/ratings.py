from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news_list = sorted(
        find_news(),
        key=lambda news: (-news["comments_count"], news["title"]),
    )

    result = [
        (news["title"], news["url"])
        for news in news_list
    ]

    return result[0:5]

    """
        Descobri sobre a utilização do sorted para ordenar discionários aqui:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    """

    """
        Após a aprovação no projeto,
        não esquecer de refatorar
        essa função para usar
        o método agregate do mongoDB
        com a query abaixo
        query = [{"$sort": {"comments_count": -1, "title": 1}}, {"$limit": 5}]
    """


# Requisito 11
def top_5_categories():
    categories = [news["category"] for news in find_news()]
    categories = [
        {"name": name, "count": count}
        for name, count in Counter(categories).items()
    ]

    sorted_categories = sorted(
        categories,
        key=lambda category: (-category["count"], category["name"]),
    )

    result = [category["name"] for category in sorted_categories][0:5]

    return result
