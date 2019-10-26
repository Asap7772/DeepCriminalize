from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os


class KeyPhrases:
    EXT_ANALYTICS_SUBSCRIPTION_KEY = ""
    TEXT_ANALYTICS_ENDPOINT = ""

    def __init__(self, language = 'en'):
        key_var_name = 'TEXT_ANALYTICS_SUBSCRIPTION_KEY'
        if not key_var_name in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
        subscription_key = os.environ[key_var_name]

        endpoint_var_name = 'TEXT_ANALYTICS_ENDPOINT'
        if not endpoint_var_name in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
        endpoint = os.environ[endpoint_var_name]

        credentials = CognitiveServicesCredentials(subscription_key)
        self.text_analytics = TextAnalyticsClient(endpoint=text_analytics_url, credentials=credentials)
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

        response = text_analytics.key_phrases(documents=documents)
        return response.documents[0].key_phrases
