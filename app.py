from flask_restful import Resource
from flask_restful import reqparse

# CORS(Cross Origin Resource Sharing) : 동일 출처(같은 호스트네임)가 아니더라도 정상적으로 사용 가능하도록 도와주는 방법입니다.
# 다른 도메인이나 로컬 환경에서 자바스크립트로 api 등을 호출하는 경우 브라우저에서 동일 출처 위반의 에러가 나타날 수 있습니다
from flask_cors import CORS


class Plus(Resource):
    def get(self):
        try:
            # 요청받은거를 받아주자
            parser = reqparse.RequestParser()
            # add_argument 를 통해 입력 파라미터를 설정할 수 있다.
            parser.add_argument('x', required=True, type=int, help='x cannot be blank') # add_argument(*args, **kwargs)
            parser.add_argument('y', required=True, type=int, help='y cannot be blank')
            args = parser.parse_args() # Parse all arguments from the provided request and return the results as a Namespace
            result = args['x'] + args['y']
            return {'result': result} # 실제 돌려줄 값을 여기에 넣어준다.
        except Exception as e:
            return {'error': str(e)}

from flask import Flask
from flask_restful import Api

app = Flask('My First App')
api = Api(app)
CORS(app)
api.add_resource(Plus, '/plus')

if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8080, debug=True)