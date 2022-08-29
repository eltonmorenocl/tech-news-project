import time
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
    selector = Selector(html_content)
    next = selector.css("a.next.page-numbers::attr(href)").get()
    return next


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    comments = selector.css("ol.comment-list li").getall()
    summary = selector.xpath('string(//div[@class="entry-content"]//p)').get()
    tags = selector.css("section.post-tags ul li a[rel='tag']::text").getall()
    category = selector.css("a.category-style span.label::text").get()

    return {
        "url": url,
        "title": title.rstrip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments),
        "summary": summary.strip(),
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
