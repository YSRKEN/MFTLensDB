from flask import Flask, render_template, json

from repository.i_mft_db import IMftDb
from repository.sqlite_mft_db import SQLiteMftDb

app = Flask(__name__)
mft_db: IMftDb = SQLiteMftDb()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lenses')
def get_lenses():
    return json.jsonify(mft_db.get_lenses())


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
