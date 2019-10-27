import json
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import storage
import os

class WordSyntax:
    def __init__(self, language = 'en'):
        path = "nlp/google.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=path
        self.client = language_v1.LanguageServiceClient()
        self.type_ = enums.Document.Type.PLAIN_TEXT
        self.language = language
        self.encoding_type = enums.EncodingType.UTF8

    def lookup(self, lookupstr):
        document = {"content": lookupstr, "type": self.type_, "language": self.language}
        response = self.client.analyze_syntax(document, encoding_type=self.encoding_type)

        tokdict = {}
        for token in response.tokens:
            text = token.text
            part_of_speech = token.part_of_speech
            part_of_speech_tag = enums.PartOfSpeech.Tag(part_of_speech.tag).name

            dependency_edge = token.dependency_edge
            head_token_index = dependency_edge.head_token_index
            label = enums.DependencyEdge.Label(dependency_edge.label).name
            tokdict[text.content] = [text.content, part_of_speech_tag,label]
        return tokdict


a = WordSyntax()
a.lookup("The man was a large asian dude with thick black hair")
