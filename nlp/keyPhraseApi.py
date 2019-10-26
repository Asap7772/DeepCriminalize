from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os
import Constants

class KeyPhrases:
    def __init__(self, language = 'en'):
        self.subscription_key = Constants.EXT_ANALYTICS_SUBSCRIPTION_KEY
        self.endpoint = Constants.TEXT_ANALYTICS_ENDPOINT
        self.text_analytics_url  = Constants.TEXT_ANALYTICS_URL
        print(self.text_analytics_url)

        credentials = CognitiveServicesCredentials(self.subscription_key)
        self.text_analytics = TextAnalyticsClient(endpoint=self.text_analytics_url, credentials=credentials)
        self.docId = 0
        self.language = language

    def lookup(self, lookupstr):
        documents = [
            {
                "id": str(self.docId),
                "language": self.language,
                "text": lookupstr
            }
        ]

        response = self.text_analytics.key_phrases(documents=documents)
        return response.documents[0].key_phrases


a = KeyPhrases()
lst = a.lookup("The man was a large asian dude with thick black hair")
print(lst)
