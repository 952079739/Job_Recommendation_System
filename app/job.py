import json

from flask import Blueprint, request, jsonify, render_template, session

from app.db_sql import *
from app.recommended import recommend

job = Blueprint('job', __name__)


# 返回job页面,返回页面为job.html,返回数据为json
@job.route('/index')
def index():
    username = session.get('name')
    positions = Position.query.all()
    # position = select_position('python')
    # position_name = position.position_treatment
    position_list = []
    for position in positions:
        company = select_company(position.company_id)
        position_list.append({'name': position.name,
                              'treatment': position.position_treatment,
                              'company_name': company.name,
                              'username': username})
    return jsonify(position_list)


# 查询为职位为python的job，返回job.html,type为职位类型,路由举例：/job/python
@job.route('/<string:type>', methods=['GET'])
def job_python():
    job_type = type
    username = session.get('name')
    job_information_all = select_position(job_type)
    position_list = []
    for job_information in job_information_all:
        company = select_company(job_information.company_id)
        position_list.append({'name': job_information.name,
                              'treatment': job_information.position_treatment,
                              'company_name': company.name,
                              'username': username})
    return jsonify(position_list)

#@wolfer test
# 测试接口,返回所有职业
@job.route('/test', methods=['GET'])
def test():
    positions = Position.query.all()
    position_list = []
    for job_information in positions:
        company = select_company(job_information.company_id)
        position_list.append({
                              'position_id': job_information.position_id,
                              'position_name': job_information.position_name,
                              'position_treatment': job_information.position_treatment,
                              'position_place': job_information.position_place,
                              'position_type':job_information.position_type,
                              'company_name': company.company_name,
                              'company_email': company.company_email,
                              'company_photo': company.company_photo})
    return jsonify(position_list)

@job.route('/recommend', methods=['POST'])
def recommend_list():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    print(data)
    user = select_user_name(username)
    recommends = recommend(str(user.user_id))
    print(recommends)
    position_list = []
    for recomm in recommends:
        positions = select_position_id(recomm[0])
        company = select_company(positions.company_id)
        position_list.append({'position_name': positions.position_name,
                              'position_id':positions.position_id,
                              'company_photo': company.company_photo,
                              'company_name': company.company_name})
    return jsonify(position_list)


# 收藏路由
# @job.route('/collect', methods=['POST'])
# def collecting():
#     username = session.get('name')
#     data = request.get('data')
#     if username is not None:
#         json_data = json.load(data)
#         positon_id = json_data.get['position_id']
#         add_collect(positon_id)
#         return 'success'


# 评分路由
# @job.route('/Scoring', methods=['POST'])
# def Scoring():
#     data = request.get_data('data')
#     json_data = json.load(data)
#     score = json_data.get('score')
#     company_id = json_data.get('company_id')
#     user_id = session.get('user_id')
#     if score is not None:
#         add_score(score, company_id, user_id)
#         return 'Sucess'
#     else:
#         return 'Fail'


