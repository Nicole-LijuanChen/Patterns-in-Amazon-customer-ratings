#!/usr/bin/env python3

import numpy as np
import pandas as pd
import json
from typing import Dict, List


def parse_json(json_string:str) -> any:
    """Returns a python dictionary from a string encoding a json dictionary.

    Parameters
    ----------
    json_string (str): a string encoding a json dictionary

    Returns
    -------
    {k,v}: a python dictionary from a json encoded string

    Example
    -------
    >>> parse_json(u'{"Jane": "2"}')
    {"Jane": "2"}
    """
    res = None
    try:
        res = json.loads(json_string)
    except:
        pass
    return res

def map_to_json(rdd):
    '''Map each RDD item to JSON
    '''
    return rdd.map(parse_json)


def clean_data(rdd, category):
    '''Returns a pandas dataframe from a rdd, 
        filter the ratings that is not verified.
        dataframe contains year, ratings, and category name.
    
    Parameters
    ---------- 
    rdd:  a row data , type is rdd
    category (str) : category name ,such as beauty, books...
    
    Returns
    -------
    pandas dataframe: filter the ratings that is not verified,
                      contains three columns values:
                      year, ratings, and category name.
    '''
    overall = (rdd.filter(lambda row: row['verified'])
                .map(lambda row: row['overall'])
                )
    years   = (rdd.filter(lambda row: row['verified'])
                    .map(lambda row: row['reviewTime'])
                    .map(lambda row: row.split(","))
                    .map(lambda row: int(row[1]))
                )
    lengh = overall.count()
    category_list = [str(category)]*lengh
    df = pd.DataFrame({'ratings': overall.collect(),
                        'years': years.collect(),
                        'category': category_list 
                        })
    return df
def avg_by_year(df):
    """calculate the average ratings and standard deviations by year

    Parameters
    ----------
    df (pandas dataframe): a dataframe cotanis all ratings 

    Returns
    -------
    by_year_df: a dataframe contains year,the average ratings by year,
                and tandard deviations by year
    """
    #calculate the average ratings by year
    avg_by_year_df = df.groupby('years')['ratings'].mean()
    
    #calculate the std ratings by year
    std_by_year_df = df.groupby('years')['ratings'].std()
    #convert Series to pd.dataframe
    avg_by_year_df = pd.DataFrame({'year': avg_by_year_df.index.tolist(),
                  'avg_ratings': avg_by_year_df,
                   'std': std_by_year_df})
    
    #reset index
    avg_by_year_df.reset_index(drop=True, inplace=True)
    
    return avg_by_year_df



def ratings_mean(df):
    """calculate the ratings mean from the given dataframe
    parameters
    ----------
    df (pandas dataframe): a dataframe cotanis all ratings 

    Returns
    -------
    mean(float): mean of ratings, keep 4 decimal
    """
    mean_value = df['ratings'].mean()
    mean_value = round(mean_value,4) 
    return mean_value

def ratings_std(df):
    """calculate standard deviation of ratings from the given dataframe
    parameters
    ----------
    df (pandas dataframe): a dataframe cotanis all ratings 

    Returns
    -------
    standard deviation(float): standard deviation of ratings, keep 4 decimal
    """
    std_value = df['ratings'].std()
    std_value = round(std_value,4) 
    return std_value

