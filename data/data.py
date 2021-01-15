#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:32:20 2021

@author: caiyang
"""
"""
    File to load dataset based on user control from main file
"""

from data.TSP import TSPDataset


def LoadData(DATASET_NAME):
    """
        This function is called in the main.py file 
        returns:
        ; dataset object
    """

    # handling for TSP dataset
    if DATASET_NAME == 'TSP':
        return TSPDataset('data/TSP/')
    else:
        raise NotImplementedError