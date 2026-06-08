from models.db import db
from config.config import DATABASE_CONNECTION_URI
from flask import Flask

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)
# aca tenemos que agregar:
#with app.app_context():
    #from models.productos import Producto.... flask necesita que el modelo este cargado en el contexto. 
    #cambiar cuando ya lo tengamos listo
    #db.create_all()

if __name__=="__main__":
    app.run(debug=True)
