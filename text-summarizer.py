import argparse

from collections import defaultdict

from heapq import nlargest

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

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
    sentence_ranks = score_tokens(word_tokens, sentence_tokens)

    return summarize(sentence_ranks, sentence_tokens, args.length)


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


def score_tokens(filterd_words, sentence_tokens):
    word_freq = FreqDist(filterd_words)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]

    return ranking


def summarize(ranks, sentences, length):
    if int(length) > len(sentences):
        print("Error, more sentences requested than available. Use --l (--length) flag to adjust.")
        exit()

    indices = nlargest(length, ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indices)]

    return " ".join(final_sentences)


if __name__ == "__main__":
    print(main())
