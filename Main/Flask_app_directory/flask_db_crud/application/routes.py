
from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

zelda = Games(name="zelda")
db.session.add(zelda)
db.session.commit()

goldeneye = Games(name='goldeneye')
db.session.add(goldeneye)
db.session.commit()

zelda = Games.query.first()
db.session.delete(zelda)
db.session.commit

zelda = Games.query.first()
zelda.name = "zelda two" 
db.session.commit()

