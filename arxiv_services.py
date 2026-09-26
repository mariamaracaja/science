import arxiv 
import random
import re

# function to replace latex characters and return cleaner text 
def clean_latex(text):
    if not text:
        return ""

    text = re.sub(r'\\\w+\{([^}]+)\}', r'\1', text)

    text = text.replace(r'\times', 'x')
    text = text.replace(r'\le', '<=')
    text = text.replace(r'\approx', '~')
    text = text.replace(r'\ge', '>=')
    text = text.replace('$', '')
    
    return text

def fetch_article(category=None):
    # list with all categories supported by the arxiv API
    all_categories = [
        "cs.AI",         
        "physics.gen-ph",
        "astro-ph",      
        "q-bio.NC",      
        "math.GM",       
        "stat.ML"        
    ]

    if category is None:
        category = random.choice(all_categories)

    # construct default API client.
    client = arxiv.Client()

    # to fetch a random result
    random_offset = random.randint(0, 200)

    # search for an article within the given categories 
    search = arxiv.Search(
        query=f"cat:{category}",
        max_results=1,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    # find the random article 
    try:
        results = client.results(search, offset=random_offset)
        paper = next(results)
    except StopIteration:
        results = client.results(search)
        try:
            paper = next(results)
        except StopIteration:
            return None

    return {
        "title": clean_latex(paper.title),
        "abstract": clean_latex(paper.summary),
        "pdf_url": paper.pdf_url,
        "published": paper.published.strftime("%d-%m-%Y")
    }