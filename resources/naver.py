from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required,get_jwt
from flask_jwt_extended import create_access_token,jwt_required,get_jwt
from mysql.connector import Error
from mysql_connection import get_connection
from datetime import datetime
import boto3
from config import Config
import requests

class NaverSearchResource(Resource) :

    def get(self) :

    
        
        keyword=request.args.get('keyword')
        limit = request.args.get('limit')

        ## 네이버 API를 호출

        ### Restful Open API를 호출할 때 사용하는 라이브러리 => requests

        data = {'query':keyword,'display':limit}
        headers = {'X-Naver-Client-Id':Config.NAVER_CLIENT_ID,'X-Naver-Client-Secret':Config.NAVER_CLIENT_SECRET}

        response = requests.get('https://openapi.naver.com/v1/search/news.json',data, headers= headers)
        
        response=response.json()

        # print(response['items'][0]['title'])
        title_list=[]
        for row in response['items'] :
            title_list.append(row['title'])

        return {'result' : 'success' , 'items' : title_list} , 200




class NaverPapagoResource(Resource) :

    def post(self) :
        # {"content":"안녕하세요~"}
        data = request.get_json()
        headers = {'X-Naver-Client-Id':Config.NAVER_CLIENT_ID,'X-Naver-Client-Secret':Config.NAVER_CLIENT_SECRET,
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}

        # 네이버 파파고 api 호출
        req_data = {'source':'ko','target':'zh-CN','text': data['content']}

        response=requests.post('https://openapi.naver.com/v1/papago/n2mt',req_data,headers=headers)

        response=response.json()

        result_text = response['message']['result']['translatedText']

        return {'result':'success','result_text':result_text}