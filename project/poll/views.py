from flask import render_template, flash, redirect, url_for, session, logging, request, Blueprint, jsonify
from flask_login import login_user, current_user, login_required, logout_user
from datetime import datetime
import boto3
from ..upload_to_s3.config import S3_BUCKET
import re, itertools, random, json

from .. import app, db
from ..models import Poll, Voted_Poll
from .forms import PollForm
from sqlalchemy import and_


poll_blueprint = Blueprint('poll', __name__)

def split_func(a):
    split_a = re.split('{|,|}|! ',a)
    return [item for item in split_a if item is not '']


@poll_blueprint.route("/poll_vote/<poll_uuid>", methods=['GET', 'POST'])
@login_required
def poll_vote_result(poll_uuid):
    poll = Poll.query.filter_by(poll_uuid=poll_uuid).first()
    poll_usertags = split_func(poll.user_tag)
    poll_modeltags = split_func(poll.model_tag)

    return render_template("poll_vote.html",
                           uuid=current_user.uuid,
                           poll_uuid=poll_uuid,
                           poll_text=poll.poll_text,
                           poll_images=poll.image_path,
                           poll_usertags=poll_usertags,
                           poll_modeltags=poll_modeltags,
                           poll_votes=poll.vote_cnt)


@poll_blueprint.route("/upvote/<poll_uuid>/<image_id>", methods=['GET', 'POST'])
@login_required
def upvote(poll_uuid, image_id):
    try:
        poll = Poll.query.filter_by(poll_uuid=poll_uuid).first()
        voted = Voted_Poll.query.filter_by(uuid=current_user.uuid).first()
        voted_polls = voted.voted_polls
        if poll.poll_uuid not in voted_polls:
            votes = poll.vote_cnt
            votes[int(image_id)-1] += 1
            voted_polls.append(poll.poll_uuid)
            db.session.query(Poll).filter_by(poll_uuid=poll_uuid).update({Poll.vote_cnt: votes})
            db.session.query(Voted_Poll).filter_by(uuid=current_user.uuid).update({Voted_Poll.voted_polls: voted_polls})
            db.session.commit()
            flash("Thank you for voting!", 'success')
        else:
            flash("You have voted, thank you for participating.", "success")
    except Exception as e:
        db.session.rollback()
        flash(e, 'error')

    return redirect(url_for("poll.poll_vote_result", poll_uuid=poll_uuid))


@poll_blueprint.route("/submit_poll", methods=["GET", "POST"])
@login_required
def submit_poll():
    user = current_user
    form = PollForm(request.form)
    if 'file_urls' not in session or session['file_urls'] == []:
        return redirect(url_for('users.upload'))
    file_urls = session['file_urls']

    model_tag_lst = []
    client = boto3.client('rekognition') # ML model client
    for url in file_urls:
        f_path = url.split('com/')[1].split('?')[0]
        response = client.detect_labels(Image={
                        'S3Object': {'Bucket': S3_BUCKET,
                                        'Name': f_path}
                        })
        tags = [dic['Name'] for dic in response['Labels']]
        model_tag_lst.append(tags)
    model_tags = random.sample(set(itertools.chain(*model_tag_lst)), 4)
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                poll_text = form.poll_text.data
                poll_uuid = session['poll_uuid']
                uuid = user.uuid
                id_name_dict, cnt = {}, 1
                for url in file_urls:
                    f_name = url.split('?')[0].split('/')[-1]
                    id_name_dict[cnt] = f_name
                    cnt += 1

                image_id = id_name_dict
                image_path = file_urls
                if form.user_tag.data:
                    user_tag = re.findall(r"\b\w+\b", form.user_tag.data)
                else:
                    user_tag = []
                
                poll = Poll(poll_text=poll_text, poll_uuid=poll_uuid, uuid=uuid,
                            image_id=image_id, image_path=image_path, user_tag=user_tag,
                            model_tag=model_tags, vote_cnt=[0]*len(image_path))
                
                voted = Voted_Poll.query.filter_by(uuid=uuid).first()
                if not voted:
                    voted_poll = Voted_Poll(uuid=uuid, voted_polls=[])
                    db.session.add(voted_poll)

                poll.user_tag = user_tag
                poll.model_tag = model_tags
                db.session.add(poll)
                db.session.commit()
                session.pop('file_urls', None)
                session.pop('poll_uuid', None)
                flash("Thank you for submitting your poll!", 'success')
            except Exception as e:
                db.session.rollback()
                flash(e, 'error')
        else:
            flash("Sorry, the contents you entered do not conform to our standards.", 'info')

    return render_template('poll.html', form=form, file_urls=file_urls, model_tags=model_tags, uuid=user.uuid)


