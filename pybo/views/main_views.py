from flask import Blueprint, render_template

from pybo.models import Question

# 블루 프린트 객체 생성
# 블루 프린트를 이용하면 라우트 함수를 구조적으로 관리할 수 있다.
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo!'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',
                            question_list=question_list)