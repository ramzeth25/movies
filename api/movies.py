from flask import request
from service.MovieService import MovieService
from api.validators import validate_movie_query, validate_id, validate_movie_data, validate_param


def list_movies():
    validated_query = validate_movie_query(request.args)
    return MovieService().list(validated_query)


def get_movie(movie_id):
    movie_id = validate_id(movie_id)

    if not movie_id:
        return {}, 400

    movie = MovieService().find_by_id(movie_id)

    if not movie:
        return {}, 404

    return movie.to_dict()


def get_movie_by():
    name = request.args.get('name')
    year = request.args.get('year')
    genre = request.args.get('genre')
    params = validate_param(name, year, genre)
    print(params, "This is data inside get_movi_by function")
    return MovieService().find_by(params)


def delete_movie(movie_id):
    movie_id = validate_id(movie_id)

    if not movie_id:
        return {}, 400

    MovieService().delete_movie(movie_id)
    return {}, 202


def update_movie(movie_id):
    movie_id = validate_id(movie_id)

    if not movie_id:
        return {}, 400

    updated_customer = validate_movie_data(request.json)
    MovieService().update_movie(movie_id, updated_customer)
    return {}, 202


def create_movie():
    new_movie = validate_movie_data(request.json)
    MovieService().create_movie(new_movie)
    return {}, 202
