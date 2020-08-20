from app import app
from app.job import job


app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(job, url_prefix='/job')
