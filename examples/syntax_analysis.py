import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def main(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    print(response)
    for token in response.tokens:
        print('{}: {}'.format(pos_tag[token.part_of_speech.tag], token.text.content))




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text you\'d like to analyze entities.')
    args = parser.parse_args()
    main(args.text)
