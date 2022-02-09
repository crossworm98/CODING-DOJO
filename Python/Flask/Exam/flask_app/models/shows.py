from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = 'exam_db'

class Show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['date']
        self.comments = data['comments']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows ( title, network, release_date, comments)"\
            "VALUES (%(title)s, %(network)s, %(release_date)s, %(comments)s)"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def get_shows(cls):
        query = "SELECT * FROM shows"
        return connectToMySQL(DB).query_db(query)
    @classmethod
    def get_show(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def pickone(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(date)s, comments = %(comments)s WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @staticmethod
    def validate_show(show):
        is_valid = True
        if len(show['title']) < 3 or len(show['network']) < 3 or len(show['comments']) < 3:
            flash('Entries must be longer than 3 characters.')
            is_valid = False
        return is_valid