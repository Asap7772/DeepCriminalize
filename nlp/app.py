from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from nlp.keyPhraseApi import KeyPhrases
# from nlp.syntaxApi import WordSyntax
from src.tl_gan.script_generation_interactive import gen_image
from nlp.text_to_feature import get_closest_feature

import io
import base64
import json

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'



dictReturn = {}
imgs = {}


@app.route("/", methods=["PUT"])
@cross_origin()
def put():
    uid = request.json['uid']
    # officer = request.json['o']
    # caseNumber = request.json['cn']
    # witnessName = request.json['wn']
    gender = request.json['g']
    ethnicity = request.json['e']
    moreDetails = request.json['md']


    # keyPhrases = moreDetails.split()

    keyPhrases = KeyPhrases().lookup(moreDetails)
    # syntaxDict =  WordSyntax().lookup(moreDetails)
    print('KeyPhrases:',keyPhrases)

    arr = ['Arched_Eyebrows', 'Attractive', 'Bags_Under_Eyes', 'Bald', 'Bangs', 'Big_Lips',
    'Big_Nose', 'Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Bushy_Eyebrows', 'Chubby', 'Double_Chin',
    'Eyeglasses', 'Goatee', 'Gray_Hair', 'Heavy_Makeup', 'High_Cheekbones', 'Male', 'Mouth_Slightly_Open',
    'Mustache', 'Narrow_Eyes', 'No_Beard', 'Oval_Face', 'Pale_Skin', 'Pointy_Nose', 'Receding_Hairline',
    'Rosy_Cheeks', 'Sideburns', 'Smiling', 'Straight_Hair', 'Wavy_Hair', 'Young']

    features = {}
    for key in keyPhrases:
        # print('key',key)
        direct = key.title().replace(' ','_')
        for a in arr:
            if direct == a:
                features[direct] = 1
            else:
                words = direct.split('_')
                for word in words:
                    if word.lower() == a.lower():
                        features[word] = 1

    # features = get_closest_feature(keyPhrases = keyPhrases)

    print('Features: ',features)
    # prev = None
    # for x in syntaxDict:
    #     if syntaxDict[x] == 'adj' or syntaxDict[x] == 'adv':
    #         pass

    images = gen_image(gender, ethnicity, features)
    for i in range(len(images)):
        imgs[i] = images[i]


    # dictReturn[uid] = [officer, caseNumber, witnessName, gender, ethnicity, moreDetails, keyPhrases, syntaxDict]
    dictReturn[uid] = [gender, ethnicity, moreDetails, keyPhrases]

    # for i in range(len(images)):
    #     imgByteArr = io.BytesIO()
    #     images[i].save(imgByteArr, format = 'JPEG')
    #     imgByteArr = imgByteArr.getvalue()
    #     imgs[i] = json.dumps({str(i): imgByteArr.encode('base64')})
    #     print("type of images:", type(imgs[i]))

    # print('dictReturn: ',dictReturn)
    
    return jsonify(dictReturn)

@cross_origin()
@app.route("/", methods=["POST"])
def get():
    print('REQUEST.JSON:', request.json)
    uid = request.json['uid']
    print(dictReturn)
    return json.dumps(imgs, ensure_ascii=False, indent=4)

@cross_origin()
@app.route("/clear/")
def clear():
    dict = {}
