from flask import Flask

from api.movies import list_movies, get_movie, delete_movie, update_movie, create_movie, get_movie_by
from db.database import db_session, init_db

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.add_url_rule("/movies", methods=['GET'], view_func=list_movies)
app.add_url_rule("/movies", methods=['POST'], view_func=create_movie)
app.add_url_rule("/movies/<movie_id>", methods=['GET'], view_func=get_movie)
app.add_url_rule("/movies/values", methods=['GET'], view_func=get_movie_by)
app.add_url_rule("/movies/<movie_id>", methods=['DELETE'], view_func=delete_movie)
app.add_url_rule("/movies/<movie_id>", methods=['PUT'], view_func=update_movie)

init_db()

if __name__ == '__main__':
    app.run()
