from flask import Blueprint, url_for
from werkzeug.utils import redirect

# 블루 프린트 객체 생성
# 블루 프린트를 이용하면 라우트 함수를 구조적으로 관리할 수 있다.
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo!'

@bp.route('/')
def index(): 
    # question._list에 해당하는 URL로 리다이렉트할 수 있도록 수정
    # redirect 함수는 입력받은 URL로 리다이렉트해 주고, url_for함수는 라우트가 설정된 함수명으로 URL을 역으로 찾아준다.
    return redirect(url_for('question._list')) # question은 등록된 블루 프린트 이름, _list는 블루 프린트에 등록된 함수명