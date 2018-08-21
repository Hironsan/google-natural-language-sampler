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

For more information, see [Analyzing sentiment](https://cloud.google.com/natural-language/docs/analyzing-sentiment).

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

For more information, see [Analyzing entities](https://cloud.google.com/natural-language/docs/analyzing-entities).

### Syntax Analysis

```bash
$ python examples/syntax_analysis.py "President Obama is speaking at the White House."
NOUN: President
NOUN: Obama
VERB: is
VERB: speaking
ADP: at
DET: the
NOUN: White
NOUN: House
PUNCT: .
```

For more information, see [Analyzing syntax](https://cloud.google.com/natural-language/docs/analyzing-syntax).

### Entity Sentiment Analysis

```bash
$ python examples/entity_sentiment.py "President Obama is speaking at the White House."
====================
         name: Obama
         type: PERSON
     salience: 0.9082207679748535
wikipedia_url: -
    magnitude: 0.10000000149011612
        score: 0.0
====================
         name: White House
         type: LOCATION
     salience: 0.09177924692630768
wikipedia_url: https://en.wikipedia.org/wiki/White_House
    magnitude: 0.0
        score: 0.0
```

For more information, see [Analyzing entity sentiment](https://cloud.google.com/natural-language/docs/analyzing-entity-sentiment).

### Text Classification

```bash
$ python examples/classify_text.py "On Saturday, Sevilla FC announced the signing of Spanish defender Aleix Vidal from defending LaLiga champions FC Barcelona. Via their official website, Barcelona said they were to receive €8.5 million transfer as well as two million in variables."
====================
name            : /Sports/Team Sports/Soccer
confidence      : 0.9900000095367432
====================
name            : /News
confidence      : 0.550000011920929

```

For more information, see [Classifying text](https://cloud.google.com/natural-language/docs/classifying-text).
In [the content category page](https://cloud.google.com/natural-language/docs/categories), You can see all categories returned by classify_text method.

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

* [Natural Language](https://googlecloudplatform.github.io/google-cloud-python/latest/language/usage.html)
* [Natural Language API Client Libraries](https://cloud.google.com/natural-language/docs/reference/libraries)
* [Method: documents.classifyText](https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText)