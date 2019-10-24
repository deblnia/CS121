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

def calc_idf(docs): 
    #computes tf and idf 
    numer = len(docs)
    uniquewords = []
    idf = dict()
    for doc in docs: 
        uniquewords = count_tokens(doc)
        for key,value in uniquewords: 
            idf[key] = idf.get(key, 0)+1
    for value in idf.values(): 
        value = math.log(numer/value)
    return idf

def calc_tf(docs): 
    '''
    docstring
    '''
    # loop through each doc calc tf scores for each doc using count_token 
    # multiply by idf 
    # sort using sort count pairs and then slice and return 
    # sort list retrned from count_tokens and use first 
    # do it in one loop 
    # append intermediate lists into return value  
    # list of dictionaries (key, value)   
    # change values in dictionary 
    tf_full = []
    for doc in docs: 
        if len(doc) == 0:
            tf_full.append({})  
        else:
            sorted_count = sort_count_pairs(count_tokens(doc))
            max_tf = sorted_count[0][1]
            tf_doc = {}
            for k,v in sorted_count: 
                tf_doc[k] = 0.5+0.5*(v/max_tf)
            tf_full.append(tf_doc) 
    return tf_full

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
    tf = calc_tf(docs)
    idf = calc_idf(docs)
    tf_idf = []
    for doc in tf:
        doc_tfidf = {}
        for term,tf_2 in doc.items(): 
            doc_tfidf[term] = tf_2 * idf[term]
        tf_idf.append(doc_tfidf) 
    for dic in tf_idf:
        most_sal = []
        final = []
        for key,v in dic.items():
            most_sal.append((key,v))
        sorted_sal = sort_count_pairs(most_sal)
    final.append(find_top_k(sorted_sal,k))
    return final 
