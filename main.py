import json
from flask_cors import *
from flask import Flask,render_template,request,Response,redirect,url_for

# 导入蓝图
app = Flask(__name__)
# 跨域
CORS(app, supports_credentials=True)

# 路由
# 首页
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

# 运行
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)