import json
from flask_cors import *
from flask import Flask,render_template,request,Response,redirect,url_for
import wzh.db as db

# 导入蓝图
app = Flask(__name__)
# 跨域
CORS(app, supports_credentials=True)

# 路由
# 首页图表
@app.route('/')
def pie_nest():
    return render_template('pie-nest.html')
# 动态柱状图
@app.route('/bar-race')
def bar_race():
    return render_template('bar-race.html')

#pie-nest-data
@app.route('/pie_data')
def pie_data():
    data_list = {}
    data_raw = db.Cmd("SELECT value,name FROM pie") 

    # 获取图例
    legend = [i[1] for i in data_raw if i[0] > 6000]
    data_list['data1'] = legend

    # 获取数据
    data_large = []
    data_small = []
    for i in data_raw:
        if i[0] > 6000:
            data_large.append({'value':i[0],'name':i[1]})
        elif i[0] > 3000:
            data_small.append({'value':i[0],'name':i[1]})
    data_large[0]['selected'] = True # 默认选中第一个
    data_list['data2'] = data_large
    data_list['data3'] = data_small
    
    return Response(json.dumps(data_list), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)

