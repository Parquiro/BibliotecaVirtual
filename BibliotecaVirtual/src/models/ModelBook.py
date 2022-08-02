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
            conn.close()
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
    
    @classmethod
    def update_book(self, db, id, book):
        name = book.name
        editorial = book.editorial
        pages = book.pages
        publicDate = book.publicD
        author = book.authorBook
        genre = book.genreBook
        description = book.description
        url = book.url
        conn = db.connection
        cur = conn.cursor()
        cur.execute("""
        UPDATE libro
        SET  
            Lib_Nombre = %s, Lib_Editorial = %s,
            Lib_NroPaginas = %s, Lib_FPublicacion = %s,
            Lib_IdAutor = %s, Lib_IdGenero = %s, Lib_Descripcion = %s, Lib_Url = %s     
        WHERE Lib_Id = %s """, (name, editorial, pages, publicDate, author, genre, description, url, id))
        conn.commit()
        conn.close()
    
    @classmethod
    def delete_book(self, db, id):
        conn = db.connection
        cur = conn.cursor()
        sql = """DELETE FROM libro WHERE Lib_id = {}""".format(id)
        cur.execute(sql)
        conn.commit()
        conn.close()
    
    @classmethod
    def search_book(self, db, searchBookCondition):
        searchCondition = "%"+ searchBookCondition +"%"
        conn = db.connection
        cur = conn.cursor()
        cur.execute("""SELECT Lib_Id, Lib_Nombre, Lib_IdAutor, Lib_IdGenero, Lib_Editorial, Lib_FPublicacion, Lib_Url
        FROM libro
        WHERE Lib_Nombre like %s
        or Lib_Editorial like %s """, (searchCondition, searchCondition))
        data = cur.fetchall()
        return data

    @classmethod
    def count_books(self, db):
        cur = db.connection.cursor()
        sql = """SELECT COUNT(*) AS 'cantidad de libros'
        FROM libro"""
        cur.execute(sql)
        data = cur.fetchone()
        return data