#!/usr/bin/python
import concurrent.futures
import urllib.request
import string
from xml.sax.handler import feature_validation
from functools import partial


URLS = [
    "http://www.foxnews.com/",
    "http://www.cnn.com/",
    "http://europe.wsj.com/",
    "http://www.bbc.co.uk/",
    "http://sapo.pt/",
    "http://microsoft.com/",
    "http://yahoo.com",
]

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print("%r generated an exception: %s" % (url, exc))
        else:
            print("%r page is %d bytes" % (url, len(data)))


def main():
    count_word_ocorrunces("lorem.txt")


def read_chunks(bigfile, chunk_size=1024):
    """Lazy read"""
    while True:
        data = bigfile.read(chunk_size)
        if not data:
            break
        yield data


def count_word_ocorrunces(f):
    word_dic = {}

    i = 0
    with open("Actors.txt") as bigfile:
        piece = partial(bigfile.read, 1024)
        iterator = iter(piece, b"")
        for index, block in enumerate(iterator, start=1):
            # for piece in read_chunks(bigfile):
            for line in block:
                line = (
                    line.translate(
                        line.maketrans(
                            string.punctuation, " " * len(string.punctuation)
                        )
                    )
                    .replace(" " * 4, " ")
                    .replace(" " * 3, " ")
                    .replace(" " * 2, " ")
                    .strip()
                )
                word_dic = word_count(word_dic, line)
    rank_up(word_dic)


def rank_up(word_dic):
    """Get a dicionary Ranks words usage"""
    for word in sorted(word_dic, key=word_dic.get, reverse=True):
        print(word, word_dic[word])


def word_count(word_dic, line):
    """Add words to dicionary if they are not there, adds one to ocorrunce else and returns a list"""
    for word in line.split():
        word = word.lower()
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1
    return word_dic


def create_thread():
    pass


if __name__ == "__main__":
    main()
