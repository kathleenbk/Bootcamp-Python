from flask_app.config.mysqlconnection import connectToMySQL
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Email:
    db="email_validation"
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.db).query_db(query,email)
        if len(results) >= 1:
            flash("Email is already in use.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email")
            is_valid=False
        return is_valid

