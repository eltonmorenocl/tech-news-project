from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})

    find_news = []

    for new in news:
        title_url = (new['title'], new['url'])
        find_news.append(title_url)

    return find_news


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        news = search_news({"timestamp": date_format})

        result = [(new["title"], new["url"]) for new in news]

        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    get_news = search_news({"tags": {"$regex": tag, "$options": "i"}})

    get_tag = [(new["title"], new["url"]) for new in get_news]

    return get_tag


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
