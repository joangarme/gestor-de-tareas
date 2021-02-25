from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask
app.config['SQLALCHEMY_DATABASE_UTI'] = 'sqlite://database/tareas.db'
db = SQLAlchemy(app) #Cursor para la base de datos SQLite

# La barra (el slash) se conoce como la página de inicio (página home).
# Vamos a definir para esta ruta, el comportamiento a seguir.
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True) #El debug=True hace que cada vez que reiniciemos el
# servidor o modifiquemos el codigo, el servidor de Flask se reinicie solo

