import sys
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

from app.models import City, db

app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
db.init_app(app)

@app.route('/')
def index():
    return render_template("homepage.html")


@app.route('/city_page', methods=['GET', 'POST'])
def city():
    # destination = get key from get request
    destination = request.form['destination']
    city = City.query.filter_by(destination=destination).first()
    return render_template("city_page.html", city=city)

@app.route('/city_event_page/<destination>', methods=['GET'])
def city_page(destination):
    destination = City.query.filter_by(destination=destination).first()
    return render_template("city_event_page.html", events=destination.events, city_event_destination=destination)

@app.route('/testing')
def testing_page():
    """ testing page"""
    return render_template("index.html")

def main():
    if len(sys.argv) == 2:
        print(sys.argv)
        if sys.argv[1] == 'It is created':
            db.create_all()
    else:
        app.run()

if __name__ == "__main__":
    app.run(debug=True)
    import os

    os.system("dropdb cities")
    os.system("dropdb events")
    print('dropping db')

    os.system("createdb cities")
    os.system("createdb events")
    print('created db')

