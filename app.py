from lyric_analyzer import LyricAnalyzer
from flask import Flask, jsonify, render_template, request
import pdb

app = Flask(__name__)

#lyrs = "Bag bag bag bag bag run run run run pen pen pen pen science history grammar bottles cars."
#api = LyricAnalyzer(lyrs)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/articles')
def articles():
    lyrics = request.args.get('query')
    api = LyricAnalyzer(lyrics)
    data = api.top_articles()
    return jsonify({'data': data})


if __name__ == '__main__':
        app.run()
