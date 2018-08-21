import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def main(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    features = {'extract_syntax': True,
                'extract_entities': True,
                'extract_document_sentiment': True,
                'extract_entity_sentiment': True,
                'classify_text': False
                }
    response = client.annotate_text(document=document, features=features)
    sentiment = response.document_sentiment
    entities = response.entities

    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    for entity in entities:
        print('=' * 20)
        print('         name: {0}'.format(entity.name))
        print('         type: {0}'.format(entity_type[entity.type]))
        print('     salience: {0}'.format(entity.salience))
        print('wikipedia_url: {0}'.format(entity.metadata.get('wikipedia_url', '-')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text you\'d like to classify text.')
    args = parser.parse_args()
    main(args.text)
