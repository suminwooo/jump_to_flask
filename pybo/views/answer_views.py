from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm 
from ..models import Question, Answer
from ..views.auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')
# answer_views.py 파일이 answer라는 이름의 블루프린트 파일임을 나타냄 


@bp.route('/create/<int:question_id>', methods=('POST',)) 
@login_required
# 답변 저장 템플릿이 있는 form 엘리먼트의 method값과 일치해야함
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        # g.user은 auth_views.py 파일의 @bp.before_app_request 애너테이션으로 만든 로그인한 사용자 정보
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)