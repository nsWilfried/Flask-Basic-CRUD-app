# coding=utf-8
from flask import Flask, jsonify, request, render_template, url_for, flash
from werkzeug.utils import redirect

from .models import session, Content
import requests as req
from .home import Film

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET'])
def home():

    if request.method == 'GET':
        data = session.query(Content)

    return render_template('home.html', data=data, title='Animes - Home')


@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    film = session.query(Content).filter(Content.id == id).first()

    if request.method == "POST":
        film.name = request.form['filmName']
        film.description = request.form['filmDescription']
        film.poster = request.form['filmPoster']

        session.commit()
        session.query(Content)
        return redirect(url_for("home"))
    elif request.method == "GET":
        return render_template("update.html", film=film, title="{{film.name}} update")


@app.route("/add/", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    elif request.method == 'POST':
        film_name = request.form['filmName']
        film_desc = request.form['filmDescription']
        film_img = request.form['filmPoster']
        new_film = Content(name=film_name, description=film_desc, poster=film_img)

        session.add(new_film)
        session.commit()

        return redirect('/')


@app.route("/remove/<int:id>",  methods=["POST"])
def remove_film(id):
    if request.method == "POST":
        film = session.query(Content).filter(Content.id == id).first()
        session.delete(film)
        session.commit()
        return redirect('/')



@app.route('/api/', methods=['GET'])
def init_api():
    data_list = []
    if request.method == 'GET':
        data = session.query(Content)
        for one_data in data:
            data_list.append(
                {
                    "name": one_data.name,
                    "description": one_data.description,
                    "poster": one_data.poster
                }

            )

    return jsonify(data_list)




