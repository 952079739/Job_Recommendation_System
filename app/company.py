import json

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session

from app.db_sql import *

company = Blueprint('company', __name__)

#@wolfer test
@company.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            email = data['email']
            if len(username) > 0 and len(password) > 0 and len(email) > 0:
                company = select_company_name(username)
                if company is None:
                    add_companmy(username, password, email)
                    # return redirect(url_for('company.login'))
                    return jsonify({'msg': "success"})
                else:
                    # return jsonify(type_information='False')
                    return jsonify({'msg': "公司已存在"})
            return render_template('register.html')


#@wolfer test
@company.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            company = select_company_two(username, password)
            if company is not None:
                # session['name'] = username
                # return redirect(url_for('company.info'))
                return jsonify({'msg': "success"})
            else:
                # return render_template('login.html')
                return jsonify({'msg': "公司名或密码错误"})

#@wolfer test
@company.route('/info',methods=['POST'])
def select():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    companys = select_company_name(username)
    company = {
        'company_name': companys.company_name,
        'company_email': companys.company_email
    }
    return jsonify(company)


@company.route('/logout/', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('/login'))

@company.route('/company-position-select', methods=['POST'])
def info_company_position():
    data = request.form.get('data')
    print(data)
    data = json.loads(data)
    username = data['username']
    position_list = []
    company = select_company_name(username)
    if company is not None:
        positions = select_position_company_all(company.company_id)
        for position_infomation in positions:
           position_list.append({
                'position_id': position_infomation.position_id,
                'position_name': position_infomation.position_name,
                'company_name': company.company_name,
                'company_photo': company.company_photo
            })
        return jsonify(position_list)


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