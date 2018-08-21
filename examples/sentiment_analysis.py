import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def main(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('    Sentiment score: {}'.format(sentiment.score))
    print('Sentiment magnitude: {}'.format(sentiment.magnitude))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text you\'d like to analyze sentiment.')
    args = parser.parse_args()
    main(args.text)
