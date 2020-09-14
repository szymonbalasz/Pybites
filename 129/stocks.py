import requests
import json
from collections import defaultdict

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    
    if cap == "n/a":
        return 0
    
    cap = cap.replace("$", "")

    if "M" in cap:
        cap = cap.replace("M", "")
        return float(cap)
    
    elif "B" in cap:
        cap = cap.replace("B", "")
        return float(cap) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    
    cap_values = []

    for stock in data:
            if industry in stock["industry"]:
                cap_values.append(_cap_str_to_mln_float(stock["cap"]))

    return round(sum(cap_values), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    
    highest = (0, '')
    for stock in data:
        stock_cap = _cap_str_to_mln_float(stock["cap"])
        if stock_cap > highest[0]:
            highest = (stock_cap, stock["symbol"])
    return highest[1]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    
    sectors = defaultdict(lambda: 0)
    for stock in data:
        if stock["sector"] == "n/a":
            continue
        sectors[stock["sector"]] += 1

    return (max(sectors, key=sectors.get), min(sectors, key=sectors.get))
