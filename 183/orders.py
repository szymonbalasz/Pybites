import os
from urllib.request import urlretrieve

import pandas as pd
import datetime

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    
    return pd.read_excel(excel, sheet_name="SalesOrders")


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    
    df['Year'] = pd.DatetimeIndex(df['OrderDate']).year
    return df.groupby(by=['Year', 'Region']).sum()['Total']


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    return (df.groupby(by=['Rep']).sum()['Total'].idxmax(), df.groupby(by=['Rep']).sum()['Total'].max())


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    return (df.groupby(by=['Item']).sum()['Units'].idxmax(), df.groupby(by=['Item']).sum()['Units'].max())
