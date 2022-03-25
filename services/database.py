import sqlite3


class MyDatabase:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect("movies.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()
        create_movie_table = "CREATE TABLE IF NOT EXISTS movie (movie_id integer PRIMARY KEY AUTOINCREMENT NOT NULL, name text, sinopse text, rating text, url_image text, cast text)"
        self._cursor.execute(create_movie_table)
        self._db_connection.commit()

    def create_movie(self, movie):
        create_movie_SQL = "INSERT INTO movie (name, sinopse, rating, url_image, cast) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            movie.name, movie.sinopse, movie.rating, movie.url_image, movie.cast
        )
        self._cursor.execute(create_movie_SQL)
        self._db_connection.commit()

        return self._cursor.lastrowid

    def list_movies(self):
        list_movies_SQL = "SELECT * from movie;"
        return self._cursor.execute(list_movies_SQL).fetchall()

    def delete_movie(self, movie):
        delete_movie_SQL = "DELETE FROM movie WHERE movie_id='{}'".format(movie.id)
        self._cursor.execute(delete_movie_SQL)
        self._db_connection.commit()

    def find_movie(self, movie_id):
        select_movie_SQL = "SELECT * FROM movie WHERE movie_id='{}'".format(movie_id)
        return self._cursor.execute(select_movie_SQL).fetchone()

    def edit_movie(self, movie):
        edit_movie_SQL = "UPDATE movie SET name='{}', sinopse='{}', rating='{}', url_image='{}', cast='{}' WHERE movie_id='{}'".format(
            movie.name,
            movie.sinopse,
            movie.rating,
            movie.url_image,
            movie.cast,
            movie.id,
        )

        self._cursor.execute(edit_movie_SQL)
        self._db_connection.commit()

    def find_filter(self, title=None, actor=None):
        select_movie_SQL = "SELECT * FROM movie WHERE 1=1 "

        if title:
            wr = "OR title like '%{}%'".format(title)
        if actor:
            wr += "OR cast like '%{}%'".format(actor)

        return self._cursor.execute(select_movie_SQL).fetchmany()

    def __del__(self):
        self._db_connection.close()
