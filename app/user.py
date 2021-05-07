import json


from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session

from app.db_sql import *


user = Blueprint('user', __name__)

# @wolfer test
# 注册页面,传输数据为json,方式为
@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            password2 =data['password2']
            if len(username) > 0 and len(password) > 0  and len(password2) > 0:
                user = select_user_name(username)
                if user is None:
                    if password == password2:
                        add_user(username, password)
                        # return redirect(url_for('user.login'))
                        return jsonify({'msg': "success"})
                    else:
                        return jsonify({'msg':"密码不一致"})
                else:
                    # return jsonify(type_information='False')
                    return jsonify({'msg': "用户名存在"})
            return jsonify(typ_inforamtion='请注册后再登录')


# @wolfer test
# 登录页面,传输数据为json,类型为POST
@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            users = select_user(username, password)
            if users is not None:
                return jsonify({'msg': "success"})
            else:
                return jsonify({'msg': "用户名或密码错误"})


# @wolfer test
# 获取该用户信息
@user.route('/select', methods=['POST'])
def select():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
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


#用户所有收藏信息查询
@user.route('/collect-select-all', methods=['POST'])
def info_collect_all():
    data = request.form.get('data')
    print(data)
    data = json.loads(data)
    collect_list = []
    username = data['username']
    print(username)
    users = select_user_name(username)
    collects = select_collect_all(users.user_id)
    print(collects)
    for collect_infomation in collects:
                position = select_position_id(collect_infomation.collecting_position_id)
                company = select_company(position.company_id)
                collect_list.append({
                    'position_id':position.position_id,
                    'position_name':position.position_name,
                    'company_name':company.company_name,
                    'company_photo':company.company_photo
                })
    return  jsonify(collect_list)
 

#用户收藏信息查询
@user.route('/collect-select', methods=['POST'])
def info_collect():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    position_id = data['position_id']
    users = select_user_name(username)
    collects = select_collect(users.user_id,position_id)
    if collects is not None:
        return jsonify({'msg': "yes"})
    else:
        return jsonify({'msg': "no"})

# 用户收藏
@user.route('/collect-position', methods=['POST'])
def position_collect():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    position_id = data['position_id']
    users = select_user_name(username)
    if users is not None:
         add_collect(users.user_id, position_id)
         return jsonify({'msg': "collect_have"})

# 取消收藏
@user.route('/collect-delete', methods=['POST'])
def delete_collect_one():
    data = request.form.get('data')
    data = json.loads(data)
    print(data)
    username = data['username']
    position_id = data['position_id']
    users = select_user_name(username)
    if users is not None:
         delete_collect(users.user_id, position_id)
         return jsonify({'msg': "collect_delete"})


# 用户评分
@user.route('/score-add', methods=['POST'])
def Scoring():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    users = select_user_name(username)
    position_id = data['position_id']
    score = data['score']
    postions = select_position_id(position_id)
    # list = [{'user_id': users.user_id,
    #          'position_id': position_id,
    #          'score': score,
    #          'position_type': postions.position_type}]
    if len(username) > 0 and len(position_id) > 0 and len(score) > 0:
        add_score(score, position_id, users.user_id)
        return jsonify({'msg': "success"})

# 用户评分信息查询
@user.route('/score-select', methods=['POST'])
def info_score():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    position_id = data['position_id']
    users = select_user_name(username)
    score = select_score(users.user_id, position_id)
    if score is not None:
        return jsonify({'msg': score.position_appraisal})
    else:
        return jsonify({'msg': "no"})


# 用户所有评分查询
@user.route('/score-select-all', methods=['POST'])
def info_score_all():
    data = request.form.get('data')
    data = json.loads(data)
    username = data['username']
    score_list = []
    users = select_user_name(username)
    scores = select_score_all(users.user_id)
    print(scores)
    for score_infomation in scores:
                position = select_position_id(score_infomation.position_id)
                company = select_company(position.company_id)
                score_list.append({
                    'position_score':score_infomation.position_appraisal,
                    'position_id': position.position_id,
                    'position_name': position.position_name,
                    'company_name': company.company_name,
                    'company_photo': company.company_photo
                })
    return jsonify(score_list)


# 职位评分总查询
@user.route('/score-position-select-all', methods=['POST'])
def info_position_score_all():
    data = request.form.get('data')
    print(data)
    data = json.loads(data)
    position_id = data['position_id']
    scores = select_position_score_all(position_id)
    score_list = []
    print(scores)
    for score_infomation in scores:
        score_list.append({'score':score_infomation.position_appraisal})
    return jsonify(score_list)


# 用户信息修改
@user.route('/add_user', methods=['POST'])
def add_user():
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            userphone = data['user_phone']
            user = select_user_name(username)
            if user is None:
                update_user(username, password, userphone)
                return jsonify({'msg': "success"})
            return jsonify({'msg':'用户已存在'})


@user.route('/delete_user', methods=['POST'])
def delete_user():
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            user = select_user_name(username)
            if user is not None:
                delete_user(username)
                return jsonify({'msg': "success"})
            return jsonify({'msg':'用户不存在'})

