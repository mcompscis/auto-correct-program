from nltk.corpus import words
word_list = words.words()


def odd_func(numb):
    if numb % 2 != 0:
        return "odd"
    else:
        return "even"


def subs(word, count):
    if odd_func(count) == "odd":
        return "" + word[1] + word[0] + word[2:] + ""
    else:
        return "" + word[0] + word[2] + word[1] + ""


def rearranger(word):
    count = 1
    cur_word = word
    while cur_word not in word_list:
        cur_word = subs(cur_word, count)
        count += 1


print(rearranger('ype'))
