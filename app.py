import datetime

from flask import Flask

import sqlhandler

app = Flask(__name__)

handler = sqlhandler.SQLHandler()


@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    handler.submit(date)
    data = handler.threaded_select()
    return data


if __name__ == '__main__':
    app.run()
