from .entities import Author

class ModelAuthor():

    @classmethod
    def register_author(self, db, author):
        try:
            conn = db.connection
            cursor = db.connection.cursor()
            id = None
            name = author.name
            lastname = author.lastname
            cursor.execute("INSERT INTO autor VALUES (%s,%s,%s)", (id, name, lastname))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def list_authors(self, db):
        cur = db.connection.cursor()
        sql = """SELECT Aut_Id, Aut_Nombre, Aut_Apellido
        FROM autor"""
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        return data
    
    @classmethod
    def get_author_byID(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """SELECT Aut_Id, Aut_Nombre, Aut_Apellido FROM autor WHERE Aut_Id = {}""".format(id)
        cur.execute(sql)
        data = cur.fetchone()
        return data

    @classmethod
    def update_author(self, db, id, author):
        name = author.name
        lastname = author.lastname
        conn = db.connection
        cur = conn.cursor()
        cur.execute("""
        UPDATE autor
        SET Aut_Nombre = %s,
            Aut_Apellido = %s
        WHERE Aut_Id = %s """, (name, lastname, id))
        conn.commit()
    
    @classmethod
    def delete_author(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """DELETE FROM autor WHERE Aut_id = {}""".format(id)
        cur.execute(sql)
        conn.commit()

    @classmethod
    def search_author(sef, db, searchAuthorCondition):
        searchCondition = "%"+ searchAuthorCondition + "%"
        cur = db.connection.cursor()
        cur.execute("""
        SELECT Aut_Id, Aut_Nombre, Aut_Apellido
        FROM autor
        WHERE Aut_Nombre like %s
            or Aut_Apellido like %s """, (searchCondition, searchCondition))
        data = cur.fetchall()
        return data
    
    @classmethod
    def count_authors(self, db):
        cur = db.connection.cursor()
        sql = """SELECT COUNT(*) AS 'cantidad de usuarios'
        FROM autor"""
        cur.execute(sql)
        data = cur.fetchone()
        return data