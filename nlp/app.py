from flask import Flask, request, jsonify
from nlp.keyPhraseApi import KeyPhrases
from nlp.syntaxApi import WordSyntax
# from KeyPhraseApi import KeyPhrases
# from SyntaxApi import WordSyntax
from src.tl_gan.script_generation_interactive import gen_image

app = Flask(__name__)


dict = {}
@app.route("/", methods=["PUT", "POST"])
def put():
    uid = request.json['uid']
    officer = request.json['o']
    caseNumber = request.json['cn']
    witnessName = request.json['wn']
    gender = request.json['g']
    ethnicity = request.json['e']
    moreDetails = request.json['md']

    keyPhrases = KeyPhrases().lookup(moreDetails)
    syntaxDict =  WordSyntax().lookup(moreDetails)

    arr = ['Arched_Eyebrows', 'Attractive', 'Bags_Under_Eyes', 'Bald', 'Bangs', 'Big_Lips',
    'Big_Nose', 'Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Bushy_Eyebrows', 'Chubby', 'Double_Chin',
    'Eyeglasses', 'Goatee', 'Gray_Hair', 'Heavy_Makeup', 'High_Cheekbones', 'Male', 'Mouth_Slightly_Open',
    'Mustache', 'Narrow_Eyes', 'No_Beard', 'Oval_Face', 'Pale_Skin', 'Pointy_Nose', 'Receding_Hairline',
    'Rosy_Cheeks', 'Sideburns', 'Smiling', 'Straight_Hair', 'Wavy_Hair', 'Young']

    #direct matching
    features = {}
    singleWords = {}
    for key in keyPhrases:
        print('key',key)
        direct = key.title().replace(' ','_')
        for a in arr:
            if direct == a:
                features[direct] = 1
            else:
                words = direct.split('_')
                for word in words:
                    if word.lower() == a.lower():
                        features[word] = 1

    prev = None
    for x in syntaxDict:
        if syntaxDict[x] == 'adj' or syntaxDict[x] == 'adv':
            pass

    image1, image2, image3 = gen_image(gender, ethnicity, features)

    dict[uid] = [officer, caseNumber, witnessName, gender, ethnicity, moreDetails, keyPhrases, syntaxDict]
    print('here',dict)

    return jsonify(dict)

@app.route("/", methods=["GET"])
def get():
    uid = request.json['uid']
    print(dict)
    return jsonify({'image1': 'hi', 'image2': 'hi', 'image3':'hi','description': dict[uid][-1]})

@app.route("/clear/")
def clear():
    dict = {}
