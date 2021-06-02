from flask import Flask 
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy


import config 


db = SQLAlchemy()
migrate = Migrate()

def create_app(): # 플라스크 내부에서 정의된 함수명
    app = Flask(__name__) # 플라스크 애플리케이션을 생성하는 코드, 이코드에서 __name__이라는 변수에는 모듈명이 담긴다.
    app.config.from_object(config) # app.config 환경 변수로 부르기 위해 추가

    # ORM : object relational mapping : 데이터 베이스에 데이터를 저장하는 테이블을 파이ㅏ썬 클래스로 만들어 관리하는 기술
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루 프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp) # 블루프린트 객체 bp 등록 
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app