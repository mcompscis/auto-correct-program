from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://en.wikipedia.org/wiki/Wikipedia:Featured_articles'

# opening the connection and grabbing the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each link
card_text = page_soup.findAll('span', {"class": "featured_article_metadata has_been_on_main_page"})


def url_getter():
    links = []
    for x in card_text:
        try:
            links.append('https://en.wikipedia.org' + x.a['href'])
        except Exception:
            continue
    return links


#print(len(url_getter()))

