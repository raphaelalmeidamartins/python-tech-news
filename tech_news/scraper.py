import requests
from ratelimiter import RateLimiter
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
