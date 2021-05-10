from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True)
    user_password = db.Column(db.String(100), unique=True)
    user_phone = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.user_name)


class Manager(db.Model):
    __tablename__ = 'manager'
    __table_args__ = {'extend_existing': True}
    manager_id = db.Column(db.Integer, primary_key=True)
    manager_name = db.Column(db.String(100), unique=True)
    manager_password = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return '<Manager {}>'.format(self.manager_name)


class Device(db.Model):
    __tablename__ = 'device'
    __table_args__ = {'extend_existing': True}
    device_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100), unique=False)
    device_province = db.Column(db.String(100), unique=False)
    device_ip = db.Column(db.String(200), unique=True)
    device_user = db.Column(db.String(200), unique=False)
    device_password = db.Column(db.String(100), unique=False)
    data = db.relationship('Ddata', backref='device')

    def __repr__(self):
        return '<Device {}>'.format(self.device_name)


class Ddata(db.Model):
    __tablename__ = 'device_data'
    __table_args__ = {'extend_existing': True}
    data_id = db.Column(db.Integer, primary_key=True)
    data_cpu = db.Column(db.String(100), nullable=True)
    data_memory = db.Column(db.String(100), nullable=True)
    data_flow = db.Column(db.String(100), nullable=True)
    data_time = db.Column(db.String(100), nullable=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.device_id'))


