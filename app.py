from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from resources.naver import NaverPapagoResource, NaverSearchResource



app = Flask(__name__)

jwt = JWTManager(app)

api = Api(app)
# 경로를 리소스와 연결한다.


api.add_resource(NaverSearchResource,'/news')
api.add_resource(NaverPapagoResource,'/chinese')

if __name__ == '__main__' : 
    app.run()