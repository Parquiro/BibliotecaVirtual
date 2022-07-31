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