from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Survey:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data):
        query= "INSERT INTO surveys (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_survey(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Survey(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 2:
            is_valid=False
            flash("Name must be at least two characters.")
        if len(survey['location']) < 1:
            is_valid=False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid=False
            flash("Must choose a language.")
        if len(survey['comment']) < 2:
            is_valid=False
            flash("Must leave a comment of at least two characters.")
        return is_valid

