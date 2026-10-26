```python
import os
from flask import Flask
import pyodbc

app = Flask(__name__)

@app.route("/")
def hello():
    # Asegúrate de usar el nombre correcto
    # de tu cadena de conexión en las variables de entorno
    conn_str = os.environ.get('SQLAZURECONNSTR_DefaultConnection')
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        row = cursor.fetchone()
    return f"Hola desde Azure. Versión de la base de datos: {row[0]}"
