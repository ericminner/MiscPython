#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
#em3373

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. There should be 11
    columns (the "quality" column cannot be used for classificaiton).
    """
    wine = np.genfromtxt(csv_filename, dtype=float, delimiter=';', skip_header=1,usecols=(0,1,2,3,4,5,6,7,8,9,10))   
    return wine   
    
    
    
def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. For example, 0.9 means that the training portion should contain
    90% of the data. You do not have to randomize the rows. Make sure that 
    there is no overlap. 
    """
    train_idx = range(0,int(len(dataset)*ratio))
    test_idx = range(int(len(dataset)*ratio),len(dataset))
    train = dataset[train_idx,:]
    test = dataset[test_idx,:]
    return(train,test)
    
    
def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    return sum(data[:,:]) / len(data)

    
def experiment(ww_train, rw_train, ww_test, rw_test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    ww_centroid = compute_centroid(ww_train)
    rw_centroid = compute_centroid(rw_train)
    correct = 0
    for i in range(len(ww_test)):
        ww_dis = euclidean_distance(ww_test[i],ww_centroid)
        rw_dis = euclidean_distance(ww_test[i],rw_centroid)
        if ww_dis< rw_dis:
            correct +=1
    for i in range(len(rw_test)):
        ww_dis = euclidean_distance(rw_test[i],ww_centroid)
        rw_dis = euclidean_distance(rw_test[i],rw_centroid)
        if rw_dis< ww_dis:
            correct +=1
    return float(correct)/ (len(rw_test)+len(rw_test))
    
def learning_curve(ww_training, rw_training, ww_test, rw_test):
    """
    Perform a series of experiments to compute and plot a learning curve.
    """
    np.random.shuffle(ww_training)
    np.random.shuffle(rw_training)
    accuracy_list = []
    for i in range(1,len(ww_training)+1):
        accuracy_list.append(experiment(ww_training[:i],rw_training[:i],ww_test,rw_test))
    plt.plot(accuracy_list)
    
def cross_validation(ww_data, rw_data, k=5):
    """
    Perform k-fold crossvalidation on the data and print the accuracy for each
    fold. 
    """
    testSize = len(ww_data)//k
    index = 0
    accuracy = []
    for i in range(k):
        if i != k-1:
            ww_test = ww_data[index:index+testSize]
            rw_test = rw_data[index:index+testSize]
            rw_train = np.concatenate((rw_data[:index],rw_data[index+testSize:]))
            ww_train = np.concatenate((ww_data[:index],ww_data[index+testSize:]))
            index += testSize
        else:
            ww_test = ww_data[index:]
            rw_test = rw_data[index:]
            ww_train = ww_data[:index]
            rw_train = rw_data[:index]
        accuracy.append(experiment(ww_train,rw_train, ww_test,rw_test))
    return sum(accuracy)/len(accuracy)
        
        

    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')
    
    # Uncomment the following lines for step 2: 
    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    print (experiment(ww_train, rw_train, ww_test, rw_test))

    # Uncomment the following lines for step 3
    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    learning_curve(ww_train, rw_train, ww_test, rw_test)
    
    # Uncomment the following lines for step 4:
    k = 10
    acc = cross_validation(ww_data, rw_data,k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
