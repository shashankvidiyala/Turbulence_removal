from flask import Flask, render_template, Response
import time
app=Flask(__name__)

@app.route('/')
def index():
    return Response('static/mypage.html')
def generate_image(url):
    pass
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True)