import argparse

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from string import punctuation


def main():
    args = parse_arguments()
    data = ""

    try:
        with open(args.filepath, "r") as file:
            data = file.read()

    except IOError:
        print(f"Fatal Error: File ({args.filepath}) could not be located or is not readable.")
        exit()

    content = sanitize_input(data)
    sentence_tokens, word_tokens = tokenize_content(content)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='File name of text to summarize')
    parser.add_argument('-l', '--length', default=4, help='Number of sentences to return')
    args = parser.parse_args()

    return args


def sanitize_input(data):
    replace = {
        ord('\f'): ' ',
        ord('\t'): ' ',
        ord('\n'): ' ',
        ord('\r'): None
    }

    return data.translate(replace)


def tokenize_content(content):
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())

    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]
    ]
