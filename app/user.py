import json

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session

from app.db_sql import *

user = Blueprint('user', __name__)


# 注册页面,传输数据为json,方式为
@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.get_data()
        if data is not None:
            data = json.load(data)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            liking = data.get('like_position')
            rolename = data.get('role_name')
            if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(liking) > 0 and len(rolename) > 0 :
                user = select_user(username, password)
                if user is not None:
                    add_user(username, password, email, liking, rolename)
                    return redirect(url_for('user.login'))
                else:
                    return jsonify(type_information='False')
            return render_template('register.html')


# 登录页面,传输数据为json,类型为POST
@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.get_data()
        if data is not None:
            data = json.load(data)
            username = data.get('username')
            password = data.get('password')
            users = select_user(username, password)
            if users is not None:
                session['name'] = username
                return redirect(url_for('job.index'))
            else:
                return render_template('login.html')


# 获取该用户信息
@user.route('/select', methods=['GET'])
def select():
    username = session.get('name')
    users = select_user_name(username)
    roles = select_role(users.role_id)
    user = {'username': users.user_name,
             'email': users.user_email,
             'liking': users.like_position,
             'role_name': roles.role_name}
    return jsonify(user)


