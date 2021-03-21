from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tareas.db'
db = SQLAlchemy(app) #Cursor para la base de datos SQLite


class Tarea(db.Model):
    __tablename__ = "tarea"
    id = db.Column(db.Integer, primary_key=True)  # Identificador único de cada tarea
    contenido = db.Column(db.String(200))  # Contenido de la tarea, un texto de máximo 200 caracteres
    hecha = db.Column(db.Boolean)  # Booleano que indica si una tarea ha sido hecha o no


db.create_all()  # Creación de las tablas
db.session.commit()  # Ejecución de las tareas pendientes en la base de datos

# La barra (el slash) se conoce como la página de inicio (página home).
# Vamos a definir para esta ruta, el comportamiento a seguir.
@app.route('/')
def home():
    todas_las_tareas = Tarea.query.all()
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = Tarea.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = Tarea.query.filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) #El debug=True hace que cada vez que reiniciemos el
# servidor o modifiquemos el codigo, el servidor de Flask se reinicie solo

