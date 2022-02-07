from flask import request
from .models import session, Content

class Film:

    def __init(self, name, description, poster):
        self.name = name
        self.description = description
        self.poster  = poster


    def add_film(self):
        film_name = request.form['filmName']
        film_desc = request.form['filmDesc']
        film_img = request.form['filmImg']
        print(film_name, film_desc, film_img)
        new_film = Content(name=film_name, description=film_desc, poster=film_img)

        session.add(new_film)
        session.commit()

