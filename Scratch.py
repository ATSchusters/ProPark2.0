from models import Deck
import csv
import database as db

# inserting the data into the database need to start a session
i = 0
with open('decksdata.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = Deck(name=row['name'], coord_x=row['coord_x'], coord_y=row['coord_y'], commuter=row['commuter'], resident=row['resident'], staff=row['staff'])
        db.session.add(x)
db.session.commit()
