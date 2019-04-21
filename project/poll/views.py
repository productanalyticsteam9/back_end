from flask import render_template, flash, redirect, url_for, session, logging, request, Blueprint
from flask_login import login_user, current_user, login_required, logout_user
from datetime import datetime
import re

from .. import app, db
from ..models import Poll
from .forms import PollForm


poll_blueprint = Blueprint('poll', __name__)


# @poll_blueprint.route("/poll/<uuid>/<poll_uuid>", methods=["GET", "POST"]) # def submit_poll(uuid, poll_uuid):
@poll_blueprint.route("/submit_poll", methods=["GET", "POST"])
@login_required
def submit_poll():
    user = current_user
    form = PollForm(request.form)
    if 'file_urls' not in session or session['file_urls'] == []:
        return redirect(url_for('users.upload'))
    file_urls = session['file_urls']
    
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                poll_text = form.poll_text.data
                poll_uuid = session['poll_uuid']
                uuid = user.uuid
                image_id = list(range(1, len(file_urls)+1))
                image_path = file_urls
                if form.user_tag.data:
                    user_tag = re.findall(r"\b\w+\b", form.user_tag.data)
                else:
                    user_tag = []
                poll = Poll(poll_text=poll_text, poll_uuid=poll_uuid, uuid=uuid, 
                            image_id=image_id, image_path=image_path)
                poll.user_tag = user_tag
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
    
    return render_template('poll.html', form=form, file_urls=file_urls)