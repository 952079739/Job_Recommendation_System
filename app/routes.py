from flask import redirect, url_for
from app import app
from app.device import device
from app.job import job
from app.user import user
from app.manager import manager


app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(job, url_prefix='/job')
app.register_blueprint(device, url_prefix='/device')
app.register_blueprint(manager, url_prefix='/manager')


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('user.login'))







