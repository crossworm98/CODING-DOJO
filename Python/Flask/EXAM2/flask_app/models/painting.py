from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = 'art_schema'

class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.artist_id = data['artist_id']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO paintings ( title, description, price, artist_id  ) VALUES (%(title)s, %(description)s, %(price)s, %(artist_id)s )"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def get_paintings(cls, data):
        query = "SELECT * FROM artists JOIN paintings ON artist.id = paintings.artist_id WHERE artist_id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def getall_paintings(cls):
        query = "SELECT * FROM paintings JOIN artists ON artists.id = paintings.artist_id"
        return connectToMySQL(DB).query_db(query)
    @classmethod
    def pickone(cls, data):
        query = "SELECT * FROM paintings WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    @classmethod
    def update(cls, data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @staticmethod
    def validate_painting(painting):
        is_valid = True
        if len(painting['title']) < 3:
            flash('Entries must be longer than 3 characters.')
            is_valid = False
        if len(painting['description']) < 10:
            flash('Entries must be at least 10 characters')
            is_valid = False
        if len(painting['price']) < 0:
            is_valid = False
        return is_valid