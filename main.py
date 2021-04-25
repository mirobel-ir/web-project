from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.users import User
import jobs_api
import datetime
from flask import make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource


start = Flask(__name__)

api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    start.register_blueprint(jobs_api.blueprint)
    start.run()


@app.route('/')
def index():
    session = db_session.create_session()
    ans = []
    jobs = session.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    main()
