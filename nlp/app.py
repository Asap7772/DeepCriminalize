from flask import Flask, request, jsonify
from nlp.KeyPhraseApi import KeyPhrases
from nlp.SyntaxApi import WordSyntax

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
    dict[uid] = [officer, caseNumber, witnessName, gender, ethnicity, moreDetails, keyPhrases, syntaxDict]
    return jsonify(dict)

@app.route("/", methods=["GET"])
def get():
    uid = request.json['uid']
    return dict[uid][-1]
