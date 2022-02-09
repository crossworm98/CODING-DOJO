from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
DB = 'dojo_survey_schema'
class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment)"\
            "VALUES (%(name)s, %(dojoloc)s, %(dojolang)s, %(comment)s)"
        return connectToMySQL(DB).query_db(query, data)
    @classmethod
    def results(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['comment']) < 15:
            flash("Comments must be longer than 15 characters.")
            is_valid = False
        if survey['dojolang'] == 'null':
            flash("A language must be specified")
            is_valid = False
        return is_valid