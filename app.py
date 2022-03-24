from flask import Flask
from flask_restful import Api

# from resources.comments import Comment
# from resources.movie import Post
from resources.movies import Movie

app = Flask(__name__)
api = Api(app)


api.add_resource(Movie, "/movies", "/movies/<int:movie_id>")

if __name__ == "__main__":
    app.run(debug=True)


######

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/climate/predict", methods=["GET"])

# api.add_resource(Post, "/post/<int:id>", "/post(GET)", "/post")
# api.add_resource(
#     Comment,
#     "/post/<int:post_id>/comment/<int:comment_id>",
#     "/post/<int:post_id>/comment",
# )
