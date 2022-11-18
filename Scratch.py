from models import Deck
import csv
import database as db

# inserting the data into the database need to start a session

with open('decksdata.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['name'] = Deck(name=row['name'], coord_x=row['coord_x'], coord_y=row['coord_y'], commuter=row['commuter'], resident=row['resident'], staff=row['staff'])
        print(row['name'])

