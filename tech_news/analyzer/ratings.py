from tech_news.database import search_news


# Requisito 10
def top_5_news():
    query = {"$sort": {"comments_count": -1, "$limit": 5}}
    news_list = search_news(query)
    return [
        (news["title"], news["url"])
        for news in news_list
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
