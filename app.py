from flask import Flask
from flask_restful import Resource, Api
import os
import bugsnag
app = Flask(__name__)
api = Api(app)
port = int(os.environ.get("PORT", 5000))

bugsnag.configure(
    api_key="8fb4eae6257a8ef2260c41ee758c3033",
    project_root="/",
)

class HelloWorld(Resource):
    def get(self):
        print('Hello World')
        bugsnag.notify(Exception('Test error'))
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
