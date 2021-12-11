from functions import search_posts_by_substring, get_favorites
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/search")
def page_search():
    s = request.args.get("s")
    posts = search_posts_by_substring(s)
    return render_template("search.html", posts=posts)

@app.route("/favorites")
def page_favorites():
    favorites = get_favorites()
    have_favorites = len(favorites) > 0
    return render_template("favorites.html", have_favorites=have_favorites)


app.run()
