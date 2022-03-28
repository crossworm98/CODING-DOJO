from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DB = 'car_dealers'

class Seller:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    @classmethod
    def register(cls, data):
        query = "INSERT INTO sellers (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s)"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_seller(cls, data):
        query = "SELECT * FROM sellers WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM sellers WHERE email = %(email)s"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @staticmethod
    def validate_seller(seller):
        is_valid = True
        if not EMAIL_REGEX.match(seller['email']):
            flash('User email is not valid. Check again.')
            is_valid = False
        if len(seller['fname']) < 3 or len(seller['lname']) < 3:
            flash('First AND Last name must be at least 3 characters long')
            is_valid = False
        if len(seller['password']) < 5:
            flash('Password must be at least 5 characters long')
            is_valid = False
        if seller['confirmpass'] != seller['password']:
            flash('Passwords do not match')
            is_valid = False
        return is_valid