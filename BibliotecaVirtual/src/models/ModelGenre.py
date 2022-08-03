from .entities import Genre

class ModelGenre():
    @classmethod
    def register_genre(self, db, genre):
        try:
            conn = db.connection
            cursor = db.connection.cursor()
            id = None
            name = genre.name
            cursor.execute("INSERT INTO genero VALUES (%s,%s)", (id, name))
            conn.commit()
            conn.close()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def list_genre(self, db):
        cur = db.connection.cursor()
        sql = """SELECT Gen_Id, Gen_Nombre
        FROM genero"""
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @classmethod
    def get_genre_byID(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """SELECT Gen_Id, Gen_Nombre FROM genero WHERE Gen_Id = {}""".format(id)
        cur.execute(sql)
        data = cur.fetchone()
        return data

    @classmethod
    def update_genre(self, db, id, genre):
        name = genre.name
        conn = db.connection
        cur = conn.cursor()
        cur.execute("""
        UPDATE genero
        SET Gen_Nombre = %s
        WHERE Gen_Id = %s """, (name, id))
        conn.commit()
        conn.close()
    
    @classmethod
    def delete_genre(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """DELETE FROM genero WHERE Gen_id = {}""".format(id)
        cur.execute(sql)
        conn.commit()
        conn.close()

    @classmethod
    def search_genre(sef, db, searchGenreCondition):
        searchCondition = "%"+ searchGenreCondition + "%"
        cur = db.connection.cursor()
        cur.execute("""
        SELECT Gen_Id, Gen_Nombre
        FROM genero
        WHERE 
        Gen_Nombre like %s
        or Gen_Id like %s """, (searchCondition, searchCondition))
        data = cur.fetchall()
        return data
    
    @classmethod
    def count_genres(self, db):
        cur = db.connection.cursor()
        sql = """SELECT COUNT(*) AS 'cantidad de generos'
        FROM genero"""
        cur.execute(sql)
        data = cur.fetchone()
        return data