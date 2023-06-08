from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash  
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name =  data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# Add user into db
    @classmethod
    def save(cls, data):
        query ="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"
        return connectToMySQL('login_registration').query_db( query, data )

# Get all users - didnt need for this project but could be useful later
    # @classmethod
    # def get_all(cls):
    #     query ="SELECT * FROM users;"
    #     results = connectToMySQL('login_registration').query_db(query)
    #     users = []
    #     for user in results:
    #         users.append( cls(user) )
    #     return users

# Get one user
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_registration').query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

# Get user by email
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_registration").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

# Registration validation
    @staticmethod
    def validate( user ):
        is_valid = True
        if len(user['first_name'])< 2:
            is_valid = False
            flash("First name must be at least two characters.","register")
        if len(user['last_name'])< 2:
            is_valid = False
            flash("Last name must be at least two characters.","register")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password'])< 8:
            flash("Password must be at least eight characters.","register")
            is_valid = False
        if user['confirm_password'] != user['password']:
            flash("Passwords do not match.")
            is_valid = False
        return is_valid
