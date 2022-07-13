from flask import Flask, render_template, request, redirect, url_for, flash,send_from_directory
from flaskext.mysql import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
from datetime import datetime
import os
from models.ModelUser import ModelUser
from models.entities.User import User
app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
lg=False
id_user=""
carpeta=os.path.join('archivos')
app.config['carpeta']=carpeta
@app.route('/archivos/<archivo>')
def archivos(archivo):
    return send_from_directory(app.config['carpeta'],archivo)
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)
@app.route('/')
def index():
    return render_template("paginas/index.html")
@app.route('/login', methods=['GET', 'POST'])
def login():
    global lg
    global id_user
    if lg:
        return redirect(url_for("index"))
    else:
        if request.method == 'POST':
            user = User(0, 0,request.form['email'], request.form['password'])
            logged_user = ModelUser.login(db, user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    lg=True
                    id_user=logged_user.id
                    return redirect(url_for('codigos'))
                else:
                    flash("Contraseña incorrecta")
                    return render_template('paginas/login.html')
            else:
                flash("Usuario no encontrado")
                return render_template('paginas/login.html')
        else:
            return render_template('paginas/login.html')

@app.route("/registro",methods=["GET","POST"])
def registro():
    global lg
    if lg:
        return redirect(url_for("index"))
    else: 
        if request.method=="POST":
            user=User(0,request.form["username"],request.form["email"],request.form["password"])
            ModelUser.registro(db,user)
            user = User(0, 0,request.form['email'], request.form['password'])
            logged_user = ModelUser.login(db, user)
            login_user(logged_user)
            lg=True
            id_user=logged_user.id
            return redirect(url_for('codigos'))
        else:
            return render_template("paginas/registro.html")   
@app.route('/logout')
def logout():
    global lg
    global id_user
    logout_user()
    lg=False
    id_user=""
    return redirect(url_for('login'))
@app.route('/home')
@login_required
def home():
    return render_template('home.html')
@app.route('/codigos')
@login_required
def codigos():
    sql="SELECT*FROM codigos"
    conn=db.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    codigos=cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template("paginas/codigos.html",codigos=codigos)
@app.route('/add',methods=['GET','POST'])
def add():

    if request.method=="POST":
        nombre=request.form['name']
        archivo=request.files['archivo']
        now=datetime.now()
        tiempo=now.strftime("%Y%H%M%S")
        if archivo.filename!='':
            newnamearchivo=tiempo+archivo.filename
            archivo.save('archivos/'+newnamearchivo)
        datos=(nombre,newnamearchivo)
        sql="INSERT INTO codigos (id, name, archivo) VALUES (NULL, %s, %s)"
        conn=db.connect()
        cursor=conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        conn.close()
    return redirect(url_for('codigos'))
@app.route('/agregar')
@login_required
def agregar():
    global id_user 
    if id_user=="" or id_user!=1:
        return redirect(url_for("codigos"))
    elif id_user==1:
        

        return render_template("paginas/registra_archivos.html")
@app.route('/editar/<int:id>')
@login_required
def editar(id):
    global id_user 
    if id_user==1 :
        conn=db.connect()
        cursor=conn.cursor()
        cursor.execute("SELECT*FROM codigos WHERE id=%s",(id))
        datos=cursor.fetchall()
        conn.commit()
        conn.close()
        return render_template("paginas/editar.html",datos=datos)
    else:
        return render_template("paginas/index.html")
@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    global id_user 
    if id_user==1:
        conn=db.connect()
        cursor=conn.cursor()
        cursor.execute("SELECT archivo FROM codigos WHERE id=%s",id)
        fila=cursor.fetchall()
        os.remove(os.path.join(app.config['carpeta'],fila[0][0]))
        cursor.execute("DELETE FROM codigos WHERE id=%s",(id))
        conn.commit()
        conn.close()
        return redirect(url_for('codigos'))
    else:
        return render_template("paginas/index.html")
@app.route("/update",methods=["GET","POST"])
@login_required
def update():
    if request.method=="POST":
        id=request.form["id"]
        nombre=request.form['name']
        archivo=request.files['archivo']
        now=datetime.now()
        tiempo=now.strftime("%Y%H%M%S")
        conn=db.connect()
        cursor=conn.cursor()
        if archivo.filename!='':
            newnamearchivo=tiempo+archivo.filename
            archivo.save('archivos/'+newnamearchivo)
            cursor.execute("SELECT archivo FROM codigos WHERE id=%s",id)
            fila=cursor.fetchall()
            os.remove(os.path.join(app.config['carpeta'],fila[0][0]))
            cursor.execute("UPDATE codigos SET archivo=%s WHERE id=%s",(newnamearchivo,id))
            conn.commit()
        datos=(nombre,id)
        sql="UPDATE codigos  SET name=%s WHERE id=%s"


        cursor.execute(sql,datos)
        conn.commit()
        conn.close()

    return redirect(url_for('codigos'))
@app.route("/usuarios")
@login_required
def usuarios():
    sql1="SELECT id, username, email FROM user"
    conn=db.connect()
    cursor=conn.cursor()
    cursor.execute(sql1)
    usuarios=cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template("paginas/usuarios.html",usuarios=usuarios)
    
def status_401(error):
    return redirect(url_for('login'))
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404
if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(port=8000)
