from app import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    user = db.relationship('User', backref='roles')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)
    like_position = db.Column(db.String(100), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    appraisal = db.relationship('Appraisal', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=False)
    position = db.relationship('Position', backref='company')
    appraisal = db.relationship('Appraisal', backref='company')

    def __repr__(self):
        return '<Company {}>'.format(self.name)


class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    position_type = db.Column(db.String(100), unique=False)
    position_treatment = db.Column(db.String(200), nullable=True)
    position_place = db.Column(db.String(200), unique=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Position {}>'.format(self.name)


class Appraisal(db.Model):
    __tablename__ = 'appraisals'
    id = db.Column(db.Integer, primary_key=True)
    company_appraisal = db.Column(db.Integer, unique=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


if __name__ == '__main__':
    # 创建表
    # db.drop_all()
    # db.create_all()
    # 创建测试数据
    # test_role_one = Role(name='寻找者')
    # test_role_two = Role(name='职员')
    #
    # test_user_one = User(name='li', email='952079739@qq.com', password='123456',
    #                      like_position='python', roles=test_role_one)
    # test_user_two = User(name='huang', email='9123123123@123.com', password='945685',
    #                      like_position='java', roles=test_role_two)
    # test_user_three = User(name='qiu', email='885858558@169.com', password='a789456123',
    #                        like_position='java', roles=test_role_one)
    #
    # test_company_one = Company(name='美团', email='952079739@qq.com', password='123456')
    # test_company_two = Company(name='阿里巴巴', email='9123123123@123.com', password='945685')
    #
    # test_position_one = Position(name='系统运维', position_type='python',
    #                              position_treatment='零食下午茶,年终奖,员工旅游,五险一金,节日福利,定期体检,带薪年假',
    #                              position_place='成都·武侯区·新会展中心', company=test_company_one)
    # test_position_two = Position(name='Python开发', position_type='python',
    #                              position_treatment='零食下午茶,年终奖,员工旅游,五险一金,节日福利,定期体检,带薪年假',
    #                              position_place='成都·武侯区·新会展中心', company=test_company_one)
    # db.session.add_all([test_role_one, test_role_two])
    # db.session.add_all([test_user_one, test_user_two])
    # db.session.add_all([test_user_three, test_company_one])
    # db.session.add_all([test_position_one, test_position_two])
    # db.session.commit()
    user = User.query.filter(User.name == 'li').first()









