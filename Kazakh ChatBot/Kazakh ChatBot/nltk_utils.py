import numpy as np
import nltk
from kazstem import kazstem

def tokenize(sentence):
    # split sentence into array of words/tokens
    # a token can be a word or punctuation character, or number
    return nltk.word_tokenize(sentence)


def stem(word):
    # stemming = find the root form of the word
    return kazstem(word.lower())


def bag_of_words(tokenized_sentence, words):
    # return bag of words array:
    # 1 for each known word that exists in the sentence, 0 otherwise
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag