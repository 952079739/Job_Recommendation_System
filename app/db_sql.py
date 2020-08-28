from app import db
from app.create_db import User, Position, Company, Collecting, Appraisal


def select_user(name, password):
    user = User.query.filter(User.user_name == name, User.user_password == password).first()
    return user


def select_user_name(name):
    user = User.query.filter(User.user_name == name).first()
    return user


def select_position(name):
    position_list = Position.query.filter(Position.position_name == name).all()
    return position_list


def select_company(id):
    company = Company.query.filter(Company.company_id == id).first()
    return company

def select_company_name(name):
    company = Company.query.filter(Company.company_name == name).first()
    return company

def select_company_two(name, password):
    company = Company.query.filter(Company.company_name == name, Company.company_password == password).first()
    return company


def add_user(user_name, password, email, liking):
    user = User(user_name=user_name, user_password=password, user_email=email, like_position=liking)
    db.session.add_all([user])
    db.session.commit()

def add_companmy(username, password, email):
    company = Company(company_name=username, company_password=password, company_email=email)
    db.session.add(company)
    db.session.commit()

def add_position(position_name, position_type, position_treatment, position_place, company_id):
    position = Position(position_name=position_name, position_type=position_type,
                        position_treatment=position_treatment, position_place=position_place, company_id=company_id)
    db.session.add_all([position])
    db.session.commit()


def select_position(p_type):
    positions = Position.query.filter(Position.position_type == p_type).all()
    return positions


def add_collect(id):
    collect_one = Collecting(collecting_position_id=id)
    db.session.add_all([collect_one])
    db.session.commit()


def select_collect(id):
    collecting_list = Collecting.query.filter(Collecting.user_id == id)
    return collecting_list


def select_position_id(id):
    position_list = Position.query.filter(Position.position_id == id).first()
    return position_list


def add_score(company_appraisal, company_id, user_id):
    score_one = Appraisal(company_appraisal=company_appraisal, company_id=company_id,
                          user_id=user_id)
    db.session.add_all([score_one])
    db.session.commit()


#
# def add_position(p_name, p_type, p_treatment, p_place, c_id):
#     position = Position(name=p_name, position_type=p_type, position_treatment=p_treatment,
#                         position_place=p_place, company_id=c_id)
#     db.session.add_all([position])
#     db.session.commit()
