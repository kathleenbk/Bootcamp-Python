from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
from flask import flash

class Ninja:
    def __init__( self, db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # self.dojo_id = db_data['dojo_id']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def create(cls, data ):
        query = "INSERT INTO ninjas (first_name , last_name , age, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s );"

        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        if len(ninja['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(ninja['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if int(ninja['age']) < 10:
            flash("Ninja must be at least 10 years of age.")
            is_valid = False
        return is_valid