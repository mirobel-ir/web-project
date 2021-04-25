from data import db_session
import flask
from data.jobs import Jobs
from flask import jsonify, request
import datetime

spisok = [['id', 'team_leader', 'job',
           'work_size', 'end_date', 'start_date',
           'collaborators', 'is_finished']
way = flask.Blueprint('news_api',
                            __name__, 
                            template_folder='templates')


@way.route('/api/jobs/<int:job_id>')
def get_job_simp(job_id):
    db_session = db_session.create_session()
    a = db_session.query(Jobs).get(job_id)
    if a:
        return jsonify(
            {
                'job': a.to_dict()
            }
        )
    else:
        return jsonify(
            {
                'job': 'NotFound'
            }
        )


@way.route('/api/jobs')
def get_jobs():
    db_session = db_session.create_session()
    jobs = db_session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict()
                 for item in jobs]
        }
    )


@way.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in spisok):
        return jsonify({'error': 'Bad request'})
    db_session = db_session.create_session()
    job = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished']
    )
    if db_session.query(Jobs).get(job.id):
        return jsonify({'error': 'Id already exists'})
    db_session.add(job)
    db_session.commit()
    return jsonify({'success': 'OK'})


@way.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_session = db_session.create_session()
    job = db_session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_session.delete(job)
    db_session.commit()
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
    # part 2
    if team_leader:
        job.team_leader = team_leader
    job=request.json.get('job')
    
    if job:
        job.job = job
    work_size=request.json.get('work_size')
    if work_size:
        job.work_size = work_size
        
    collaborators=request.json.get('collaborators')
    if collaborators:
        job.collaborators = collaborators
    #part 3
    start_date=request.json.get('start_date')
    if start_date:
        job.start_date = start_date
        
    end_date=request.json.get('end_date')
    if end_date:
        job.end_date = end_date
    is_finished=request.json.get('is_finished')
    if is_finished:
        job.is_finished = is_finished
