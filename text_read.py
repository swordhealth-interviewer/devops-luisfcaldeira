#!/usr/bin/python
import concurrent.futures

# import urllib.request
import string
from itertools import islice

URLS = [
    "http://www.foxnews.com/",
    "http://www.cnn.com/",
    "http://europe.wsj.com/",
    "http://www.bbc.co.uk/",
    "http://sapo.pt/",
    "http://microsoft.com/",
    "http://yahoo.com",
]

file_lines = []


def main():
    count_word_occurrences("Actors.txt")


def read_chunks(bigfile, offset, chunk_size=1024):
    """Lazy read"""
    while True:
        data = bigfile.read(chunk_size)
        if not data:
            break
        yield data


def count_word_occurrences(bigfile):
    word_dic = {}

    with open("Actors.txt") as bigfile:

        file_lines = bigfile.readlines()

        file_lines = [
            line.translate(
                line.maketrans(string.punctuation, " " * len(string.punctuation))
            )
            for line in file_lines
        ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
        future_lines = {
            e.submit(word_count, word_dic, line): line for line in file_lines
        }
        for future in concurrent.futures.as_completed(future_lines):
            line = future_lines[future]
            try:
                data = future.result()
            except Exception as exc:
                print("%r generated an exception: %s" % (line, exc))

        rank_up(word_dic)


def rank_up(word_dic):
    """Get a dicionary Ranks words usage"""
    for word in sorted(word_dic, key=word_dic.get, reverse=True):
        print(word, word_dic[word])


def word_count(word_dic, line):
    """Add words to dicionary if they are not there, adds one to occurrence else and returns a list"""
    for word in line.split():
        word = word.lower()
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1
    return word_dic


def count_lines(f):
    count = 0
    for i in f:
        count += 1
    return count


def read_n_lines_from_file(f, n_lines):
    return [[x.strip() for x in islice(f, n_lines)]]


if __name__ == "__main__":
    main()
