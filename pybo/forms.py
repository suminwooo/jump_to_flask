from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

# QuestionFrom 클래스는 Flask-WTF 모듈의 FlaskForm을 상속받으며 subject, content 속성을 포함한다.
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[
        DataRequired('내용은 필수입력 항목입니다.')
    ])