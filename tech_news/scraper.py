import requests
from bs4 import BeautifulSoup
from parsel import Selector
from ratelimiter import RateLimiter

from tech_news.database import create_news


# Requisito 1
@RateLimiter(max_calls=1, period=1)
def fetch(url):
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Dica de Lais Namatela 19A - https://pypi.org/project/ratelimiter/#description


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()) or 0,
        "summary": BeautifulSoup(
            selector.css(".entry-content p").get(), "html.parser"
        )
        .get_text()
        .strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://blog.betrybe.com/")
    news_url_list = []

    while len(news_url_list) < amount:
        news_url_list += scrape_novidades(html_content)

        if len(news_url_list) < amount:
            html_content = fetch(scrape_next_page_link(html_content))

    news_dicts_list = [
        scrape_noticia(fetch(url))
        for url in news_url_list[0:amount]
    ]

    create_news(news_dicts_list)

    return news_dicts_list
