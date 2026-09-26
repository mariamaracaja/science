from arxiv_services import fetch_article
from database import init_db, save_article, get_today_article, favorite_articles
from ui import database_ui

if __name__ == "__main__":
    # initialize database 
    init_db()

    article = get_today_article()

    # if no article is found for today, fetch a new one from the arXiv API and save it
    if not article:
        article = fetch_article()
        if article:
            save_article(article)

    # display article on the database 
    if article:
        database_ui(article)
    else:
        print("Error")