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
def clean_tweets(tweets, entity_key):
    '''
    Indexes into the dictionary for a given entity_key pair. 
    Input: 
        tweets: a list of tweets 
        entity_key: a tuple of entities and key 
    Returns: a list of the desired entity and key 
    '''
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
    top_k = find_top_k(good_tweets,k)
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
    Works through all the pre-processing steps listed in the assignment 
    Inputs: 
        tweet: one tweet (dictionary)
        stopwords: a boolean (True/False), specifying whether stopwords 
                    should be removed 
    Returns: a processed tweet (a list of words) 
    '''
    words = tweet['abridged_text'].split()
    list_lower = []
    for word in words: 
        list_lower.append(word.lower())
    punc = []
    if stopwords == True:
        for word in list_lower: 
            word = word.strip(PUNCTUATION)
            if word.startswith(STOP_PREFIXES) == False: 
                punc.append(word)
        stopw = []
        for word in punc: 
            if word not in STOP_WORDS:
                if len(word) != 0:  
                    stopw.append(word)
        return stopw
    else: 
        for word in list_lower: 
            word = word.strip(PUNCTUATION)
            if word.startswith(STOP_PREFIXES) == False: 
                if len(word) != 0: 
                    punc.append(word)
        return punc


def gen_n_grams(tweet,k): 
    '''
     Generates ngrams of length k given a tweet 
     Input: 
        tweet: a single tweet 
        k: an integer 
    Returns: a list of lists of ngrams  
    '''
    input_list = preprocess(tweet, True)
    ngrams = []
    for i in range(len(input_list)-(k-1)):
        ngrams.append(tuple(input_list[i:i+k]))
    return ngrams  


def find_top_k_ngrams(tweets, n, k):
    '''
     Find k most frequently occurring n-grams across all tweets

     Inputs:
         tweets: a list of tweets
         n: integer
        k: integer

     Returns: list of key/value pairs
    '''
    top_k = []
    for tweet in tweets: 
        ngrams = gen_n_grams(tweet,k)
        top_k.append(find_top_k(ngrams,n))
    return top_k[:k]


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
    min_ngrams = []
    for tweet in tweets:
        ngrams = gen_n_grams(tweet,k)
        min_ngrams.append(find_min_count(ngrams,min_count))
    return min_ngrams


def find_most_salient_ngrams(tweets, n, k):
    '''
     Find k most salient n-grams for each tweet.

     Inputs:
         tweets: a list of tweets
         n: integer
         k: integer

     Returns: list of list of strings
    '''
    for tweet in tweets:
        ngrams = []
        input_list = preprocess(tweet, False)
        for i in range(len(input_list)-(n-1)):
            ngrams.append(tuple(input_list[i:i+n]))
    sal_ngrams = []
    sal_ngrams.append(find_most_salient(ngrams,k))
    return []
