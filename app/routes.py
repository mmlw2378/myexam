from flask import render_template, request, redirect, url_for
from . import db
from .models import Movie

def register_routes(app):
    @app.route('/')
    def index():
        # Récupérer les paramètres de recherche et de filtrage
        search_query = request.args.get('search', '').strip()
        filter_status = request.args.get('filter', 'all')

        # Construire la requête de base
        query = Movie.query

        # Appliquer la recherche par titre
        if search_query:
            query = query.filter(Movie.title.ilike(f'%{search_query}%'))

        # Appliquer le filtre par statut (vus/non vus)
        if filter_status == 'watched':
            query = query.filter_by(watched=True)
        elif filter_status == 'not_watched':
            query = query.filter_by(watched=False)

        # Trier les résultats par ID décroissant
        movies = query.order_by(Movie.id.desc()).all()

        return render_template('index.html', movies=movies, search_query=search_query, filter_status=filter_status)

    @app.route('/add', methods=['GET', 'POST'])
    def add_movie():
        if request.method == 'POST':
            title = request.form['title']
            year = request.form['year']
            description = request.form['description']
            image_url = request.form['image_url']
            new_movie = Movie(
                title=title,
                year=int(year) if year else None,
                description=description,
                image_url=image_url
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_movie.html')

    @app.route('/toggle/<int:movie_id>')
    def toggle_watched(movie_id):
        movie = Movie.query.get_or_404(movie_id)
        movie.watched = not movie.watched
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/delete/<int:movie_id>')
    def delete_movie(movie_id):
        movie = Movie.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('index'))