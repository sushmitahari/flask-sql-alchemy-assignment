from src.models import db, Movie
class MovieRepository:
    def get_all_movies(self):
        # TODO get all movies from the DB
        movies = Movie.query.all()
        return movies
    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        movies1 = Movie.query.get(movie_id)
        return movies1

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_Movie=Movie(title, director, rating)
        movies2 = Movie.session.add(new_Movie)
        return movies2

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movies3=Movie.query.filter(Movie.message.match(title)).all()
        return movies3



# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
