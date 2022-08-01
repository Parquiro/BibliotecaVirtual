from .entities import Book

class ModelBook():
    @classmethod
    def register_book(self, db, book):
        try:
            conn = db.connection
            cursor = db.connection.cursor()
            id = None
            name = book.name
            editorial = book.editorial
            pages = book.pages
            publicDate = book.publicD
            author = book.authorBook
            genre = book.genreBook
            description = book.description
            url = book.url
            cursor.execute("INSERT INTO libro VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, name,
            editorial, pages, publicDate, author, genre, description, url))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def list_book(self, db):
        cur = db.connection.cursor()
        sql = """SELECT Lib_Id, Lib_Nombre, Lib_IdAutor, Lib_IdGenero, Lib_Editorial, Lib_FPublicacion, Lib_Url
        FROM libro"""
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @classmethod
    def get_book_byID(self, db, id):
        cur = db.connection.cursor()
        sql = """
        SELECT Lib_Id, 
            Lib_Nombre,  Lib_IdGenero,
            Lib_IdAutor, Lib_Descripcion,
            Lib_Url, Lib_Editorial,
            Lib_FPublicacion, Lib_NroPaginas
        FROM libro
        WHERE Lib_Id = {}""".format(id)
        cur.execute(sql)
        data = cur.fetchone()
        return data