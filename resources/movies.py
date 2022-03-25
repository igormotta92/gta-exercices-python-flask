from json import dumps, loads

from flask_restful import Resource, reqparse
from model.movie import MovieModel


class Movie(Resource):
    def get(self, movie_id=None):

        ### /<:movie_id>
        if movie_id is not None:
            movie = MovieModel.find_movie(movie_id)
            if movie:
                return movie.to_dict()
            else:
                return {"message": "Movie not found"}, 404

        ### filters
        # request.args
        parse = reqparse.RequestParser()
        parse.add_argument("title", type=str, location="args")
        parse.add_argument("actor", type=str, location="args")
        params = parse.parse_args()
        # print(params.title, params.actor)

        if params.title is not None:
            movie = MovieModel.find_movie_by_params(params)
            if len(movie) > 0:
                return loads(dumps(movie, default=MovieModel.to_dict))
            else:
                return {}

        ### all
        return MovieModel.list_to_dict()

    def post(self):

        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("name")
        body_arguments.add_argument("sinopse")
        body_arguments.add_argument("rating")
        body_arguments.add_argument("url_image")
        body_arguments.add_argument("cast", action="append")
        params = body_arguments.parse_args()

        new_movie = MovieModel(params)
        MovieModel.add_movie(new_movie)

        return new_movie.to_dict()

    def delete(self, movie_id):
        movie = MovieModel.find_movie(movie_id)
        if movie:
            MovieModel.remove_movie(movie)
            return movie.to_dict()
        return {"message": "Movie not found"}, 404

    def put(self, movie_id):
        movie = MovieModel.find_movie(movie_id)

        if movie:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("name")
            body_arguments.add_argument("sinopse")
            body_arguments.add_argument("rating")
            body_arguments.add_argument("url_image")
            body_arguments.add_argument("cast", action="append")

            params = body_arguments.parse_args()

            movie.name = params.name
            movie.sinopse = params.sinopse
            movie.rating = params.rating
            movie.url_image = params.url_image
            movie.cast = params.cast

            MovieModel.edit_movie(movie)

            return movie.to_dict()

        return {"message": "Movie not found"}, 404
