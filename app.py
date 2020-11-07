## 필요한 모듈(Flask, pymongo) import하기
import api
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

# Flask 서버 만들기
app = Flask(__name__)

# 메인 페이지 로드
@app.route('/')
def home():
    return render_template('index.html')

# API Read 기능
@app.route('/read', methods=['GET'])
def show_oilprice():
    doc = api.api
    return jsonify(doc)

# API Create 기능


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)