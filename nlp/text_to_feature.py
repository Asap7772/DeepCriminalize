import numpy as np
import os
import pickle
import json


def save_glove():
    BASE_DIR = './'
    GLOVE_DIR = os.path.join(BASE_DIR, 'glove.6B')
    print('Indexing word vectors.')

    embeddings_index = {}
    with open(os.path.join(GLOVE_DIR, 'glove.6B.50d.txt'),encoding='utf-8') as f:
        for line in f:
            word, coefs = line.split(maxsplit=1)
            coefs = np.fromstring(coefs, 'f', sep=' ')
            coefs = coefs.tolist()
            embeddings_index[word] = coefs

    print('Found %s word vectors.' % len(embeddings_index))
    print(type(embeddings_index))
    with open('glove_embeddings.json', 'w') as outfile:
        json.dump(embeddings_index, outfile)

def get_embeddings(keyPhrases = ['bangs']):
    with open('glove_embeddings.json', 'r') as infile:
        embeddings_index = json.load(infile)

    features = ['Five o Clock Shadow', 'Arched Eyebrows', 'Attractive', 'Bags Under Eyes', 'Bald', 'Bangs', 'Big Lips', 'Big Nose', 'Black Hair', 'Blond Hair', 'Blurry', 'Brown Hair', 'Bushy Eyebrows', 'Chubby', 'Double Chin', 'Eyeglasses', 'Goatee', 'Gray Hair', 'Heavy Makeup', 'High Cheekbones', 'Male', 'Mouth Slightly Open', 'Mustache', 'Narrow Eyes', 'No Beard', 'Oval Face', 'Pale Skin', 'Pointy Nose', 'Receding Hairline', 'Sideburns', 'Smiling', 'Straight Hair', 'Wavy Hair', 'Wearing Earrings','Wearing Hat', 'Wearing Lipstick', 'Wearing Necklace','Wearing Necktie', 'Young']
    feature_embeddings = np.ndarray(shape=(len(features),50))
    i=0
    for feature in features:
        print('Feature: ', feature)
        feature = feature.lower()
        feature_embedding = np.zeros((50))
        for word in feature.split():
            print("Word: ",word)
            try:
                word_embedding=embeddings_index[word]
                feature_embedding = np.add(feature_embedding, word_embedding)
            except:
                pass
        feature_embedding = np.divide(feature_embedding,len(feature.split()))
        feature_embeddings[i]=feature_embedding
        i+=1
    
    phrase_embeddings = np.ndarray(shape=(len(keyPhrases),50))
    i=0
    for phrase in keyPhrases:
        print("Phrase: ",phrase)
        phrase = phrase.lower()
        phrase_embedding = np.zeros((50))
        for word in phrase.split():
            print('Word: ',word)
            try:
                word_embedding=embeddings_index[word]
                phrase_embedding = np.add(phrase_embedding, word_embedding)
            except:
                pass
        phrase_embedding = np.divide(phrase_embedding,len(phrase.split()))
        phrase_embeddings[i]=phrase_embedding
        i+=1
    return feature_embeddings, phrase_embeddings

def get_closest_feature():
    features = ['Five o Clock Shadow', 'Arched Eyebrows', 'Attractive', 'Bags Under Eyes', 'Bald', 'Bangs', 'Big Lips', 'Big Nose', 'Black Hair', 'Blond Hair', 'Blurry', 'Brown Hair', 'Bushy Eyebrows', 'Chubby', 'Double Chin', 'Eyeglasses', 'Goatee', 'Gray Hair', 'Heavy Makeup', 'High Cheekbones', 'Male', 'Mouth Slightly Open', 'Mustache', 'Narrow Eyes', 'No Beard', 'Oval Face', 'Pale Skin', 'Pointy Nose', 'Receding Hairline', 'Sideburns', 'Smiling', 'Straight Hair', 'Wavy Hair', 'Wearing Earrings','Wearing Hat', 'Wearing Lipstick', 'Wearing Necklace','Wearing Necktie', 'Young']
    feature_embeddings,phrase_embeddings = get_embeddings()
    results=[]
    for phrase_embedding in phrase_embeddings:
        dot_products=[np.dot(phrase_embedding,feature_embedding) for feature_embedding in feature_embeddings]
        print(dot_products)
        idx = np.argmin(dot_products)
        results.append(features[idx])
    print(results)

get_closest_feature()