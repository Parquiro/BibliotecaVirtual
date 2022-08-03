from flask import Flask, render_template, request, flash, redirect, url_for, Response
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from fpdf import FPDF

from config import config

#Models
from models.ModelUser import ModelUser
from models.ModelAuthor import ModelAuthor
from models.ModelGenre import ModelGenre
from models.ModelBook import ModelBook
from models.ModelCatalog import ModelCatalog
from models.ModelFavorite import ModelFavorite

#Entities
from models.entities.User import User
from models.entities.Author import Author
from models.entities.Genre import Genre
from models.entities.Book import Book

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
    users = ModelUser.count_users(db)
    authors = ModelAuthor.count_authors(db)
    genres = ModelGenre.count_genres(db)
    books = ModelBook.count_books(db)
    return render_template('admin/adminHome.html', countUsers = users, countAuthors = authors,
    countGenres = genres, countBooks = books)

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

@app.route('/addGenre', methods=['GET', 'POST'])
def addGenre():
    if request.method == 'POST':
        genre = Genre(None, request.form['genreName'])
        ModelGenre.register_genre(db, genre)
        flash('Genero registrado satisfactoriamente')
    else:
        return render_template('admin/newGenre.html')
    return redirect(url_for('addGenre'))

@app.route('/addBook', methods=['GET', 'POST'])
def addBook():
    if request.method == 'POST':
        book = Book(None, request.form['bookName'], request.form['bookEditorial'], 
        request.form['bookPages'], request.form['bookDate'], request.form['bookAuthor'], 
        request.form['bookGenre'], request.form['bookDescription'], request.form['bookUrl'])
        ModelBook.register_book(db, book)
        flash('Libro registrado satisfactoriamente')
    else:
        dataAuthors = ModelAuthor.list_authors(db)
        dataGenres = ModelGenre.list_genre(db)
        return render_template('admin/addBook.html', authors = dataAuthors, genres = dataGenres)
    return redirect(url_for('addBook'))

@app.route('/userList', methods=['GET', 'POST'])
#@login_required
def userList():
    data = ModelUser.list_users(db)
    return render_template('admin/userList.html', users = data)

@app.route('/authorList', methods=['GET', 'POST'])
def authorList():
    data = ModelAuthor().list_authors(db)
    return render_template('admin/authorList.html', authors = data)

@app.route('/genreList', methods=['GET', 'POST'])
def genreList():
    data = ModelGenre().list_genre(db)
    return render_template('admin/genreList.html', genres = data)

@app.route('/bookList', methods=['GET', 'POST'])
def bookList():
    data = ModelBook().list_book(db)
    return render_template('admin/bookList.html', books = data)

@app.route('/searchUsers', methods=['GET', 'POST'])
def searchUsers():
    searchCondition = request.form['searchCondition']
    data = ModelUser.search_user(db, searchCondition)
    return render_template('admin/userList.html', users = data)

@app.route('/searchAuthors', methods=['GET', 'POST'])
def searchAuthors():
    searchCondition = request.form['searchCondition']
    data = ModelAuthor().search_author(db, searchCondition)
    return render_template('admin/authorList.html', authors = data)

@app.route('/searchGenres', methods=['GET', 'POST'])
def searchGenres():
    searchCondition = request.form['searchCondition']
    data = ModelGenre().search_genre(db, searchCondition)
    return render_template('admin/genreList.html', genres = data)

@app.route('/searchBooks', methods=['GET', 'POST'])
def searchBooks():
    searchCondition = request.form['searchCondition']
    data = ModelBook().search_book(db, searchCondition)
    return render_template('admin/bookList.html', books = data)

@app.route('/editUser/<string:id>')
#@login_required
def editUser(id):
    data = ModelUser.get_user_byID(db, id)
    return render_template('admin/editUser.html', userEdit = data)

@app.route('/editAuthor/<string:id>')
#@login_required
def editAuthor(id):
    data = ModelAuthor.get_author_byID(db, id)
    return render_template('admin/editAuthor.html', authorEdit = data)

@app.route('/editGenre/<string:id>')
#@login_required
def editGenre(id):
    data = ModelGenre.get_genre_byID(db, id)
    return render_template('admin/editGenre.html', genreEdit = data)

@app.route('/editBook/<string:id>')
#@login_required
def editBook(id):
    bookEdit = ModelBook.get_book_byID(db, id)
    genre = ModelGenre().list_genre(db)
    author = ModelAuthor().list_authors(db)
    return render_template('admin/editBook.html', bookEdit = bookEdit, genres = genre, authors = author)

