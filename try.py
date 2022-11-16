from flask import Flask, render_template, url_for, session, logging, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy


def create_app(config_file='settings.py'):
	app = Flask(__name__) # That will work like a placeholder for our app 
	app.config.from_pyfile(config_file)
	return app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

if __name__ == '__main__':
	app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
	db.create_all()
	app.run(debug = True)