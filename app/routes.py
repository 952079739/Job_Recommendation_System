from app import app
from app.company import device
from app.job import job
from app.user import user
from flask import url_for, redirect, request, render_template
from werkzeug.exceptions import HTTPException
import json

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(job, url_prefix='/job')
app.register_blueprint(device, url_prefix='/company')


@app.route('/')
def home_page():
    data = request.get_data()
    data = json.load(data)
    name = data.get('username')
    if name is not None:
        return redirect(url_for('/job.index'))
    else:
        return redirect(url_for('/user.login'))


@app.errorhandler(HTTPException)
def handle_bad_request(e):
    index = "job/index"
    return render_template('404.html', index=index), 404


