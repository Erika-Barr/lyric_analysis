from lyric_analyzer import LyricAnalyzer
from flask import Flask, jsonify
app = Flask(__name__)

lyrs = "Bag bag bag bag bag run run run run pen pen pen pen science history grammar bottles cars."
api = LyricAnalyzer(lyrs)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return jsonify(api.top_articles())



if __name__ == '__main__':
        app.run()
