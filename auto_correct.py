from collections import Counter
import re
import correction
from word_counter import word_count_25
import word_counter

# words = re.findall(r'\w+', open('/Users\Alka\Desktop\data.txt').read().lower())
# common_words_pair = dict(Counter(words))
# common_words = set(common_words_pair.keys())

common_wiki = set(word_count_25.keys())


def common_filter(word):
    all_words = correction.correction(word)
    return common_wiki & all_words


def common_values(word):
    list_words = common_filter(word)
    list_dict = {}
    for key, value in word_count_25.items():
        if key in list_words:
            list_dict[key] = value
    return list_dict


def most_common_words(word):
    dict_words = common_values(word)
    return list(dict(Counter(dict_words).most_common(5)).keys())


def best_words(word):
    list_words = most_common_words(word)
    for x in list_words:
        print(x)


best_words("walet")


