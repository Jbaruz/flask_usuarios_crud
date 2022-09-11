from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name'] 
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('usuarios').query_db(query)
        all_users = []
        if len(results) == 0:
            return None
        for data in results:
            all_users.append(cls(data))
        return all_users
    
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': id}   
        results = connectToMySQL('usuarios').query_db(query, data)
        return cls(results[0])if len(results)> 0 else None

    @classmethod
    def insert_user(cls, data):
        query = f"INSERT INTO users(first_name,last_name,email,created_at,updated_at)VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        results = connectToMySQL('usuarios').query_db(query,data)
        print (results)
        return results
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s,NOW(),NOW();"
        results = connectToMySQL('usuarios').query_db(query,data)
        return results
    
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id': id}   
        results = connectToMySQL('usuarios').query_db(query, data)
        return results
