from app import create_app, db
from app.models import Episode, Guest, Appearance
import csv
from datetime import datetime

app =create_app()

def parse_date(show_date) :
    try:
        return datetime.strptime(show_date, "%m/%d/%y").strftime("%-m/%-d/%y")
    except ValueError:
        try:
            return datetime.strptime(show_date, "%m/%d/%Y").strftime("%-m/%-d/%y")
        except ValueError:
            return show_date

with app.app_context():
    db.drop_all()
    db.create_all()

    episodes= {}
    guests ={}
    
    with open('seeds/guests.csv', 'r') as f:
        reader= csv.DictReader(f)
        for row in reader:
            if not row['Show'] or row['Show'] == 'NA':
                continue
                
            show_date = parse_date(row['Show'])
            if show_date not in episodes:
                episode = Episode(date=show_date, number=len(episodes)+1)
                db.session.add(episode)
                episodes[show_date] = episode
            
            guest_name = row['Raw_Guest_List'].split(',')[0].strip()
            if guest_name not in guests:
                guest= Guest(
                    name=guest_name,
                    occupation=row['GoogleKnowlege_Occupation'] or 'Unknown'
                )
                db.session.add(guest)
                guests[guest_name] = guest
    
    db.session.commit()
    print(f"Seeded {len(episodes)} episodes and {len(guests)} guests!")