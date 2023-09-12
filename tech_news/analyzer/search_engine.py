from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    title_lower = title.lower()
    query = {"title": {"$regex": f".*{title_lower}.*", "$options": "i"}}
    found_news = search_news(query)
    result = [(news["title"], news["url"]) for news in found_news]
    return result


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        date_iso = date.strftime('%d/%m/%Y')
        query = {"timestamp": {"$regex": f".*{date_iso}.*", "$options": "i"}}
        found_news = search_news(query)
        result = [(news["title"], news["url"]) for news in found_news]
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
