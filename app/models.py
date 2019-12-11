from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class City(db.Model):

    __tablename__ = "cities"

    city_id = db.Column(db.String(64), autoincrement=True, primary_key=True)
    origin_airport = db.Column(db.String(64), nullable=True )
    destination_airport = db.Column(db.String(64), nullable=True )
    destination = db.Column(db.String(64), nullable=True )
    departure_date = db.Column(db.String(64), nullable=True)
    return_date = db.Column(db.String(64), nullable=True)


class Event(db.Model):

    __tablename__ = "events"

    city_id = db.Column(db.String(64), db.ForeignKey('cities.city_id'))
    event_id = db.Column(db.String(64), primary_key=True )
    destination = db.Column(db.String(64),nullable=True)
    event_date = db.Column(db.String(64), nullable=True)
    event_time = db.Column(db.String(64), nullable=True)
    event_name = db.Column(db.String(64), nullable=True)
    event_location = db.Column(db.String(64), nullable=True)
    event_cost = db.Column(db.String(64), nullable=True)
    event_theme = db.Column(db.String(64), nullable=True)
    event_description = db.Column(db.String(20000), nullable=True)


    city = db.relationship("City",
                           backref=db.backref("events", order_by=event_id))

def __repr__(self):

        return "<location %s name %s>" % (
            self.destination, self.event_name)


def connect_to_db(app, database_URI='postgresql:///cities'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = database_URI
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)