from flask import Response ,jsonify ,make_response , json
import flask
from my_util.my_logger import my_logger
from flask_cors import CORS

app =  flask.Flask(__name__)


@app.route("/" , methods=['GET','POST'])
def index():
    my_res =Response("차단되지롱")
    http_method = flask.request.method


    if http_method == "OPTIONS": # 사전요청
        print("--사전 요청(Preflight Request)--")
        my_res.headers.add("Access-Control-Allow-Origin", "*")
        my_res.headers.add('Access-Control-Allow-Headers', "*")
        my_res.headers.add('Access-Control-Allow-Methods', "GET,DELETE")
    elif http_method == "GET": # 실제요청
        print("--실제 요청--")
        my_res.headers.add("Access-Control-Allow-Origin", "*")
        # 실제 데이터를 보내는 부분
        # my_res.set_data("가져왔지롱")
        
        # my_res = make_response(json.dumps(body, ensure_ascii=False).decode('utf8'))
        # d = json.loads(resp.get_data()) 
        # d['time'] = float('%.4f' % (time.time() - tic)) 
        my_res.set_cookie('name','soogeun')



        

    elif http_method == "DELETE": # 실제요청
        print("--실제 요청--")
        my_res.headers.add("Access-Control-Allow-Origin", "*")
        my_res.set_data("삭제했지롱")
    else: 
        print("요구하지 않은 HTTP METHOD(" + http_method + ")입니다.")       
    
    return my_res
    # return jsonify(result)


if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1', port=8080)