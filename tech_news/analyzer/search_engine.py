from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    title_lower = title.lower()
    query = {"title": {"$regex": f".*{title_lower}.*", "$options": "i"}}
    found_news = search_news(query)
    result = [(news["title"], news["url"]) for news in found_news]
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
