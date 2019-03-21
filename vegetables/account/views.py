from flask import Flask,Blueprint,redirect,url_for,request,session,g,render_template,flash,get_flashed_messages,jsonify
import json,string

accountBlue = Blueprint('accountBlue',__name__)

@accountBlue.route('/login')
def login():
    session['user'] = '123'
    # db操作
    from .models import Role, db
    array = []
    r = Role.query
    if r is not None:
        for row in r:
            # print(row.id, row.name)
            dic = {'id':row.id,'name':row.name}
            array.append(dic)
    else:
        print('none')
    print(r)

    return jsonify(array)


class User(object):
    __slots__ = ('id','name')
    def __init__(self,sid,name):
        self.id = sid
        self.name = name

@accountBlue.route('/account')
def account():
    from .models import Role, db
    u = User(1,'wyy123')
    for key in u.__dir__():
        if not key.startswith('__'):
            print(key)
            print(u.__getattribute__(key))


    return 'account'

@accountBlue.route('/account/add')
def accountAdd():
    from .models import Role, db

    r = Role('wyy123')
    db.session.add(r)
    db.session.commit()
    print(r.__dict__)

    return 'account_add'