from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "users"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod # SAVE/CREATE
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod # UPDATE
    def update(cls, data):
        query = """UPDATE users 
                SET first_name = %(first_name)s, 
                last_name = %(last_name)s, 
                email = %(email)s
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod # DELETE
    def delete(cls, id):
        query = """
                DELETE FROM users
                WHERE id = %(id)s;
        """
        data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod # READ ONE
    def get_one(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod # ALL USERS/READ
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
