from flask import Flask,redirect,g,session,request
from flask_sqlalchemy import SQLAlchemy
from config import config,dev,pro
from account import accountBlue
from goods import goodsBlue
# db
db = SQLAlchemy()

def creatApp():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(accountBlue)
    app.register_blueprint(goodsBlue)

    # 配置
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_01?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    return app

