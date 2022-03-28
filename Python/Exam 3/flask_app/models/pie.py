from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
DB = 'pypie_derby'

class Pie:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.users_id = data['users_id']
        self.votes = data['votes']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO pies (name, filling, crust, users_id, votes) VALUES (%(name)s, %(filling)s, %(crust)s, %(users_id)s, 0)"
        return connectToMySQL(DB).query_db(query, data)


    @classmethod
    def get_pies(cls, data):
        query = "SELECT * FROM pies WHERE users_id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def pickone(cls, data):
        query = "SELECT * FROM pies WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE pies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pies JOIN users ON users.id = pies.users_id"
        return connectToMySQL(DB).query_db(query)

    @classmethod
    def pickall(cls, data):
        query = "SELECT * FROM pies JOIN users ON users.id = pies.users_id WHERE users_id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def addvote(cls, data):
        query = "UPDATE pies SET votes = votes + 1 WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pies WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @staticmethod
    def validate_pie(pie):
        is_valid = True
        if len(pie['name']) < 3:
            flash('Name must be at least 3 characters long')
        if len(pie['filling']) < 3:
            flash('Filling must be at least 3 characters long')
            is_valid = False
        if len(pie['crust']) < 3:
            flash('Crust must be at least 3 characters long')
            is_valid = False
        return is_valid