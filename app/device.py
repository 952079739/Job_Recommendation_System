import json
import os

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session, send_from_directory
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from app.db_sql import *
from app.connet import upload

device = Blueprint('device', __name__)


# @wolfer test
@device.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            device_name = data['device_name']
            province = data['province']
            device_ip = data['device_ip']
            device_user = data['username']
            device_password = data['password']
            if len(device_name) > 0 and len(province) > 0 and len(device_ip) > 0:
                device = select_device_name(device_name)
                if device is None:
                    add_device(device_name, province, device_ip, device_user, device_password)
                    device_data = select_device_name(device_name)
                    create_data(device_data.device_id)
                    # upload(host=device_ip, port=22, username=device_user, password=device_password)
                    return jsonify({'msg': "success"})
                else:
                    # return jsonify(type_information='False')
                    return jsonify({'msg': "设备已存在"})
            return jsonify({'msg': "请填写完所有数据"})


# @wolfer test
@device.route('/info', methods=['GET'])
def select():
    devices = select_device_all()
    device_list = []
    for device in devices:
        device_list.append({
            'device_name': device.device_name,
            'province': device.device_province,
            'device_ip': device.device_ip,
            'device_id': device.device_id,
        })

    return render_template('device_info.html', devicelist=device_list)


@device.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('login.html')


# 公司职位查询
@device.route('/<string:province>', methods=['POST'])
def info_device_province(province):
    provice_name = province
    device_list = []
    devices = select_devices_province(provice_name)
    for device in devices:
        device_list.append({
            'device_name': device.device_name,
            'province': device.device_province,
            'device_ip': device.device_ip,
            'device_id': device.device_id,
         })
    return render_template('device_info.html', devicelist=device_list)


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
    return jsonify({'msg': "设备名不一致"})


@device.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    directory = os.getcwd() + '/' + 'templates' + '/' + 'static'
    return send_from_directory(directory, filename, as_attachment=True)


def cpu_base(x_list, y_list) ->Bar:
    c = (
        Bar()
        .add_xaxis(x_list)
        .add_yaxis('CPU', y_list)
        .set_global_opts(title_opts=opts.TitleOpts(title="CPU", subtitle="超过0.8需要密切注意"))
    )
    return c


@device.route('/cpu/<int:device_id>', methods=['GET'])
def cpu(device_id):
    session['device_id'] = device_id
    return render_template('cpu.html')


@device.route('/cpu', methods=['GET'])
def send_cpu():
    device_id = session['device_id']
    data = select_device_data(device_id)
    cpu_list = []
    time_list = []
    for cpu in data:
        cpu_list.append(float(cpu.data_cpu))
        time_list.append(int(cpu.data_time))
    c = cpu_base(time_list, cpu_list)
    return c.dump_options_with_quotes()


def mem_base(x_list, y_list) ->Bar:
    c = (
        Bar()
        .add_xaxis(x_list)
        .add_yaxis('Memory', y_list)
        .set_global_opts(title_opts=opts.TitleOpts(title="Memory", subtitle="超过50需要密切注意"))
    )
    return c


@device.route('/memory/<int:device_id>', methods=['GET'])
def mem(device_id):
    session['device_id'] = device_id
    return render_template('mem.html')


@device.route('/memory', methods=['GET'])
def send_mem():
    device_id = session['device_id']
    data = select_device_data(device_id)
    mem_list = []
    time_list = []
    for mem in data:
        mem_list.append(float(mem.data_memory))
        time_list.append(int(mem.data_time))
    c = mem_base(time_list, mem_list)
    return c.dump_options_with_quotes()


def flow_base(x_list, y_list) ->Bar:
    c = (
        Bar()
        .add_xaxis(x_list)
        .add_yaxis('FLOW', y_list)
        .set_global_opts(title_opts=opts.TitleOpts(title="flow", subtitle="超过50000需要密切注意"))
    )
    return c


@device.route('/flow/<int:device_id>', methods=['GET'])
def flow(device_id):
    session['device_id'] = device_id
    return render_template('flow.html')


@device.route('/flow', methods=['GET'])
def send_flow():
    device_id = session['device_id']
    data = select_device_data(device_id)
    flow_list = []
    time_list = []
    for flow in data:
        flow_list.append(float(flow.data_flow))
        time_list.append(int(flow.data_time))
    c = flow_base(time_list, flow_list)
    return c.dump_options_with_quotes()