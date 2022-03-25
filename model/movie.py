import time
from ast import Param
from json import dumps, loads

from services.database import MyDatabase


class MovieModel:
    _movie_list = list()
    database_service: MyDatabase = None

    def __init__(self, params) -> None:
        # self.id = round(time.time() * 1000)
        self.name = params.name
        self.sinopse = params.sinopse
        self.rating = params.rating
        self.url_image = params.url_image
        self.cast = params.cast

    def to_dict(self):
        return {
            # "id": self.id,
            "name": self.name,
            "sinopse": self.sinopse,
            "rating": self.rating,
            "url_image": self.url_image,
            "cast": self.cast,
        }

    @classmethod
    def add_movie(cls, movie):
        # depois fazer outra tabela para isso
        movie.cast = ", ".join(movie.cast)
        cls.database_service.create_movie(movie)

    @classmethod
    def find_movie(cls, movie_id):
        found_movie = None
        result = cls.database_service.find_movie(movie_id)
        if result:
            found_movie = MovieModel(
                result[1], result[2], result[3], result[4], result[5], result[6]
            )
        return found_movie

    @classmethod
    def find_movie_by_params(cls, params):
        title = params.get("title")
        actor = params.get("actor")
        found_movie = cls.database_service.find_filter(title, actor)
        return found_movie

    @classmethod
    # def list_to_dict(cls):
    #     return loads(dumps(cls._movie_list, default=MovieModel.to_dict))
    def list_to_dict(cls):
        # está dando erro aqui 24/03/2022
        result = cls.database_service.list_movies()
        movie_list = []
        for post in result:
            params = {
                "name": post[1],
                "sinopse": post[2],
                "rating": post[3],
                "url_image": post[4],
                "cast": post[5],
            }
            movie_list.append(MovieModel(params))
        return loads(dumps(movie_list, default=MovieModel.to_dict))

    @classmethod
    def remove_movie(cls, movie):
        cls.database_service.delete_movie(movie)

    @classmethod
    def edit_movie(cls, movie):
        movie.cast = ", ".join(movie.cast)
        cls.database_service.edit_movie(movie)
