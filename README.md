# Daily Scientific Articles 

### Description
A terminal-launched desktop app built with Python, CustomTkinter, and SQLite. The application serves an "Article of the Day" fetched directly from the arXiv API. 
Everyday, the user can see a different random article about physics, mathematics and computer science.

## Features

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2+-00599E?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite)

* Cache-First: Checks the local SQLite database (`arxiv_database.db`) for todays entry before querying the arXiv API.
* Modern GUI: Built with `customtkinter` instead of tkinter with display, formatted  labels, and interactive actions for a more modern and stylish UI :).
* LaTeX Text replacement: Built-in Regex cleaner to scrub raw LaTeX artifacts (`\textbf{}`, `\times`, `$`) for a seamless reading.

---

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/mariamaracaja/science.git](https://github.com/mariamaracaja/science.git)
   cd science.git 

## Future improvements
- [ ] Favorites Page with filtering and "Remove" option.

- [ ] Category selector in the UI.

- [ ] Conversion into a native desktop widget/desklet.

- [ ] Light/dark theme toggle.

---

this is a very flexible project and a lot can be done with it :))
