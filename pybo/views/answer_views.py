from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')
# answer_views.py 파일이 answer라는 이름의 블루프린트 파일임을 나타냄 

@bp.route('/create/<int:question_id>', methods=('POST',)) # 답변 저장 템플릿이 있는 form 엘리먼트의 method값과 일치해야함
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content'] # name 속성이 'content'인 값
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)# 질문에 대한 답변들
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))