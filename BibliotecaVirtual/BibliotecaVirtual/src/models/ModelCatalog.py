from .entities.Catalog import Catalog

class ModelCatalog():

    @classmethod
    def catalog(self, db, catalog, Lib):
        try:
            cur = db.connection.cursor()
            sql = """SELECT Lib_Id, Lib_Nombre, Aut_Nombre, Lib_FPublicacion
            FROM catalog WHERE Lib_Id = '{}'""".format(Lib.Id)
            cur.execute(sql)
            row = cur.fetchone()
            if row != None:
                catalog = Catalog(row[0], row[1], row[2], row[3], row[4], row[5])
                return catalog
            else:
                return None
        except Exception as ex:
            raise Exception(ex)