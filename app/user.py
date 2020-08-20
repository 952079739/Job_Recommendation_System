import json

from flask import Blueprint, request, render_template, url_for, jsonify, redirect

from app.db_sql import add_user, select_user

user = Blueprint('user', __name__)


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
            if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(liking) > 0:
                user = select_user(username, password)
                if user is not None:
                    return redirect(url_for('user.login'))
                else:
                    return jsonify(type_information='False')
            return redirect(url_for('user.login'))


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
            user = selcet_user(username, password)
            if user is not None:
                return render_template('login.html')
            else:
                return redirect(url_for('job.index'), jsonify(username=username))




