from .entities import Book

class ModelCatalog():

    @classmethod
    def filter_by_genre(self, db, id):
        cur = db.connection.cursor()
        sql = """
        SELECT 
            libro.Lib_Id, libro.Lib_Nombre, autor.Aut_Nombre, 
            autor.Aut_Apellido, genero.Gen_Nombre, libro.Lib_Editorial,
            libro.Lib_FPublicacion, libro.Lib_Url 
        FROM libro
        INNER JOIN autor ON
            libro.Lib_IdAutor = autor.Aut_Id   
        INNER JOIN genero ON
            libro.Lib_IdGenero = genero.Gen_Id 
        WHERE libro.Lib_IdGenero = {} """.format(id)
        cur.execute(sql)
        data = cur.fetchall()
        return data