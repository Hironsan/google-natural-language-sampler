import argparse
import os

from utils import Service


def main(text_file):

    access_token = os.environ.get('LANGUAGE_API')
    service = Service('language', 'v1beta1', 'analyzeEntities', access_token=access_token)

    with open(text_file, 'rb') as f:
        text = f.read().decode('utf-8')
        body = {
            "document": {
                "type": "PLAIN_TEXT",
                "language": "EN",
                "content": text
            },
            "encodingType": "UTF8"
        }
        response = service.execute(body=body)
        print(response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text_file', help='The text you\'d like to extract entities.')
    args = parser.parse_args()
    main(args.text_file)
