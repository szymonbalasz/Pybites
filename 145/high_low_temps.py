from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value
         
    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """

    df = pd.read_csv(DATA_FILE)
    df['Date'] = pd.to_datetime(df['Date'], errors='ignore')
    df = df[~((df.Date.dt.month == 2) & (df.Date.dt.day == 29))]
    df['Data_Value'] = df['Data_Value'].map(lambda x: int(x)/10)
    df['dayofyear'] = df['Date'].dt.dayofyear

    record_days = {}


    for _ in range(1, 366):
        mini = df.loc[df[(df['dayofyear'] == _) & (df['Element'] == 'TMIN')].Data_Value.idxmin()]
        maxi = df.loc[df[(df['dayofyear'] == _) & (df['Element'] == 'TMAX')].Data_Value.idxmax()]

        if mini.Date.year == 2015:
            record_days[_] = STATION(mini.ID, mini.Date.date(), mini.Data_Value)

        if maxi.Date.year == 2015:
            record_days[_] = STATION(maxi.ID, maxi.Date.date(), maxi.Data_Value)

    return (record_days[max(record_days, key=lambda x: record_days[x].Value)],
            record_days[min(record_days, key=lambda x: record_days[x].Value)])



