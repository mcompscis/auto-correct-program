from nltk.corpus import words
import string
import itertools

word_list = words.words()
letters = string.ascii_lowercase


def valid(set_word):
    word_set = set_word
    dict_word_set = set(word_list)
    if word_set & dict_word_set:
        return word_set & dict_word_set


def correction_one(word):
    split = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    sub = [(L + R[1] + R[0] + R[2:]) for L, R in split if len(R) > 1]
    delete = [(L + R[1:]) for L, R in split if len(L) != len(word)]
    switch = [L + C + R[1:] for L, R in split if len(L) != len(word) for C in letters]
    add = [L + C + R for L, R in split for C in letters]
    all_words = sub + delete + switch + add
    return all_words


def correction_two(word):
    list_word = []
    wrd_list = correction_one(word)
    for x in wrd_list:
        list_word.append(correction_one(x))
    return valid(set(list(itertools.chain.from_iterable(list_word))))


def correction(word):
    set_one = valid(set(correction_one(word)))
    set_two = correction_two(word)
    if set_one is None:
        return set_two
    elif set_two is None:
        return set_one
    else:
        return set_one | set_two


def whitespace(word):
    split = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    word1 = ''
    word2 = ''
    word_set = []
    for x in split:
        if list(x)[0] in word_list and list(x)[1] in word_list:
            word1 = list(x)[0]
            word2 = list(x)[1]
            word_set.append(word1 + " " + word2)
    return set(word_set)


# print(whitespace('theirresponsibility'))
# print(correction('myspace'))
# print(correction("cta"))
