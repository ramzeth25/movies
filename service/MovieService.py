from db.database import db_session
from db.entity import Movie
from db.repository import MovieRepository


class MovieService:
    def __init__(self):
        self.repository = MovieRepository(db_session)

    def create_movie(self, new_movie):
        self.repository.create(Movie(**new_movie))

    def delete_movie(self, movie_id):
        self.repository.delete_movie(movie_id)

    def find_by_id(self, movie_id):
        return self.repository.find_by_id(movie_id)

    # def find_by(self, param):
    #     return self.repository.find_by_params(param)

    def find_by(self, params):
        print("Code inside find_by from MovieService")
        return self.repository.find_by_params(params)

    def list(self, query):
        return self.repository.list_movies(query)

    def update_movie(self, movie_id, movie_data):
        self.repository.update_movie(movie_id, movie_data)

