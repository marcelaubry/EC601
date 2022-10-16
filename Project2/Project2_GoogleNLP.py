from google.cloud import language_v1
import os

def sample_analyze_sentiment(text_content):

    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/marce/Downloads/project2-365114-4a2eb989b280.json"

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

print("I am tired, tears are running down my cheeks. My computer is just as pissed as me. Why is it so complicated to use this API?!!?")
sample_analyze_sentiment("I am tired, tears are running down my cheeks. My computer is just as pissed as me. Why is it so complicated to use this API?!!?")
print("\n")
print("We did it! We have successfully made the exercise work like it should! Excellent job everyone!!!")
sample_analyze_sentiment("We did it! We have successfully made the exercise work like it should! Excellent job everyone!!!")
