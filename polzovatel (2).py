from data import db_session
import flask
from data.jobs import User
from flask import jsonify, request
import datetime
spisok = ['id', 'surname', 'name', 'age',
          'position', 'speciality',
          'address',
          'about', 'email',
          'hashed_password',
          'modified_date'
way = flask.Blueprint('news_api', __name__, 
                            template_folder='templates')


@way.route('/api/users/<int:job_id>')
def get_job_simp(job_id):
    db_session = db_session.create_session()
    a = db_session.query(User).get(job_id)
    if a:
        return jsonify(
            {
                'user': a.to_dict()
            }
        )
    else:
        return jsonify(
            {
                'user': 'NotFound'
            }
        )


@way.route('/api/users/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_session = db_session.create_session()
    job = db_session.query(User).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_session.delete(job)
    db_session.commit()
    return jsonify({'success': 'OK'})


@way.route('/api/users')
def get_jobs():
    db_session = db_session.create_session()
    jobs = db_session.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict()
                 for item in jobs]
        }
    )


@way.route('/api/users', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in spisok):
        return jsonify({'error': 'Bad request'})
    
    session = db_session.create_session()
    user = User(
        id=request.json['id'],
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        about=request.json['about'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        modified_date=request.json['modified_date']
    )
    if session.query(User).get(user.id):
        return jsonify({'error': 'Id already exists'})
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK'})


@way.route('api/jobs/<int:job_id>', methods=['PUT'])
def change_job(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    if not ('id' in request.json):
        
        return jsonify({'error': 'Bad request'})
    
    db_session = db_session.create_session()
    job = db_session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Wrong ID'})
    
    team_leader=request.json.get('team_leader')
    
    if team_leader:
        job.team_leader = team_leader
    job=request.json.get('job')
    
    if job:
        job.job = job
    work_size=request.json.get('work_size')
    
    if work_size:
        job.work_size = work_size
    collaborators=request.json.get('collaborators')
    
    if start_date:
        job.start_date = start_date
    end_date=request.json.get('end_date')
    
    if end_date:
        job.end_date = end_date
    is_finished=request.json.get('is_finished')

    if collaborators:
        job.collaborators = collaborators
    start_date=request.json.get('start_date')
    
    if is_finished:
        job.is_finished = is_finished
