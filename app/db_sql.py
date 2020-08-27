from app import db
from app.create_db import User, Position, Company, Role


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


def select_company_two(name, password):
    company = Company.query.filter(Company.company_name == name, Company.company_password == password).first()
    return company


def add_user(user_name, password, email, liking, role_name):
    job_role = Role(name=role_name)
    user = User(user_name=user_name, user_password=password, user_email=email, like_position=liking,
                role=job_role)
    db.session.add_all(user)
    db.session.commit()


def select_position(p_type):
    positions = Position.query.filter(Position.position_type == p_type).all()
    return positions


def select_role(id):
    role = Role.query.filter(Role.role_id == id).first()
    return role
#
#
# def add_position(p_name, p_type, p_treatment, p_place, c_id):
#     position = Position(name=p_name, position_type=p_type, position_treatment=p_treatment,
#                         position_place=p_place, company_id=c_id)
#     db.session.add_all(position)
#     db.session.commit()














