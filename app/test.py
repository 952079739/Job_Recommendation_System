from app.create_db import *

# 添加测试数据
test_role_one = Role(role_name='寻找者')
test_role_two = Role(role_name='职员')

test_user_one = User(user_name='li', user_email='952079739@qq.com', user_password='123456',
                     like_position='python', roles=test_role_one)
test_user_two = User(user_name='huang', user_email='9123123123@123.com', user_password='945685',
                     like_position='java', roles=test_role_two)
test_user_three = User(user_name='qiu', user_email='885858558@169.com', user_password='a789456123',
                       like_position='java', roles=test_role_one)

test_company_one = Company(company_name='美团', company_email='952079739@qq.com', company_password='123456', company_photo='photo')
test_company_two = Company(company_name='阿里巴巴', company_email='9123123123@123.com', company_password='945685', company_photo='photo')

test_position_one = Position(position_name='系统运维', position_type='python',
                             position_treatment='零食下午茶,年终奖,员工旅游,五险一金,节日福利,定期体检,带薪年假',
                             position_place='成都·武侯区·新会展中心', company=test_company_one)
test_position_two = Position(position_name='Python开发', position_type='python',
                             position_treatment='零食下午茶,年终奖,员工旅游,五险一金,节日福利,定期体检,带薪年假',
                             position_place='成都·武侯区·新会展中心', company=test_company_one)
db.session.add_all([test_role_one, test_role_two])
db.session.add_all([test_user_one, test_user_two])
db.session.add_all([test_user_three, test_company_one, test_company_two])
db.session.add_all([test_position_one, test_position_two])
db.session.commit()

