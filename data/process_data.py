"""This file is used to convert raw data into clean data to be used for analysis
Cleaning steps include:
    - creating player_id column
    - creating country_id column
    - normalising the units of 'value' and 'wage' columns
    - imputing the average 'value' or 'wage for players with missing data
    - reordering and dropping uncessary columns
"""
import pandas as pd
import numpy as np

import logging


def clean_money_values(money):
    """Converts all €M and €K values to base units of € and converts to int
    
        Parameters: money (str)
            From 'value' or 'wage' columns
        
        Returns: (int)
            Integer converted into consistent base units of €
    """
    
    suffix = money[-1]
    if suffix == "M":
        money =  float(money[1:-1]) * 1000000
    elif suffix == "K":
        money =  float(money[1:-1]) * 1000
    else:
        #if the value or wage is €0, return nan
        return np.nan
    
    return int(money)
    
def clean_raw_df(df):
    """Cleans the raw data
    
        Parameters: df (pandas dataframe)
            Raw data from 'raw' data folder
        
        Returns: final_df (pandas dataframe)
            Clean dataframe with no missing values or incorrect datatypes

    """

    assert df.isnull().sum().all() == 0, "There is missing data"
    assert df['link'].nunique() == len(df), "Duplicate data"

    #-----------------
    #create player_id
    #-----------------
    df['player_id'] = df['link'].apply(lambda x: x.split('/')[4])
    assert df['player_id'].nunique() == len(df), "Non-unique player id"

    #-----------------
    #create country_id
    #-----------------
    df['country_id'] = df['country_link'].apply(lambda x: x.split('=')[-1])

    #-----------------
    #clean value and wage column
    #-----------------
    df['value_clean'] = df['value'].apply(clean_money_values)
    df['wage_clean'] = df['wage'].apply(clean_money_values)

    #imput na values with the mean for that overal rating
    df['value_clean'] = df.groupby('overall_rating')['value_clean'].transform(lambda x: x.fillna(x.mean()))
    df['wage_clean'] = df.groupby('overall_rating')['wage_clean'].transform(lambda x: x.fillna(x.mean()))

    #if there are still nan, replace with 0 (these tend to be very low ranked players)
    df[['value_clean','wage_clean']] = df[['value_clean','wage_clean']].fillna(0)

    #-----------------
    #Reorder columns for final dataframe
    #-----------------
    keep_cols = ['player_id','name', 'age', 'overall_rating','potential',
                 'likes', 'dislikes','followers','value_clean','wage_clean']

    ATTRIBUTES=['Crossing','Finishing','Heading Accuracy', 'Short Passing','Volleys',
                'Dribbling','Curve','FK Accuracy','Long Passing','Ball Control','Acceleration',
                'Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina',
                'Strength','Long Shots','Aggression','Interceptions','Positioning','Vision',
                'Penalties','Composure','Marking','Standing Tackle','Sliding Tackle','GK Diving',
                'GK Handling','GK Kicking','GK Positioning','GK Reflexes']


    final_df = df[keep_cols + ATTRIBUTES]
    assert final_df.isnull().sum().all() == 0 

    return final_df


if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)

    df = pd.read_csv("0. raw/data.csv")

    logging.info('Cleaning data...')

    clean_df = clean_raw_df(df)

    logging.info('Dataframe cleaning completed')

    #save to processed data folder
    pd.DataFrame(clean_df).to_csv("1. processed/data_clean.csv",index=False,encoding='utf-8-sig')
    
    logging.info("File successfully saved in 'processed' folder")

