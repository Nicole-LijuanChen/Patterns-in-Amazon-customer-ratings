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

def clean_data(rdd, category):
    '''Returns a pandas dataframe from a rdd, 
        filter the ratings that is not verified.
        dataframe contains year, ratings, and category.
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


