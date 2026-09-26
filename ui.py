from tkinter import *
from tkinter import ttk
import customtkinter as ctk 

from arxiv_services import fetch_article
from database import init_db, save_article, get_today_article, favorite_articles

import webbrowser

# entire UI with main window, labels with title, summary and published date 
def database_ui(article):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("Article of the day")
    app.geometry("800x600")
    app.resizable(width=True, height=True) # allow resizing

    title_label = ctk.CTkLabel(
        app, 
        text=article['title'], 
        font=("Helvetica", 28),
        wraplength=700
    )

    title_label.pack(pady=(20, 10), padx=20)

    published_label = ctk.CTkLabel(
        app,
        text=f"Published on {article['published']}",
        font=("Helvetica", 16),
    )

    published_label.pack(pady=(0, 10))

    summary_textbox = ctk.CTkTextbox(
        app,
        width=700,
        height=300,
        wrap="word",
        font=("Helvetica", 17)
    )

    summary_textbox.pack(pady=(0, 9), padx=20)

    summary_textbox.insert("0.0", article['abstract'])
    summary_textbox.configure(state="disabled")

    link_label = ctk.CTkLabel(
        app,
        text=f"Access this article through {article['pdf_url']}"
    )

    link_label.pack(pady=(0, 8))

    # button to set the article as favorite 
    def favorites_click():
        favorite_articles(article["title"])
        save_button.configure(text="Favorited", state="disabled")

    save_button = ctk.CTkButton(
    app, 
    text="Save to favorites", 
    command=favorites_click
    )

    save_button.pack(pady=(0, 7))

    app.mainloop()

if __name__ == "__main__":
    # initialize database 
    init_db()
    
    article = get_today_article()
    
    if not article:
        article = fetch_article()
        if article:
            save_article(article)

    if article:
        database_ui(article)