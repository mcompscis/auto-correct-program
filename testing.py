from collections import Counter

sentence1 = "hello my name is my name is hello and my i like to hello my friends"


def sentence_word(sentence):
    word_list = []
    for word in sentence.split():
        word_list.append(word)
    return word_list


print(dict(Counter(sentence_word(sentence1)).most_common(3)))
print(sentence_word(sentence1))
