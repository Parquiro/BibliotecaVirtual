class Book():
    def __init__(self, Lib_Id, Lib_Nombre, Lib_Editorial, Lib_NroPaginas, Lib_FPublicacion, Lib_IdAutor, Lib_IdGenero, Lib_Descripcion, Lib_Url) -> None:
        self.id = Lib_Id
        self.name = Lib_Nombre
        self.editorial = Lib_Editorial
        self.pages = Lib_NroPaginas
        self.publicD = Lib_FPublicacion
        self.authorBook = Lib_IdAutor
        self.genreBook = Lib_IdGenero
        self.description = Lib_Descripcion
        self.url = Lib_Url