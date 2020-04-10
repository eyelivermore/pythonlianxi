from flask import Flask

app = Flask(__name__)

@app.route('/')
def helle_world():
    return 'hello world!'

@app.route('/got')
def hello_get():
    return 'helllo 加油武汉，中国加油'

if __name__ =='__main__':
    app.run()