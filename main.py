'''
Extract information from the Riot Games API using Python
Author: Viraj Vaitha
Date: 18/12/2021
'''
from pandas.core.frame import DataFrame
import requests
import pandas as pd
import os

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
}

headers["X-Riot-Token"] = os.environ.get('X-Riot-Token')

# Parameters
params = {'size': '10', 'startIndex': '0'} 

# Function to use API
def return_leaderboard(headers: dict, params: dict) -> pd.DataFrame:
    """
    Function uses requests to the GET http request/response provided by Riot Games API.

    API Key provided in header prevents 400 status code errors

    Params control how many users are shown from the leaderboard and from what position they're shown
    """
    resp = requests.request("GET",
                           url =  f"https://eu.api.riotgames.com/val/ranked/v1/leaderboards/by-act/a16955a5-4ad0-f761-5e9e-389df1c892fb",
                           headers=headers,
                           params=params)

    # Response as json
    json_data = resp.json()
    
    # Return response as dataframe
    df = pd.DataFrame.from_dict(json_data['players'])

    
    print(df.head(int(params["size"])))
    return df


df = return_leaderboard(headers, params)

