import time
from types import new_class
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)

        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = selector.css('h2.entry-title a::attr(href)').getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
