from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = 'A SOOCRET KOO'
db = SQLAlchemy(app)

from application import routes

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import getenv

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI') 
# app.config['SECRET_KEY'] = "my-secret"

# db = SQLAlchemy(app)


# from application import routes
