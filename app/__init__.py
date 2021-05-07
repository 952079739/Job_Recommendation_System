import pymysql

from flask_sqlalchemy import SQLAlchemy
from app.util import Redis
from flask import Flask
from flask_cors import *

app = Flask(__name__)

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/' \
                                        'device?charset=utf8mb4'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Redis数据库配置
app.config['REDIS_HOST'] = "127.0.0.1"  # redis数据库地址
app.config['REDIS_PORT'] = 6379   # redis 端口号
app.config['REDIS_DB'] = 0  # 数据库名
app.config['REDIS_EXPIRE'] = 60  # redis 过期时间60秒

db = SQLAlchemy(app)
app.secret_key = '123456'

app.config['JSON_AS_ASCII'] = False

CORS(app, supports_credentials=True)

from app import routes

