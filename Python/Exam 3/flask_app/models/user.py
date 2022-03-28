from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DB = 'pypie_derby'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s)"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        return connectToMySQL(DB).query_db(query, data)
    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('User email is not valid. Check again.')
            is_valid = False
        if len(user['fname']) < 3 or len(user['lname']) < 3:
            flash('First AND Last name must be at least 3 characters long')
            is_valid = False
        if len(user['password']) < 5:
            flash('Password must be at least 5 characters long')
            is_valid = False
        if len(user['confirmpass']) == user['password']:
            flash('Passwords do not match')
            is_valid = False
        return is_valid