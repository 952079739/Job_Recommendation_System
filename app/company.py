import json

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session

from app.db_sql import *

company = Blueprint('company', __name__)


@company.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.data()
        if data is not None:
            data = json.load(data)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            photo_addr = data.get('photo_addr')
            if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(photo_addr) > 0:
                company = select_company(username, password)
                if company is not None:
                    add_user(username, password, email, photo_addr)
                    return redirect(url_for('company.login'))
                else:
                    return jsonify(type_information='False')
            return render_template('register.html')


@company.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.data()
        if data is not None:
            data = json.load(data)
            username = data.get('username')
            password = data.get('password')
            company = select_company(username, password)
            if company is not None:
                session['name'] = username
                return redirect(url_for('company.info'))
            else:
                return render_template('login.html')


@company.route('/info',methods=['GET'])
def select():
    username = session.get('name')
    companys = select_company(username)
    company = {
        'name': companys.company_name,
        'email': companys.company_email,
        'photo_addr': companys.company_photo
    }
    return jsonify(company)


@company.route('/logout/', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('/login'))


@company.route('/SendDate', methods=['POST', 'GET'])
def form_data():
    if request.method == 'GET':
        return redirect(url_for('company.info'))
    if request.method == 'POST':
        data = request.form.data()
        if data is not None:
            position_name = data.get('position_name')
            position_type = data.get('position_type')
            position_treatment = data.get('position_treatment')
            position_place = data.get('position_place')
            company_id = session.get('company_id')
            if len(position_name) > 0 and position_place > 0 and position_type > 0 and position_treatment > 0:
                add_position(position_name, position_type, position_treatment, position_place, company_id)
                return jsonify(type_information='Success')
            else:
                return jsonify(type_information='Flase')
        return jsonify(type_information='Flase')