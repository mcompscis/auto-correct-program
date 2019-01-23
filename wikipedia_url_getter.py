from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# the main url of Wikipedia that contains links to several articles
my_url = 'https://en.wikipedia.org/wiki/Wikipedia:Featured_articles'

# opening the connection and grabbing the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each link
card_text = page_soup.findAll('span', {"class": "featured_article_metadata has_been_on_main_page"})

# url_getter(): goes to the main Wikipedia page with links to several articles and returns all the links of the article
#               in the list


def url_getter():
    links = []
    for x in card_text:
        try:
            links.append('https://en.wikipedia.org' + x.a['href'])
        except Exception:
            continue
    return links


# this results in 4474
# there are 4474 possible links to construct word-frequency dictionary with
# print(len(url_getter()))

