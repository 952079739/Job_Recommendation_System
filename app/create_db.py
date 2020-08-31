from app import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True)
    user_email = db.Column(db.String(100), unique=True)
    user_password = db.Column(db.String(100), unique=True)
    like_position = db.Column(db.String(100), nullable=True)
    appraisal = db.relationship('Appraisal', backref='users')
    collecting = db.relationship('Collecting', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.user_name)


class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = {'extend_existing': True}
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), unique=True)
    company_email = db.Column(db.String(100), unique=True)
    company_photo = db.Column(db.String(100), unique=False)
    company_password = db.Column(db.String(100), unique=False)
    position = db.relationship('Position', backref='company')

    def __repr__(self):
        return '<Company {}>'.format(self.company_name)


class Position(db.Model):
    __tablename__ = 'position'
    __table_args__ = {'extend_existing': True}
    position_id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(100), unique=True)
    position_type = db.Column(db.String(100), unique=False)
    position_treatment = db.Column(db.String(200), nullable=True)
    position_place = db.Column(db.String(200), unique=False)
    company_name = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    appraisal = db.relationship('Appraisal', backref='position')

    def __repr__(self):
        return '<Position {}>'.format(self.position_name)


class Appraisal(db.Model):
    __tablename__ = 'appraisals'
    __table_args__ = {'extend_existing': True}
    appraisal_id = db.Column(db.Integer, primary_key=True)
    position_appraisal = db.Column(db.String(50), unique=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.position_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


class Collecting(db.Model):
    __tablename__ = 'collecting'
    __table_args__ = {'extend_existing': True}
    collecting_id = db.Column(db.Integer, primary_key=True)
    collecting_position_id = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

