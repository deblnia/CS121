'''
Analyzing Election Tweets

YOUR NAME

Use the algorithms in the previous part on the dataset of
tweets. Every collection of tweets is represented as a JSON
file. Functions to implement:
  find_top_k_entities,
  find_min_count_entities,
  find_top_k_ngrams,
  find_min_count_ngrams,
  find_most_salient_ngrams
'''

import unicodedata
import sys

from basic_algorithms import find_top_k, find_min_count, find_most_salient

##################### DO NOT MODIFY THIS CODE #####################

def keep_chr(ch):
    '''
    Find all characters that are classifed as punctuation in Unicode
    (except #, @, &) and combine them into a single string.
    '''

    return unicodedata.category(ch).startswith('P') and \
        ch not in ("#", "@", "&")

PUNCTUATION = " ".join([chr(i) for i in range(sys.maxunicode)
                        if keep_chr(chr(i))])

# When processing tweets, ignore these words
STOP_WORDS = ["a", "an", "the", "this", "that", "of", "for", "or",
              "and", "on", "to", "be", "if", "we", "you", "in", "is",
              "at", "it", "rt", "mt", "with"]

# When processing tweets, words w/ a prefix that appears in this list
# should be ignored.
STOP_PREFIXES = ("@", "#", "http", "&amp")


#####################  MODIFY THIS CODE #####################

# Task 1
def find_top_k_entities(tweets, entity_key, k):
    '''
    Find the K most frequently occuring entitites

    Inputs:
        tweets: a list of tweets
        entity_key: a pair ("hashtags", "text"),
          ("user_mentions", "screen_name"), etc
        k: integer

    Returns: list of entity, count pairs
    '''

    # Your code for Task 2.1 goes here
    # Replace None with appropriate value
    return None


def find_min_count_entities(tweets, entity_key, min_count):
    '''
    Find the entitites that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        entity_key: a pair ("hashtags", "text"),
          ("user_mentions", "screen_name"), etc
        min_count: integer

    Returns: list of entity, count pairs
    '''

    # Your code for Task 2.2 goes here
    # Replace None with appropriate value
    return None


def find_top_k_ngrams(tweets, n, k):
    '''
    Find k most frequently occurring n-grams across all tweets

    Inputs:
        tweets: a list of tweets
        n: integer
        k: integer

    Returns: list of key/value pairs
    '''

    # Your code for Task 2.3 goes here
    # Replace None with appropriate value
    return None


def find_min_count_ngrams(tweets, n, min_count):
    '''
    Find n-grams that occur at least min_count times across all
    tweets.

    Inputs:
        tweets: a list of tweets
        n: integer
        min_count: integer

    Returns: list of ngram/value pairs
    '''

    # Your code for Task 2.4 goes here
    # Replace None with appropriate value
    return None


def find_most_salient_ngrams(tweets, n, k):
    '''
    Find k most salient n-grams for each tweet.

    Inputs:
        tweets: a list of tweets
        n: integer
        k: integer

    Returns: list of list of strings
    '''

    # Your code for Task 2.5 goes here
    # Replace None with appropriate value
    return None
