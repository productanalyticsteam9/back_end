from flask import render_template, flash, redirect, url_for, session, logging, request, Blueprint
from flask_login import login_user, current_user, login_required, logout_user
from datetime import datetime
import boto3
from ..upload_to_s3.config import S3_BUCKET
import re, itertools, random

from .. import app, db
from ..models import Poll
from .forms import PollForm


poll_blueprint = Blueprint('poll', __name__)

def split_func(a):
    split_a = re.split('{|,|}|! ',a[0])
    return [item for item in split_a if item is not '']


def update_count(polls, poll_votes):
    polls.update().where().values(vote_cnt = poll_votes)
    db.commit()

@poll_blueprint.route("/poll_vote/<poll_uuid>", methods = ['GET', 'POST'])
@login_required
def poll_vote_result(poll_uuid):
    model_tags = []
    form = PollForm(request.form)
    polls = Poll.query.filter_by(poll_uuid=poll_uuid).all()
    poll_texts = [poll.poll_text for poll in polls]
    poll_images = [poll.image_path for poll in polls]
    poll_dates = [poll.post_date for poll in polls]
    poll_votes = [poll.vote_cnt for poll in polls]
    poll_usertags = split_func([poll.user_tag for poll in polls])
    poll_modeltags = split_func([poll.model_tag for poll in polls])
    uuid = [poll.uuid for poll in polls][0]

    return render_template("poll_vote.html",
                           form = form,
                           polls = polls,
                           uuid = uuid,
                           model_tags = model_tags,
                           poll_texts=poll_texts,
                           poll_images=poll_images,
                           poll_dates=poll_dates,
                           poll_usertags=poll_usertags,
                           poll_modeltags=poll_modeltags,
                           poll_votes=poll_votes)



@poll_blueprint.route("/submit_poll", methods=["GET", "POST"])
@login_required
def submit_poll():
    user = current_user
    form = PollForm(request.form)
    if 'file_urls' not in session or session['file_urls'] == []:
        return redirect(url_for('users.upload'))
    file_urls = session['file_urls']

    model_tag_lst = []
    # client = boto3.client('rekognition') # ML model client
    # for url in file_urls:
    #     f_path = url.split('com/')[1].split('?')[0]
    #     response = client.detect_labels(Image={
    #                     'S3Object': {'Bucket': S3_BUCKET,
    #                                     'Name': f_path}
    #                     })
    #     tags = [dic['Name'] for dic in response['Labels']]
    #     model_tag_lst.append(tags)
    # model_tags = random.sample(set(itertools.chain(*model_tag_lst)), 4)
    model_tags = []

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
                            image_id=image_id, image_path=image_path)
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


