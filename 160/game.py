import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = {}


    with open(BATTLE_DATA) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            defeat_mapping[row['Attacker']] = [
                k for k, v in row.items() if v == 'win']

    return defeat_mapping


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    
    try:
        assert player1 in defeat_mapping
        assert player2 in defeat_mapping
    except:
        raise ValueError

    if player1 == player2:
        return "Tie"

    elif player2 in defeat_mapping[player1]:
        return player1

    else:
        return player2