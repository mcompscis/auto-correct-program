import string
import random

given_phrase = "methinks it is like a weasel"
sample = "mertbkfpofco qb pkqt vxenzvi"


def rand_phrase(length):
    letters = string.ascii_lowercase + " "
    return "".join(random.choice(letters) for i in range(length))


print(rand_phrase(len(given_phrase)))


def phrase_score(ra_phrase, phrase):
    count = 0
    score = 0
    for x in ra_phrase:
        if x == phrase[count]:
            score += ((1 / len(phrase)) * 100)
            count += 1
        else:
            score += 0
            count += 1
    return score


print(phrase_score(sample, given_phrase))


def final_func(phrase):
    some_phrase = rand_phrase(len(phrase))
    count = 0
    while phrase_score(some_phrase, phrase) < 100:
        some_phrase = rand_phrase(len(phrase))
        count += 1
    print(some_phrase)
    print("It took " + str(count) + ' tries!')


final_func(given_phrase)



final_func



        

