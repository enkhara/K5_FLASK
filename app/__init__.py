from flask import Flask
#permite que esta aplicacion se relacione
app = Flask(__name__, instance_relative_config=True)
#hay que ponerlo aqui por que si no esta creada petara1
from app import views

#para que coja el fixer config.py
app.config.from_object('config')