# lateshow-joyce-ngari
Its a FLASK API for managing Tv show episodes,guests appearances and ratings

## Features
1. Rates apperarances under a scale of 1-5
2. Tracks show episodes and numbers
3. Manages the guests details like their names and occupation


## files & Contents
1. app/__init__.py
- creates flask application instance,initializes database and migration extensions  and records blueprints.

2. app/routes.py
- defines database tables(episode,guest name,occupation,appearances and ratings).
- it also establishes relationships between models.

3. app/routes.py
- contains  the API endpoints 
- Handels the requiest and response logic

4. Seed.py
- populates database with our initial data
- Reads from the guests.csv file
- creates episodes,guests and appearance.

5. flaskenv
- tracks the database schema 




## prerequisites
- python 3.8 +
- Pip

## Installation
## clone repo
- git clone repo
- cd (project folder)
## Set up the virtual environment
-python  -m venv venv
-source venv/bin/activate
## Install dependencies
- pip install -r requirements.txt
## Initialaize
Run
- flask db init
- flask db migrate -m"initial migaration"
- flask db upgrade
## Seed the data
python seed.py
 
## Run Server
flask run -p 5555

## Author
- joyce ngari

## License
MIT License

