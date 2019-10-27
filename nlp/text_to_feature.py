from nlp.keyPhraseApi import KeyPhrases
from nlp.syntaxApi import WordSyntax
import numpy as np
import os
import pickle

BASE_DIR = 'nlp/'
GLOVE_DIR = os.path.join(BASE_DIR, 'glove.6B')

print('Indexing word vectors.')

embeddings_index = {}
with open(os.path.join(GLOVE_DIR, 'glove.6B.300d.txt'),encoding='utf-8') as f:
    for line in f:
        word, coefs = line.split(maxsplit=1)
        coefs = np.fromstring(coefs, 'f', sep=' ')
        embeddings_index[word] = coefs

print('Found %s word vectors.' % len(embeddings_index))
emb






testSentence = "The caucasian male has long blonde hair, pretty big nose, big lips, a big mustache. He is very attractive but slightly intimidating."
keyPhrase = KeyPhrases()
wordSyntax = WordSyntax()
phrases=keyPhrase.lookup(testSentence)
print(keyPhrase.lookup(testSentence))
embeddings_index = np.load(os.path.join('nlp','embeddings_index.npy'))

features = ['Five o Clock Shadow', 'Arched Eyebrows', 'Attractive', 'Bags Under Eyes', 'Bald', 'Bangs', 'Big Lips', 'Big Nose', 'Black Hair', 'Blond Hair', 'Blurry', 'Brown Hair', 'Bushy Eyebrows', 'Chubby', 'Double Chin', 'Eyeglasses', 'Goatee', 'Gray Hair', 'Heavy Makeup', 'High Cheekbones', 'Male', 'Mouth Slightly Open', 'Mustache', 'Narrow Eyes', 'No Beard', 'Oval Face', 'Pale Skin', 'Pointy Nose', 'Receding Hairline', 'Sideburns', 'Smiling', 'Straight Hair', 'Wavy Hair', 'Wearing Earrings','Wearing Hat', 'Wearing Lipstick', 'Wearing Necklace','Wearing Necktie', 'Young']
for feature in features:
    print('hi')
    feature = feature.lower()
    feature_embeddings = []
    feature_embedding = np.zeros((300))
    for word in feature:
        print('here')
        word_embedding=embeddings_index[word]
        feature_embedding = np.array([a+b for a,b in zip(feature_embedding, word_embedding)])
        feature_embeddings.append(feature_embedding)
np.save('feature_embeddings',feature_embeddings)
print(len(feature_embeddings))

for phrase in phrases:
    phrase_embedding = np.zeros((300))
    for word in phrase:
        word_embedding=embeddings_index[word]
        phrase_embedding = [a+b for a,b in zip(phrase_embedding, word_embedding)]

print(wordSyntax.lookup(testSentence))