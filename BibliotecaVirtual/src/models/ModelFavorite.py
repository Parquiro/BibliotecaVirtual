from .entities import Favorite

class ModelFavorite():
    
    @classmethod
    def add_favorite(self, db, idUser, idBook):
        conn = db.connection
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO librofavorito VALUES (%s, %s) """, (idUser, idBook))
        conn.commit()
        conn.close()

    @classmethod
    def check_favorites(self, db, id):
        cur = db.connection.cursor()
        print(id)
        sql = """SELECT Id_Usuario, Id_Libro FROM librofavorito WHERE Id_Usuario = {} """.format(id)
        cur.execute(sql)
        data = cur.fetchall()
        return data