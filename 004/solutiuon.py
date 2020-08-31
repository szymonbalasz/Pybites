import os
import re
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)
with open(tempfile) as f:
    content = f.read().lower()

TAG_HTML = re.compile(r'<category>([^<]+)</category>')


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = TAG_HTML.findall(content)
    return Counter(tags).most_common(n)
