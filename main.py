from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
import os

os.system('cls')

app = Flask(__name__)
app.config.from_pyfile('config.py')

csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

''' CONTEÚDO SITE '''
from views_home import *
from views_user  import *

if __name__ == '__main__':
    #app.run(ssl_context="adhoc", host='0.0.0.0', port=25565, debug=True)
    app.run(host='0.0.0.0', port=25565, debug=True)