from lyric_analyzer import LyricAnalyzer
from flask import Flask, jsonify, render_template, request
import os
import pdb

app = Flask(__name__)

#lyrs = "Bag bag bag bag bag run run run run pen pen pen pen science history grammar bottles cars."
#api = LyricAnalyzer(lyrs)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/articles')
def articles():
    '''make a conditional for an arg called recommendation
        *get lyrics from a call to a lyrics api
        *call top_articles below
    if args recommedation present:
        lyrics = LyricApi(args.get('recommendation'))
    else:
        lyrics = request.args.get('query')
    '''
    lyrics = request.args.get('query')
    api = LyricAnalyzer(lyrics)
    data = api.top_articles()
    return jsonify({'data': data})


#if __name__ == '__main__':
#        app.run()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
