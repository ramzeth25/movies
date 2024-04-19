from sqlalchemy import update, select
from flask import request
from db.database import db_session
from db.entity import Movie


class MovieRepository:

    def __init__(self, session):
        self.session = session

    def create(self, new_movie):
        self.session.add(new_movie)
        self.session.commit()

    def delete_movie(self, movie_id):
        stmt = update(Movie).where(Movie.id == movie_id).values(is_deleted=True)
        self.session.execute(stmt)
        self.session.commit()

    def find_by_id(self, movie_id):
        stmt = select(Movie).where(Movie.id == movie_id).where(Movie.is_deleted == False)
        cursor = self.session.execute(stmt)
        data = cursor.first()

        if data:
            movie, *_ = data
            return movie

        return None

    def find_by_params(self, param):  # retrieving movies by incomplete name, year, genre with pagination
        genre_list = ['Action', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance']
        if isinstance(param, str):
            if param in genre_list:
                stmt = (select(Movie).where(Movie.genre.filter('{}').format(param)))
                movies = []
                for row in self.session.execute(stmt):
                    data, *_ = row
                    movies.append(data.to_dict())
                return movies
            else:
                stmt = (select(Movie).where(Movie.genre.filter('%{}%').format(param)))
                movies = []
                for row in self.session.execute(stmt):
                    data, *_ = row
                    movies.append(data.to_dict())
                return movies
        if isinstance(param, int):
            stmt = (select(Movie).where(Movie.genre.filter('{}%').format(param)))
            movies = []
            for row in self.session.execute(stmt):
                data, *_ = row
                movies.append(data.to_dict())
            return movies

    def list_movies(self, query):

        stmt = select(Movie).where(Movie.is_deleted == False)
        if query:
            stmt = stmt.filter_by(**query)

        movies = []
        for row in self.session.execute(stmt):
            data, *_ = row
            movies.append(data.to_dict())

        return movies

    def update_movie(self, movie_id, updated_movie):
        stmp = (
            update(Movie)
            .where(Movie.id == movie_id)
            .where(Movie.is_deleted == False)
            .values(**updated_movie)
        )
        self.session.execute(stmp)
        self.session.commit()







