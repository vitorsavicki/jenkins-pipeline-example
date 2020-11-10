from flask import Flask
import os
import bugsnag
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

bugsnag.configure(
    api_key="8fb4eae6257a8ef2260c41ee758c3033",
    project_root="/",
)

@app.route('/')
def hello_world():
    return 'Flask Dockerized BugSnag'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)


bugsnag.notify(Exception('Test error'))
