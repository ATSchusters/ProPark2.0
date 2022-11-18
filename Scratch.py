from models import Deck
import csv
import database as db

# inserting the data into the database need to start a session
session = Session(engine)
cri_deck = Deck(name="CRI_Deck", coord_x=35.30921329 , coord_y=-80.74347472, commuter=True, resident=True,
                staff=True)
cri_deck

"""
with open('decksdata.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['name'] = Deck(name=row['name'], coord_x=row['coord_x'], coord_y=row['coord_y'], commuter=row['commuter'], resident=row['resident'], staff=row['staff'])
        print(row['name'])
"""
