import numpy as np
import nltk #pip install nltk(neural networks)
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

#tokenize the sentence
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

#sentence to word
def stem(word):
    return Stemmer.stem(word.lower())

#tokinized sentences stored in bags
def bag_of_words(tokenized_sentence,words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words),dtype = np.float32)

    for idx , w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1

    return bag
