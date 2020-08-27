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
        data = request.form.get('data')
        if data is not None:
            data = json.load(data)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            liking = data.get('like_position')
            if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(liking) > 0:
                user = select_user(username, password)
                if user is None:
                    add_user(username, password, email, liking)
                    return redirect(url_for('user.login'))
                else:
                    return jsonify(type_information='False')
            return jsonify(typ_inforamtion='请注册后再登录')


# 登录页面,传输数据为json,类型为POST
@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.load(data)
            username = data.get('username')
            password = data.get('password')
            users = select_user(username, password)
            if users is not None:
                session['name'] = username
                return redirect(url_for('job.index'))
            else:
                return jsonify(type_information='False')


# 获取该用户信息
@user.route('/select', methods=['GET'])
def select():
    username = session.get('name')
    users = select_user_name(username)
    user = {'username': users.user_name,
             'email': users.user_email,
             'liking': users.like_position}
    return jsonify(user)

# 注销用户信息
# @user.route('/loginout', methods=['GET'])
# def logingout:
#     username = session.get('name')
#



