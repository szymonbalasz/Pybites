import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df.nlargest(1, "Calories").values[0][1]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    
    if excl_drinks:
        df = df[(df.Category != 'Coffee & Tea') & (df.Category != 'Beverages')]
    df = df[df.Calories > 0]
    df['Ratio'] = (df['Protein']/df['Calories'])
    return df.nlargest(5, 'Ratio').Item.values
