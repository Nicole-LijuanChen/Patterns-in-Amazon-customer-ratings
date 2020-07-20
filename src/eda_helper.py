#!/usr/bin/env python3

import numpy as np
import pandas as pd
import json
from typing import Dict, List
from geotext import GeoText


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


def parse_country(text:str) -> dict:
    res = GeoText(text).country_mentions
    return res if res != {} else np.nan

def parse_city(text:str) -> dict:
    res = GeoText(text).cities
    return res if res else np.nan

