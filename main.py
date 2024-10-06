from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig  # ou ProductionConfig, dependendo do ambiente
import os

os.system('cls')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig) # ou ProductionConfig
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

''' CONTEÚDO SITE '''
from views_home import *
from views_user  import *

if __name__ == '__main__':
    #app.run(ssl_context="adhoc", host='0.0.0.0', port=25565, debug=True)
    app.run(host='0.0.0.0', port=9880, debug=True, threaded=True)