import json


from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session

from app.db_sql import *


user = Blueprint('user', __name__)


# @wolfer test
# 注册页面,传输数据为json,方式为
@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            password2 =data['password2']
            user_phone = data['phone']
            if len(username) > 0 and len(password) > 0 and len(password2) > 0:
                user = select_user_name(username)
                if user is None:
                    if password == password2:
                        add_user(username, password, user_phone)
                        # return redirect(url_for('user.login'))
                        return jsonify({'msg': "success"})
                    else:
                        return jsonify({'msg':"密码不一致"})
                else:
                    # return jsonify(type_information='False')
                    return jsonify({'msg': "用户名存在"})
            return jsonify(typ_inforamtion='请填写用户名和密码')


# @wolfer test
# 登录页面,传输数据为json,类型为POST
@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            users = select_user(username, password)
            if users is not None:
                return jsonify({'msg': "success"})
            else:
                return jsonify({'msg': "用户名或密码错误"})


# 用户信息修改
@user.route('/update_password', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        return render_template('update_p.html')
    if request.methos == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            user_password = data['password2']
            user = select_user_name(username)
            if user is None:
                if password == user_password:
                    update_user(username, password)
                    return jsonify({'msg': "success"})
            return jsonify({'msg': '用户已存在'})




