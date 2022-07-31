from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

#Models
from models.ModelUser import ModelUser
from models.ModelAuthor import ModelAuthor

#Entities
from models.entities.User import User
from models.entities.Author import Author

app = Flask(__name__)
app.secret_key = 'mySecretKey'

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        user = User(None, request.form['dni'], request.form['name'], request.form['lastname'],
        request.form['username'], request.form['password'], request.form['phone'])
        ModelUser.register_user(db, user)
        flash('Usuario registrado satisfactoriamente')
    else: 
        return render_template('auth/registro.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(None, None, None, None, request.form['username'], request.form['password'], None)
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('adminHome'))
            else:
                flash("Contraseña incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/adminHome')
#@login_required
def adminHome():
    data = ModelUser.count_users(db)
    return render_template('admin/adminHome.html', countUsers = data)

@app.route('/registerUser', methods=['GET', 'POST'])
#@login_required
def registerUser():
    if request.method == 'POST':
        user = User(None, request.form['dni'], request.form['name'], request.form['lastname'],
        request.form['username'], request.form['password'], request.form['phone'])
        ModelUser.register_user(db, user)
        flash('Usuario registrado satisfactoriamente')
    else: 
        return render_template('admin/registerUser.html')
    return redirect(url_for('registerUser'))

@app.route('/addAuthor', methods=['GET', 'POST'])
def addAuthor():
    if request.method == 'POST':
        author = Author(None, request.form['authorName'], request.form['authorLastname'])
        ModelAuthor.register_author(db, author)
        flash('Autor registrado satisfactoriamente')
    else:
        return render_template('admin/newAutor.html')
    return redirect(url_for('addAuthor'))

@app.route('/userList', methods=['GET', 'POST'])
#@login_required
def userList():
    data = ModelUser.list_users(db)
    return render_template('admin/userList.html', users = data)

@app.route('/searchUsers', methods=['GET', 'POST'])
def searchUsers():
    searchCondition = request.form['searchCondition']
    data = ModelUser.search_user(db, searchCondition)
    return render_template('admin/userList.html', users = data)


@app.route('/editUser/<string:id>')
#@login_required
def editUser(id):
    data = ModelUser.get_user_byID(db, id)
    user = ModelUser.list_users(db)
    return render_template('admin/editUser.html', userEdit = data, users = user)

@app.route('/updateUser/<string:id>', methods = ['POST'])
def updateUser(id):
    userUpdate = User(id, request.form['dni'], request.form['name'], request.form['lastname'],
    request.form['username'], 0, request.form['phone'])
    ModelUser.update_user(db, id, userUpdate)
    flash('Usuario actualizado correctamente')
    return redirect(url_for('userList'))


@app.route('/deleteUser/<string:id>', methods=['GET', 'POST'])
#@login_required
def delete_user(id):
    data = ModelUser.delete_user(db, id)
    flash('--- Usuario eliminado correctamente ---')
    return redirect(url_for('userList'))

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()