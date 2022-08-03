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
        sql = """
        SELECT 
            libro.Lib_Id, libro.Lib_Nombre, autor.Aut_Nombre, 
            autor.Aut_Apellido, genero.Gen_Nombre, libro.Lib_Editorial,
            libro.Lib_FPublicacion, libro.Lib_Url 
        FROM libro
        INNER JOIN autor ON
            libro.Lib_IdAutor = autor.Aut_Id   
        INNER JOIN genero ON
            libro.Lib_IdGenero = genero.Gen_Id """
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @classmethod
    def get_book_byID(self, db, id):
        cur = db.connection.cursor()
        sql = """
        SELECT 
            libro.Lib_Id, libro.Lib_Nombre, libro.Lib_IdGenero, genero.Gen_Nombre, 
            libro.Lib_IdAutor, autor.Aut_Nombre, autor.Aut_Apellido, libro.Lib_Descripcion,
            libro.Lib_Url, libro.Lib_Editorial,
            libro.Lib_FPublicacion, libro.Lib_NroPaginas
        FROM libro
        INNER JOIN autor ON
            libro.Lib_IdAutor = autor.Aut_Id   
        INNER JOIN genero ON
            libro.Lib_IdGenero = genero.Gen_Id 
        WHERE libro.Lib_Id = {} """.format(id)
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
        cur.execute("""
        SELECT 
            libro.Lib_Id, libro.Lib_Nombre, autor.Aut_Nombre, 
            autor.Aut_Apellido, genero.Gen_Nombre, libro.Lib_Editorial,
            libro.Lib_FPublicacion, libro.Lib_Url 
        FROM libro
        INNER JOIN autor ON
            libro.Lib_IdAutor = autor.Aut_Id   
        INNER JOIN genero ON
            libro.Lib_IdGenero = genero.Gen_Id
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