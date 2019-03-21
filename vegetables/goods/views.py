from flask import Flask,Blueprint,redirect,url_for,request,session,g,render_template,flash,get_flashed_messages,jsonify
import json,string

goodsBlue = Blueprint('goodsBlue',__name__)

@goodsBlue.route('/goods')
def getGoods():
    return 'goods'