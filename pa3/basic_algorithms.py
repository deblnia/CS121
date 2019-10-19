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
    # Replace return value with an appropriate value
    return []


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
    # Replace return value with an appropriate value
    return []


def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur at least min_count times

    Inputs:
        tokens: a list of tokens (must be hashable/comparable)
        min_count: integer

    Returns: sorted list of tuples
    '''

    # Your code for Task 1.3 goes here
    # Replace return value with an appropriate value
    return []


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
    # Replace return value with an appropriate value
    return []
