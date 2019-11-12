'''
Analyzing Election Tweets

<<<<<<< HEAD
Deblina Mukherjee
=======
YOUR NAME
>>>>>>> 772604324d9e6fbf8e76ecb03659b77d09955de0

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
<<<<<<< HEAD
    freq = dict() 
    for key in tokens: 
        if key in freq: 
            freq[key] += 1
        else: 
            freq[key] = 1
    return list(freq.items())
=======

    # Your code for Task 1.1 goes here
    # Replace return value with an appropriate value
    return []
>>>>>>> 772604324d9e6fbf8e76ecb03659b77d09955de0


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

<<<<<<< HEAD
    counted = count_tokens(tokens)
    sorted_tokens = sort_count_pairs(counted) 
    return sorted_tokens[:k]    
=======
    # Your code for Task 1.2 goes here
    # Replace return value with an appropriate value
    return []
>>>>>>> 772604324d9e6fbf8e76ecb03659b77d09955de0


def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur at least min_count times

    Inputs:
        tokens: a list of tokens (must be hashable/comparable)
        min_count: integer

    Returns: sorted list of tuples
    '''
<<<<<<< HEAD
    tokens = count_tokens(tokens)
    good_vals = []
    for key, value in tokens:
        if value >= min_count: 
            good_vals.append((key,value))
    good_vals = sort_count_pairs(good_vals)
    return good_vals


def calc_idf(docs):
    '''
    Calculates the IDF scores for a given corpus. 

    Inputs: 
        docs: a list of lists (must be hashable/comparable)

    Returns: a dictionary with the token as key and the IDF score as value
    ''' 
    numer = len(docs)
    uniquewords = []
    idf = dict()
    for doc in docs: 
        uniquewords = count_tokens(doc)
        for key,value in uniquewords: 
            idf[key] = idf.get(key, 0)+1
    for key,value in idf.items(): 
        idf[key] = math.log(numer/value)
    return idf


def calc_tf(docs): 
    '''
    Calculates TF scores per document for a corpus of documents. 

    Inputs: 
        docs: a list of lists (must be hashable/comparable)
    Returns: a list of dictionaries where each dictionary is a document 
                containing the token as key and TF score as value  
    ''' 
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
=======

    # Your code for Task 1.3 goes here
    # Replace return value with an appropriate value
    return []
>>>>>>> 772604324d9e6fbf8e76ecb03659b77d09955de0


def find_most_salient(docs, k):
    '''
    Find the k most salient tokens in each document

    Inputs:
        docs: a list of lists of tokens
        k: integer

    Returns: list of sorted list of tokens
     (inner lists are in decreasing order of tf-idf score)
    '''
<<<<<<< HEAD
    tf = calc_tf(docs)
    idf = calc_idf(docs)
    tf_idf = []
    for doc in tf:
        doc_tfidf = {}
        for term,tf_2 in doc.items(): 
            doc_tfidf[term] = tf_2 * idf[term]
        tf_idf.append(doc_tfidf)
    final = []
    for dic in tf_idf:
        doc = [] 
        sorting = sort_count_pairs(dic.items())[:k]
        for lists in sorting: 
            doc.append(lists[0])
        final.append(doc)
    return final
=======

    # Your code for Task 1.4 goes here
    # Replace return value with an appropriate value
    return []
>>>>>>> 772604324d9e6fbf8e76ecb03659b77d09955de0
