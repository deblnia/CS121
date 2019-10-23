'''
Analyzing Election Tweets

YOUR NAME

Algorithms for efficiently counting and sorting distinct `entities` or
unique values, are widely used in data analysis. Functions to
implement: count_tokens, find_top_k, find_min_count, find_frequent
'''

import math

from util import sort_count_pairs

def count_tokens(tokens):
    '''
    Counts each distinct token (item or entity) in a list of tokens

    Inputs:
        tokens: list of tokens (must be hashable/comparable)

    Returns: list (token, number of occurrences).
    '''

    # Your code for Task 1.1 goes here
    freq = dict() 
    for key in tokens: 
        if key in freq: 
            freq[key] += 1
        else: 
            freq[key] = 1
    return list(freq.items())

def find_top_k(tokens, k):
    '''
    Find the k most frequently occurring tokens

    Inputs:
        tokens: list of tokens (must be hashable/comparable)
        k: a non-negative integer

    Returns: sorted list of the top k tuples

    '''

    # Error checking (DO NOT MODIFY)
    err_msg = "In find_top_k, k must be a non-negative integer"
    assert k >= 0, err_msg

    # Your code for Task 1.2 goes here
    counted = count_tokens(tokens)
    sorted_tokens = sort_count_pairs(counted) 
    return sorted_tokens[:k]    


def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur at least min_count times

    Inputs:
        tokens: a list of tokens (must be hashable/comparable)
        min_count: integer

    Returns: sorted list of tuples
    '''

    # Your code for Task 1.3 goes here
    tokens = count_tokens(tokens)
    good_vals = []
    for key, value in tokens:
        if value >= min_count: 
            good_vals.append((key,value))
    good_vals = sort_count_pairs(good_vals)
    return good_vals
    # Replace return value with an appropriate value

def calc_tf(document): 
    '''
    docstring
    '''
    numerator = count_tokens(document)
    denominator = find_top_k(document, 1)[0][1]
    tf = list()
    for key,value in numerator: 
        tf.append(0.5+0.5*value/denominator)
    return tf 

def calc_idf(corpus): 
    #computes tf and idf 
    numer = len(corpus)
    count_list = []
    denom = dict()
    idf = []
    for lists in corpus: 
        count_list.append(count_tokens(lists))
    for token in count_list: 
        for word in token: 
            if word in denom: 
                denom[word] += 1
            else: 
                denom[word] = 1
    for key,value in denom.items():
        print(value,"value")
        idf.append(math.log*(numer/value)) 
    return idf


def find_most_salient(docs, k):
    '''
    Find the k most salient tokens in each document

    Inputs:
        docs: a list of lists of tokens
        k: integer

    Returns: list of sorted list of tokens
     (inner lists are in decreasing order of tf-idf score)
    '''

    # Your code for Task 1.4 goes here
    d = dict()
    for lists in docs:
        for words in lists: 
            d[words] = calc_tf(lists)*calc_idf(docs)
    sort_d = sorted((term,tf_idf) for (term,tf_idf) in d.items())  

    # Replace return value with an appropriate value
    return sort_d[:k]
