from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, Usu_Id, Usu_Dni, Usu_Nombre, Usu_Apellido, Usu_Email, Usu_Password, Usu_Telefono) -> None:
        self.id = Usu_Id
        self.dni = Usu_Dni
        self.name = Usu_Nombre
        self.lastname = Usu_Apellido
        self.username = Usu_Email
        self.password = Usu_Password
        self.phone = Usu_Telefono

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#print(generate_password_hash("sofia"))