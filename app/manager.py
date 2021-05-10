import json

from flask import Blueprint, request, jsonify, render_template, session

from app.db_sql import *


manager = Blueprint('manager', __name__)


@manager.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('manage.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            users = select_manager(username, password)
            if users is not None:
                return jsonify({'msg': "success"})
            else:
                return jsonify({'msg': "用户名或密码错误"})


@manager.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        return render_template('delete_user.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            users = select_user_name(username)
            if users is not None:
                delete_user(username)
                return jsonify({'msg':"success delete"})
            else:
                return jsonify({'msg': "该用户不存在"})


@manager.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            password2 = data['password2']
            user_phone = data['phone']
            if len(username) > 0 and len(password) > 0 and len(password2) > 0:
                user = select_user_name(username)
                if user is None:
                    if password == password2:
                        add_user_one(username, password, user_phone)
                        # return redirect(url_for('user.login'))
                        return jsonify({'msg': "success"})
                    else:
                        return jsonify({'msg': "密码不一致"})
                else:
                    # return jsonify(type_information='False')
                    return jsonify({'msg': "用户名存在"})
            return jsonify({'msg':'请填写用户名和密码'})


@manager.route('/info', methods=['GET'])
def user_info():
    users = select_user_all()
    user_list = []
    for user in users:
        user_list.append({
            'user_name': user.user_name,
            'user_phone': user.user_phone,
            'user_password': user.user_password,
        })

    return render_template('user_info.html', userlist=user_list)