from . import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)  
    image_url = db.Column(db.String(255), nullable=True)  
    watched = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Movie {self.title} ({self.year}) - Watched: {self.watched}>'