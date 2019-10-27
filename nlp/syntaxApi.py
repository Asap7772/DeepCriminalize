import json
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import storage
import os

class WordSyntax:
    def __init__(self, language = 'en'):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="nlp/google.json"
        self.client = language_v1.LanguageServiceClient()
        self.type_ = enums.Document.Type.PLAIN_TEXT
        self.language = language
        self.encoding_type = enums.EncodingType.UTF8

    def lookup(self, lookupstr):
        document = {"content": lookupstr, "type": self.type_, "language": self.language}
        response = self.client.analyze_syntax(document, encoding_type=self.encoding_type)

        pos dict = {}
        for token in response.tokens:
            text = token.text
            print(u"Token text: {}".format(text.content))
            part_of_speech = token.part_of_speech
            print(u"Part of Speech tag: {}".format(enums.PartOfSpeech.Tag(part_of_speech.tag).name))

            dependency_edge = token.dependency_edge
            print(u"Head token index: {}".format(dependency_edge.head_token_index))
            print(u"Label: {}".format(enums.DependencyEdge.Label(dependency_edge.label).name))



a = WordSyntax()
a.lookup("The man was a large asian dude with thick black hair")
