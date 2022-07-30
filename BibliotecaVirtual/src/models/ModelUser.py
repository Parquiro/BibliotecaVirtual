from .entities.User import User
from werkzeug.security import generate_password_hash

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cur = db.connection.cursor()
            sql = """SELECT Usu_Id, Usu_Dni, Usu_Nombre, Usu_Apellido, Usu_Email, Usu_Password, Usu_Telefono
            FROM usuario WHERE Usu_Email = '{}'""".format(user.username)
            cur.execute(sql)
            row = cur.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], row[3], row[4], User.check_password(row[5], user.password), row[6])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT Usu_Id, Usu_Nombre, Usu_Apellido, Usu_Email FROM usuario WHERE Usu_Id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], None, row[1], row[2], row[3], None, None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def register_user(self, db, user):
        try:
            conn = db.connection
            #id = "coalcase(select max(usuario.id) from usuario, 0) + 1"
            id = None
            dni = user.dni
            name = user.name
            lastname = user.lastname
            username = user.username
            password = generate_password_hash(user.password)
            phone = user.phone
            cursor = db.connection.cursor()
            cursor.execute("INSERT INTO usuario VALUES (%s,%s,%s,%s,%s,%s,%s)", (id, dni, name, lastname, username, password, phone))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def list_users(self, db):
        cur = db.connection.cursor()
        sql = """SELECT Usu_Id, Usu_Nombre, Usu_Apellido, Usu_Dni, Usu_Email, Usu_Telefono
        FROM usuario"""
        cur.execute(sql)
        data = cur.fetchall()
        return data
    
    @classmethod
    def delete_user(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """DELETE FROM usuario WHERE Usu_id = {}""".format(id)
        cur.execute(sql)
        conn.commit()
    
    @classmethod
    def get_user_byID(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """SELECT Usu_Id, Usu_Dni, Usu_Nombre, Usu_Apellido, Usu_Email, Usu_Telefono FROM usuario WHERE Usu_Id = {}""".format(id)
        cur.execute(sql)
        data = cur.fetchone()
        return data

    @classmethod
    def update_user(self, db, id, user):
        dni = user.dni
        name = user.name
        lastname = user.lastname
        username = user.username
        phone = user.phone
        conn = db.connection
        cur = conn.cursor()
        sql = """UPDATE usuarios 
        SET Usu_Dni = %s, Usu_Nombre = %s, Usu_Apellido = %s,
        Usu_Email = %s, Usu_Telefono = %s
        WHERE Usu_Id = %s""", (dni, name, lastname, username, phone, id)
        conn.commit()

        
        

