from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "users"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO users (first_name,last_name,email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
