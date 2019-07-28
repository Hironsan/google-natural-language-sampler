import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def main(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document=document).entities

    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER', 'PHONE_NUMBER', 'ADDRESS', 'DATE', 'NUMBER', 'PRICE')

    for entity in entities:
        print('=' * 20)
        print('         name: {0}'.format(entity.name))
        print('         type: {0}'.format(entity_type[entity.type]))
        print('     salience: {0}'.format(entity.salience))
        print('wikipedia_url: {0}'.format(entity.metadata.get('wikipedia_url', '-')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text you\'d like to analyze entities.')
    args = parser.parse_args()
    main(args.text)
