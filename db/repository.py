import sqlalchemy
from sqlalchemy import update, select
from flask import request
from sqlalchemy.orm import session
from sqlalchemy import or_
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

    # def find_by_params(self, param):  # retrieving movies by incomplete name, year, genre with pagination
    #     search = "%{}%".format(param)
    #     start = request.args.get('start', 0)
    #     limit = request.args.get('limit', 3)
    #     stmt = select(Movie).filter(Movie.original_title.like(search))
    #     stmt = stmt.offset(start).limit(limit)
    #
    #     movies = []
    #     for row in self.session.execute(stmt):
    #         data, *_ = row
    #         movies.append(data.to_dict())
    #
    #     return movies
    def find_by_params(self, params):  # retrieving movies by incomplete name, year, genre with pagination
        year = None
        name = None
        genre = None
        if 'name' in params:
            name = params['name']
        if 'year' in params:
            year = params['year']
        if 'genre' in params:
            genre = params['genre']
        print('Values after IF', name, year, genre)
        start = request.args.get('start', 0)
        limit = request.args.get('limit', 3)
        movies = []
        if name:
            search = "%{}%".format(name)
            stmt = select(Movie).filter(Movie.original_title.like(search)).where(Movie.is_deleted == False)
            stmt = stmt.offset(start).limit(limit)

            for row in self.session.execute(stmt):
                data, *_ = row
                movies.append(data.to_dict())
        if year:
            search = "%{}%".format(year)
            stmt = select(Movie).filter(Movie.release_date.like(search)).where(Movie.is_deleted == False)
            stmt = stmt.offset(start).limit(limit)

            for row in self.session.execute(stmt):
                data, *_ = row
                movies.append(data.to_dict())

        if genre:
            search = "%{}%".format(genre)
            stmt = select(Movie).filter(Movie.genre.like(search)).where(Movie.is_deleted == False)
            stmt = stmt.offset(start).limit(limit)

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







