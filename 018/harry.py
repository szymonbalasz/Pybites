import os
import urllib.request

import re
from collections import defaultdict

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    sw = (open(stopwords_file, "r").read().split("\n"))
    hp = open(harry_text, "r", encoding="UTF-8").read()
    text = (re.sub(r'[^a-zA-Z\s]', '', hp.lower())).split()
    d = defaultdict(int)
    for word in text:
        if not word in sw:
            d[word] += 1
    m = max(d, key=d.get)
    return (m, d[m])
