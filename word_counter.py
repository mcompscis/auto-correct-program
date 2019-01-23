from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from collections import Counter
from wikipedia_url_getter import url_getter
import string

# link = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# word_list = ['name', 'hello', 'my', 'hello', 'my']
# word_freq = [word_list.count(w) for w in word_list]
# word_pair = dict(zip(word_list, word_freq))


def remove_punc(sentence):
    a_sentence = [letter for letter in sentence]
    new_sentence = []
    for c in a_sentence:
        if c in string.punctuation:
            new_sentence.append('')
        else:
            new_sentence.append(c.lower())
    return ''.join(new_sentence)


def sentence_word(sentence):
    word_list = []
    for word in sentence.split():
        word_list.append(word)
    return word_list


def big_text(url):
    f = urlopen(url)
    page = f.read()
    f.close()
    parsed_text = soup(page, "html.parser")
    paragraphs_create = parsed_text.findAll("p")
    big_sentence = [paragraph.text for paragraph in paragraphs_create]
    return remove_punc(big_sentence)


def combine_big_text():
    link_list = url_getter()
    link_list = link_list[0:50]
    large_text = ''
    for link in link_list:
        large_text = large_text + big_text(link)
    return dict(Counter(sentence_word(large_text)))


word_count_25 = combine_big_text()
# print(len(word_count_25))
# over 4000 links

