from app import db
from app.create_db import User, Device, Ddata, Manager


def select_user(name, password):
    user = User.query.filter(User.user_name == name, User.user_password == password).first()
    return user


def select_manager(name, password):
    manager = Manager.query.filter(Manager.manager_name == name, Manager.manager_password == password).first()
    return manager

def select_user_all():
    users = User.query.all()
    return users


def select_user_name(name):
    user = User.query.filter(User.user_name == name).first()
    return user


def delete_user(username):
    user = User.query.filter_by(User.user_name == username).first()
    db.session.delete(user)
    db.session.commit()


def select_device_all():
    device_list = Device.query.all()
    return device_list


def select_devices_province(province):
    device_list = Device.query.filter(Device.device_province == province).all()
    return device_list


def select_device_name(name):
    device = Device.query.filter(Device.device_name == name).first()
    return device


def select_device_data(device_id):
    device_data = Ddata.query.filter(Ddata.device_id == device_id).all()
    return device_data


def add_user_one(name, password, phone):
    user = User(user_name=name, user_password=password, user_phone=phone)
    db.session.add_all([user])
    db.session.commit()


def update_user(user_name, password):
    user = User.query.filter(User.user_name == user_name).first()
    user.user_password = password
    db.session.commit()


def add_data(device_id, cpu, mem, flow, time):
    device_data = Ddata.query.filter(Ddata.device_id == device_id).first()
    device_data.data_cpu = cpu
    device_data.data_memory = mem
    device_data.data_flow = flow
    device_data.data_time = time
    db.session.commit()


def add_device(device_name, device_province, device_ip, device_user, device_password):
    device = Device(device_name=device_name, device_province=device_province, device_ip=device_ip,
                    device_user=device_user, device_password=device_password)
    db.session.add_all([device])
    db.session.commit()


def create_data(device_id):
    data = Ddata(device_id=device_id)
    db.session.add_all([data])
    db.session.commit()


#
# def add_position(p_name, p_type, p_treatment, p_place, c_id):
#     position = Position(name=p_name, position_type=p_type, position_treatment=p_treatment,
#                         position_place=p_place, company_id=c_id)
#     db.session.add_all([position])
#     db.session.commit()

