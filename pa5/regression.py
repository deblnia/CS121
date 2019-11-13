'''
Linear regression

Deblina Mukherjee 

Main file for linear regression and model selection.
'''

import numpy as np
from sklearn.model_selection import train_test_split
import util


class DataSet(object):
    '''
    Class for representing a data set.
    '''

    def __init__(self, dir_path):
        '''
        Constructor
        Inputs:
            dir_path: (string) path to the directory that contains the
              file
        '''
    	labels, csv = load_numpy_array(dir_path)
    	self.csv = prepend_ones_column(csv)
    	json_full = load_json_file(dir_path)
    	self.name = json_full['name']
    	self.predictor_vars = json_full['predictor_vars']
    	self.dependent_var = json_full['dependent_var']
    	self.training_fraction = json_full['training_fraction']
    	self.seed = json_full['seed']
    	self.train, self.test = train_test_split(csv, 
    							train_size = self.training_fraction,
    							test_size = None)

class Model(object):
    '''
    Class for representing a model.
    '''

    def __init__(self, dataset, pred_vars):
        '''
        Construct a data structure to hold the model.
        Inputs:
            dataset: an dataset instance
            pred_vars: a list of the indices for the columns (of the
              original data array) used in the model.
        '''

        # REPLACE pass WITH YOUR CODE
        #self.R2 = 
        #self.adj_R2 =
        self.dep_var = dataset.csv[:,dataset.dependent_var] 
        self.pred_vars = []+ dataset.csv[:,i] for i in dataset.predictor_vars
        self.beta = linear_regression(self.train)


    def __repr__(self):
        '''
        Format model as a string.
        '''

        # Replace this return statement with one that returns a more
        # helpful string representation
        return "!!! You haven't implemented the Model __repr__ method yet !!!"

    ### Additional methods here


def compute_single_var_models(dataset):
    '''
    Computes all the single-variable models for a dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        List of Model objects, each representing a single-variable model
    '''
    models = []
    for pred in range(len(dataset.predictor_vars))
    models.append(dataset.beta)
    # Replace [] with the list of models
    return models


def compute_all_vars_model(dataset):
    '''
    Computes a model that uses all the predictor variables in the dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object that uses all the predictor variables
    '''

    # Replace None with a model object
    return None


def compute_best_pair(dataset):
    '''
    Find the bivariate model with the best R2 value

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object for the best bivariate model
    '''

    # Replace None with a model object
    return None


def backward_elimination(dataset):
    '''
    Given a dataset with P predictor variables, uses backward elimination to
    select models for every value of K between 1 and P.

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A list (of length P) of Model objects. The first element is the
        model where K=1, the second element is the model where K=2, and so on.
    '''

    # Replace [] with the list of models
    return []



def choose_best_model(dataset):
    '''
    Given a dataset, choose the best model produced
    by backwards elimination (i.e., the model with the highest
    adjusted R2)

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object
    '''

    # Replace None with a model object
    return None


def validate_model(dataset, model):
    '''
    Given a dataset and a model trained on the training data,
    compute the R2 of applying that model to the testing data.

    Inputs:
        dataset: (DataSet object) a dataset
        model: (Model object) A model that must have been trained
           on the dataset's training data.

    Returns:
        (float) An R2 value
    '''

    # Replace 0.0 with the correct R2 value
    return 0.0
