import json

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session

from app.db_sql import *

company = Blueprint('company', __name__)


# @wolfer test
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


# @wolfer test
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

# @wolfer test
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


# 公司职位查询
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


# 公司职位增加
@company.route('/SendDate', methods=['POST'])
def form_data():
    data = request.form.get('data')
    data = json.loads(data)
    company_name = data['company_name']
    if data is not None:
        company = select_company_name(company_name)
        position_name = data['position_name']
        position_type = data['position_type']
        position_treatment = data['position_treatment']
        position_place = data['position_place']
        add_position(position_name, position_type, position_treatment, position_place, company.company_id)
        return jsonify({'msg' : "发布成功"})


# 公司职位删除
@company.route('/position-delete', methods=['POST'])
def delete_position_one():
    data = request.form.get('data')
    # print(data)
    data = json.loads(data)
    # print(data)
    position_id = data['position_id']
    if position_id is not None:
         delete_position( position_id)
         return jsonify({'msg': "position_delete"})