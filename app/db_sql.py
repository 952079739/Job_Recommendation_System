from app import db
from app.create_db import User, Position, Company, Role


def select_user(name, password):
    user = User.query.filter(User.name == name, User.password == password).first()
    return user


def select_user_name(id):
    user = User.query.filter(User.id == id).first()
    return user


def select_position(name):
    position_list = Position.query.filter(Position.name == name).all()
    return position_list


def select_company(id):
    company = Company.query.filter(Company.id == id).first()
    return company


def select_company_two(name, password):
    company = Company.query.filter(Company.name == name, Company.password == password).first()
    return company


def add_user(name, password, email, liking):
    job_role = Role(name='寻找者')
    user = User(name=name, password=password, email=email, like_position=liking,
                role=job_role)
    db.session.add_all(user)
    db.session.commit()


def select_position(p_type):
    positions = Position.query.filter(position_type=p_type).all()
    return positions


def add_position(p_name, p_type, p_treatment, p_place, c_id):
    position = Position(name=p_name, position_type=p_type, position_treatment=p_treatment,
                        position_place=p_place,company_id=c_id)
    db.session.add_all(position)
    db.session.commit()














