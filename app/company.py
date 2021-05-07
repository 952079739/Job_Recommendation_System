import json
import os

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session, send_from_directory

from app.db_sql import *

device = Blueprint('device', __name__)


#@wolfer test
@device.route('/register', methods=['POST', 'GET'])
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
@device.route('/login', methods=['POST', 'GET'])
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
@device.route('/info',methods=['POST'])
def select():
    data = request.form.get('data')
    data = json.loads(data)
    provice_name = data['device_name']
    devices = select_device_province_name(provice_name)
    device = {
        'device_name': devices.device_name,
    }
    return jsonify(device)



@device.route('/logout/', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('/login'))


# 公司职位查询
@device.route('/company-position-select', methods=['POST'])
def info_device_position():
    data = request.form.get('data')
    print(data)
    data = json.loads(data)
    provice_name = data['provice_name']
    device_list = []
    devices = select_devices_all(provice_name)
    for device_infomation in positions:
        device_list.append({
            'device_name': device_infomation.device_name,
         })
        return jsonify(device_list)


# 公司职位增加
@device.route('/SendDate', methods=['POST'])
def form_data():
    data = request.form.get('data')
    data = json.loads(data)
    print(data)
    if data is not None:
        position_name = data['position_name']
        position_type = data['position_type']
        position_treatment = data['position_treatment']
        position_place = data['position_place']
        company = select_company_name(data['company_name'])
        company_id = company.company_id
        add_position(position_name, position_type, position_treatment, position_place, company_id)
        return jsonify({'msg' : "发布成功"})


# 公司职位删除
@device.route('/device-delete', methods=['POST'])
def delete_device():
    data = request.form.get('data')
    data = json.loads(data)
    device_one = data['device_name1']
    device_two = data['device_name2']
    if device_one == device_two:
        delete_device(device_one)
        return jsonify({'msg': "成功删除"})
    return jsonify({'msg':"设备名不一致"})


@device.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    directory = os.path.abspath(filename)  # 获得文件路径
    return send_from_directory(directory, filename, as_attachment=True)