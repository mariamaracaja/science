import sqlite3
from datetime import date 

# creating database for the articles 
def init_db():
    con = sqlite3.connect("arxiv_database.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE,
            title TEXT,
            abstract TEXT,
            pdf_url TEXT,
            published TEXT,
            favorited INTEGER NOT NULL DEFAULT 0
        )
    """)

    con.commit()
    con.close()

# inserts a new article fetched from the API into the database
def save_article(article_data):
    con = sqlite3.connect("arxiv_database.db")
    cur = con.cursor()

    today = str(date.today())

    cur.execute("""
        INSERT INTO articles (date, title, abstract, pdf_url, published)
        VALUES (?,?,?,?,?)
    """, 
    (today, article_data["title"], article_data["abstract"], article_data["pdf_url"], article_data["published"])
    )

    con.commit()
    con.close()

# checks the database for an article saved with today's date
def get_today_article():
    con = sqlite3.connect("arxiv_database.db")
    cur = con.cursor()

    today = str(date.today())

    cur.execute("SELECT title, abstract, pdf_url, published FROM articles WHERE date = ?", (today,))
    row = cur.fetchone()
    con.close()

    # returns the article formatted as a dictionary or None if not found
    if row:
        return {
            "title": row[0],
            "abstract": row[1],
            "pdf_url": row[2],
            "published": row[3]
        }
    return None

# updates the article by title so its set as "favorited" (1 = True)
def favorite_articles(title):
    con = sqlite3.connect("arxiv_database.db")
    cur = con.cursor()

    cur.execute("""
        UPDATE articles
        SET favorited = 1
        WHERE title = ?
    """, (title,)
    )

    con.commit()
    con.close()
    print(f"Article '{title}' was favorited")