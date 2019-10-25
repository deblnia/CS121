'''
Analyzing Election Tweets

Deblina Mukherjee 

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

# Task 1n
def clean_tweets(tweets, entity_key):
    hashtags,text = entity_key
    first_iteration = []
    second_iteration = []
    for tweet in tweets: 
        first_iteration.append(tweet['entities'][hashtags])
    for i in first_iteration: 
        for x in i: 
            second_iteration.append(x[text].lower())
    return second_iteration

    

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
    good_tweets = clean_tweets(tweets, entity_key)

    # Your code for Task 2.1 goes here
    top_k = find_top_k(good_tweets,k)
    # Replace None with appropriate value
    return top_k 


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
    good_tweets = clean_tweets(tweets,entity_key)
    min_k = find_min_count(good_tweets,min_count)
    return min_k

def preprocess(tweet, stopwords): 
    '''
    docstring
    '''
     
    words = tweet['abridged_text'].split()
    list_lower = []
    for word in words: 
        list_lower.append(word.lower())
    punc = []
    for word in list_lower: 
        word = word.strip(PUNCTUATION)
        if word.startswith(STOP_PREFIXES) == False: 
            punc.append(word)
        return punc
    stopw = []
    if stopwords == True: 
        for word in punc: 
            if word not in STOP_WORDS: 
                 stopw.append(word)
        return stopw



def gen_n_grams(tweets,n): 
     '''
     docstring
     '''
     bases = tweets

     last = bases
     current = []
     for i in range(k-1):
         for b in bases:
             for l in last:
                 current.append(l+b)
         last = current
         current= []
     return last

def count_n_grams(k,tweets):

    rv = {}
    for i in range(0, len(tweets)-k+1):
        subseq = tweets[i:i+k]
        v = rv.get(subseq, 0)
        rv[subseq] = v + 1
    return list(rv.items())


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
