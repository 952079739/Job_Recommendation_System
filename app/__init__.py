<<<<<<< HEAD
import pymysql

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import *

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/job?charset=utf8mb4'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.secret_key = 123456

app.config['JSON_AS_ASCII'] = False

CORS(app, supports_credentials=True)

from app import routes

=======
import pymysql

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import *

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/job?charset=utf8mb4'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.secret_key = '123456'

app.config['JSON_AS_ASCII'] = False

CORS(app, supports_credentials=True)

from app import routes

>>>>>>> 690208798db77a2678433b55c333e897bfa8ca19
