from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
DB = 'car_dealers'

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.description = data['description']
        self.price = data['price']
        self.sellers_id = data['sellers_id']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cars (make, model, year, description, price, sellers_id) VALUES (%(make)s, %(model)s, %(year)s, %(description)s, %(price)s, %(sellers_id)s)"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars JOIN sellers ON sellers.id = cars.sellers_id "
        return connectToMySQL(DB).query_db(query)

    @classmethod
    def pickone(cls, data):
        query = "SELECT * FROM cars JOIN sellers ON sellers.id = cars.sellers_id WHERE cars.id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def pickall(cls, data):
        query = "SELECT * FROM cars JOIN sellers ON sellers.id = cars.sellers_id WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE cars SET make = %(make)s, model = %(model)s, year = %(year)s, description = %(description)s, price = %(price)s WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)

    @staticmethod
    def validate_car(car):
        is_valid = True
        if len(car['make']) < 3:
            flash('Make must be longer than 3 characters.')
            is_valid = False
        if len(car['model']) < 3:
            flash('Model must be at least 3 characters')
            is_valid = False
        if len(car['year']) < 4:
            flash('Year must be at least year 1900+')
            is_valid = False
        if len(car['description']) < 10:
            flash('Description must be at least 10 characters')
            is_valid = False
        if len(car['price']) < 3:
            flash('Price must be at least $100')
            is_valid = False
        return is_valid