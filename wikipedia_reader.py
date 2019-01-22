from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

link = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

f = urlopen(link)
page = f.read()
f.close()

parsed_text = soup(page, "html.parser")
paragraphs_create = (parsed_text.findAll("p"))
big_sentence = [paragraph.text for paragraph in paragraphs_create]


for x in big_sentence:
    print(x)