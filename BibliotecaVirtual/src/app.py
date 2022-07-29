from flask import Flask, redirect, render_template, request, flash, url_for
from flask_mysqldb import MySQL

from config import config


app = Flask(__name__)


db = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('/auth/registro.html')

@app.route('/add_registro', methods = ['POST'])
def add_registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        telefono = request.form['telefono']
        email = request.form['email']
        password = request.form['pass']
        try:
            cursor = db.connection.cursor()
            cursor.execute('INSERT INTO usuario(Usu_Dni,Usu_Nombre,Usu_Apellido,Usu_Email,Usu_Password,Usu_Telefono) VALUES(%s,%s,%s,%s,%s,%s)', 
            (dni, nombre, apellido, email, password, telefono ))
            db.connection.commit()
            flash('Agregado correctamente...')
            return render_template('auth/login.html')
        except Exception as e:
            flash('Ocurrio un error....')
            return redirect(url_for('auth/registro.html'))

@app.route('/login')
def login():
    return render_template('/auth/login.html')

@app.route('/entrar_login', methods = ['POST'])
def entrar_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = db.connection.cursor()
        cursor.execute('SELECT Usu_Password, Usu_Id FROM usuario WHERE Usu_Email = %s', (email,))
        data = cursor.fetchone()
        cursor.close()
        if password == data[0]:
            return redirect(url_for('adminHome', id=data[1]))
        else:
            return redirect(url_for('login'))


@app.route('/adminHome,<id>', methods = ['GET', 'POST'])
def adminHome(id):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM usuario WHERE Usu_id = %s', (id,))
        dato = cursor.fetchall()
        cursor.execute('SELECT COUNT(Usu_Id) FROM usuario')
        dato1 = cursor.fetchall()
        cursor.execute('SELECT COUNT(Lib_Id) FROM libro')
        dato2 = cursor.fetchall()
        cursor.execute('SELECT COUNT(Gen_Id) FROM genero')
        dato3 = cursor.fetchall()
        cursor.execute('SELECT COUNT(Aut_Id) FROM autor')
        dato4 = cursor.fetchall()
        tupla = (dato[0], dato1[0][0], dato2[0][0], dato3[0][0], dato4[0][0])
        print(tupla)
        cursor.close()
        return render_template('adminHome.html', app=dato[0]) 

@app.route('/Categorias')
def Categorias():
    return render_template('category.html')
    
@app.route('/catalogo')
def catalogo():
    return render_template('catalog.html')


if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()