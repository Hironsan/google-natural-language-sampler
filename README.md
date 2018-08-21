# google-natural-language-sampler

Code examples for Google Natural Language API written in Python.

## Description

Example codes has following features:

* Sentiment Analysis
* Named Entity Recognition
* Syntax Analysis
* Entity Sentiment Analysis
* Text Classification
* Text Annotation

## Requirement

* Python 3.x
* Credentials

## Setup

To install necessary library, simply use pip:

```bash
pip install google-cloud-language
```

or,

```bash
pip install -r requirements.txt
```

Next, set up to authenticate with the Cloud Natural Language API using your project's service account credentials. Then, set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to your downloaded service account credentials:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
```

## Quick Start: Running the Example

### Sentiment Analysis

```bash
$ python examples/sentiment_analysis.py "Hello world"
Text: Hello, world
Sentiment: 0.30000001192092896, 0.30000001192092896
```

### Named Entity Recognition

```bash
$ python examples/named_entities.py "President Obama is speaking at the White House."
====================
         name: Obama
         type: PERSON
     salience: 0.9082207679748535
wikipedia_url: -
====================
         name: White House
         type: LOCATION
     salience: 0.09177924692630768
wikipedia_url: https://en.wikipedia.org/wiki/White_House
```

### Syntax Analysis

```bash
$ python examples/syntax_analysis.py ""
```

### Entity Sentiment Analysis

```bash
$ python examples/entity_sentiment.py ""
```

### Text Classification

```bash
$ python examples/text_classification.py ""
```

### Text Annotation

```bash
$ python examples/text_annotation.py ""
```

## Image Sizing

To enable accurate image detection within the Google Cloud Vision API, images should generally be a minimum of 640 x 480 pixels (about 300k pixels). Full details for different types of Vision API Feature requests are shown below:

| Vision API Feature | Recommended Size | Notes |
|---|---|---|
| FACE_DETECTION | 1600 x 1200 | Distance between eyes is most important |
| LANDMARK_DETECTION | 640 x 480 |   |
| LOGO_DETECTION | 640 x 480 |   |
| LABEL_DETECTION | 640 x 480 |   |
| TEXT_DETECTION | 1024 x 768 | OCR requires more resolution to detect characters |
| SAFE_SEARCH_DETECTION | 640 x 480 |   |

## Licence

[MIT](https://github.com/Hironsan/google-vision-sampler/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)

## References

* [Natural Language API Client Libraries](https://cloud.google.com/natural-language/docs/reference/libraries)
* [Method: documents.classifyText](https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText)