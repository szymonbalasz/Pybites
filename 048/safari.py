import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS, 'r') as file:
        lines = file.readlines()

    day = 13
    result = {f'02-{day} ': []}
    for line in lines:
        if not f'02-{day}' in line:
            day += 1
            result[f'02-{day} '] = []
        if 'Python' in line and 'sending to slack channel' in (lines[lines.index(line)+1]):
            result[f'02-{day} '].append(PY_BOOK)
        elif 'sending to slack channel' in (lines[lines.index(line)+1]):
            result[f'02-{day} '].append(OTHER_BOOK)

    result = {k: v for (k, v) in result.items() if not v == []}
    for k, v in result.items():
        print(f'{k}{"".join(v).strip()}')

