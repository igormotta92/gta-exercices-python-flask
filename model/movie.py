import time
from json import dumps, loads


class MovieModel:
    _movie_list = list()

    def __init__(self, params) -> None:
        self.id = round(time.time() * 1000)
        self.name = params.name
        self.sinopse = params.sinopse
        self.rating = params.rating
        self.url_image = params.url_image
        # self.cast = params.cast

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "sinopse": self.sinopse,
            "rating": self.rating,
            "url_image": self.url_image,
            # "cast": self.cast,
        }

    @classmethod
    def add_movie(cls, movie):
        cls._movie_list.append(movie)

    @classmethod
    def find_movie(cls, movie_id):
        found_movie = None
        for movie in cls._movie_list:
            if movie.id == movie_id:
                found_movie = movie
                break
        return found_movie

    @classmethod
    def find_movie_by_params(cls, params):
        found_movie = list()
        title = params.get("title")

        for movie in cls._movie_list:
            if title.upper() in movie.name.upper():
                found_movie.append(movie)
                # break
        return found_movie

    @classmethod
    def list_to_dict(cls):
        return loads(dumps(cls._movie_list, default=MovieModel.to_dict))

    @classmethod
    def remove_movie(cls, movie):
        cls._movie_list.remove(movie)
