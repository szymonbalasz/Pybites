import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
import re

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    result = {}
    with open(stats, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            if 'None' in row.values(): continue
            bite = re.findall(r'Bite (\d+)\.', row['Bite'])
            if bite: result[bite[0]] = float(row['Difficulty'])
    
    return sorted(result, key=result.get, reverse=True)[0:N]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
