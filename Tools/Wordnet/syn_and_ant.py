# NLP Model to detect synonyms and antonyms

import nltk
from nltk.corpus import wordnet


def find_increment(word):
    synonyms = []
    antonyms = []
    most_similar = ''
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    print(synonyms)
    print(antonyms)
    w1 = wordnet.synset(word)[0]
    w2 = wordnet.synset('more.v.01')
    w2 = wordnet.synset('less.v.01')
    print("Similarity: more " + w1.wup_similarity(w2))
    print("Similarity: more " + w1.wup_similarity(w3))
