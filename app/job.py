import json

from flask import Blueprint, request, jsonify, render_template

from app.create_db import Position
from app.db_sql import select_company, select_position

job = Blueprint('job', __name__)


# 返回job页面,返回页面为job.html,返回数据为json
@job.route('/index')
def index():
    data = request.get_data()
    data = json.load(data)
    name = data.get('username')
    positions = Position.query.all()
    # position = select_position('python')
    # position_name = position.position_treatment
    position_list = []
    for position in positions:
        company = select_company(position.company_id)
        position_list.append({'name': position.name,
                              'treatment': position.position_treatment,
                              'company_name': company.name})
    return jsonify(position_list)


# 查询为职位为python的job，返回job.html
@job.route('/python', methods=['GET'])
def job_python():
    job_data = request.get_data()
    job_type = json.load(job_data)
    job_python = job_type.get('type')
    username = job_type.get('username')
    job_information_all = select_position(job_python)
    position_list = []
    company_list = []
    for job_information in job_information_all:
        company = select_company(job_information.company_id)
        company_list.append({company.name})
        position_list.append({'name': job_information.name,
                              'treatment': job_information.position_treatment,
                              })
    return render_template('job.html', jsonify(username=username, p_list=position_list, c_list=company_list))


# 测试接口,返回所有职业
@job.route('/test', methods=['GET'])
def test():
    positions = Position.query.all()
    position_list = []
    for job_information in positions:
        company = select_company(job_information.company_id)
        position_list.append({'position_name': job_information.name,
                              'treatment': job_information.position_treatment,
                             'company_name': company.name})
    return jsonify(position_list)