@app.route('/updateUser/<string:id>', methods = ['POST'])
def updateUser(id):
    userUpdate = User(id, request.form['dni'], request.form['name'], request.form['lastname'],
    request.form['username'], 0, request.form['phone'])
    ModelUser.update_user(db, id, userUpdate)
    flash('Usuario actualizado correctamente')
    return redirect(url_for('userList'))

@app.route('/updateAuthor/<string:id>', methods = ['POST'])
def updateAuthor(id):
    authorUpdate = Author(id, request.form['authorName'], request.form['authorLastname'])
    ModelAuthor.update_author(db, id, authorUpdate)
    flash('Autor actualizado correctamente')
    return redirect(url_for('authorList'))

@app.route('/updateGenre/<string:id>', methods = ['POST'])
def updateGenre(id):
    genreUpdate = Genre(id, request.form['genreName'])
    ModelGenre.update_genre(db, id, genreUpdate)
    flash('Genero actualizado correctamente')
    return redirect(url_for('genreList'))

@app.route('/updateBook/<string:id>', methods = ['POST'])
def updateBook(id):
    bookUpdate = Book(id, request.form['bookName'], request.form['bookEditorial'], 
    request.form['bookPages'], request.form['bookDate'], request.form['bookAuthor'], 
    request.form['bookGenre'], request.form['bookDescription'], request.form['bookUrl'])
    ModelBook.update_book(db, id, bookUpdate)
    flash('Libro actualizado correctamente')
    return redirect(url_for('bookList'))

@app.route('/deleteUser/<string:id>', methods=['GET', 'POST'])
#@login_required
def delete_user(id):
    data = ModelUser.delete_user(db, id)
    flash('--- Usuario eliminado correctamente ---')
    return redirect(url_for('userList'))

@app.route('/deleteAuthor/<string:id>', methods=['GET', 'POST'])
#@login_required
def delete_author(id):
    data = ModelAuthor.delete_author(db, id)
    flash('--- Autor eliminado correctamente ---')
    return redirect(url_for('authorList'))

@app.route('/deleteGenre/<string:id>', methods=['GET', 'POST'])
#@login_required
def delete_genre(id):
    data = ModelGenre.delete_genre(db, id)
    flash('--- Genero eliminado correctamente ---')
    return redirect(url_for('genreList'))

@app.route('/deleteBook/<id>', methods=['GET', 'POST'])
#@login_required
def delete_book(id):
    data = ModelBook.delete_book(db, id)
    flash('--- Libro eliminado correctamente ---')
    return redirect(url_for('bookList'))

@app.route('/catalog/<idUser>', methods=['GET', 'POST'])
#@login_required
def catalog(idUser):
    dataBooks = ModelBook.list_book(db)
    dataGenre = ModelGenre.list_genre(db)
    favorite = ModelFavorite.check_favorites(db, idUser)
    return render_template('common/catalog.html', books = dataBooks, genres = dataGenre, users = favorite)

@app.route('/genreFilter/<string:id>', methods=['GET', 'POST'])
def genreFilter(id):
    dataBooks = ModelCatalog.filter_by_genre(db, id)
    dataGenre = ModelGenre.list_genre(db)
    dataAuthor = ModelAuthor().list_authors(db)
    return render_template('common/catalog.html', books = dataBooks, genres = dataGenre, authors = dataAuthor)

@app.route('/addFavorite/<idUser>/<idBook>', methods=['GET', 'POST'])
def addFavorite(idUser, idBook):
    user = idUser
    book = idBook
    ModelFavorite.add_favorite(db, user, book)
    print(user, book)
    return redirect(url_for('catalog', idUser = idUser))


#asdasd
@app.route('/report')
def download_report():
    conn = None
    cursor = None
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute("SELECT Usu_Nombre, Usu_Apellido, Usu_Dni, Usu_Email, Usu_Telefono FROM usuario")
    result = cursor.fetchall()
    pdf = FPDF()
    pdf.add_page()

    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'Usuarios registrados', align='C')
    pdf.ln(10)

    pdf.set_font('Courier', '', 12)

    col_width = page_width/4

    pdf.ln(1)

    th = pdf.font_size

    for row in result:
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, row[1], border=1)
            pdf.cell(col_width, th, str(row[2]), border=1)
            pdf.cell(col_width, th, row[4], border=1)
            pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Times', '', 10.0)
    pdf.cell(page_width, 0.0, '- end of report -', align='C')

    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'attachment;filename=users_report.pdf'})



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