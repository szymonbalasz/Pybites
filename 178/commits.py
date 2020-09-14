from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

import re

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    result = defaultdict(lambda: 0)

    with open(commit_log) as f:
        data = f.read().splitlines()

    for line in data:
        date = parse(re.search(r"Date:   (.*?) \| ", line).group(1))
        if year and year != date.year:
            continue
        key = '{}-{:02}'.format(date.year, date.month)

        insertions = re.search(r" (\d*?) insertion", line)
        deletions = re.search(r" (\d*?) deletion", line)

        changes = 0

        if insertions:
            changes += int(insertions.group(1))
        if deletions:
            changes += int(deletions.group(1))

        result[key] += changes

    return (str(min(result, key=result.get)), str(max(result, key=result.get)))