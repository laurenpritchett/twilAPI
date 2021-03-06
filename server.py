import os

from jinja2 import StrictUndefined

from flask import (Flask, request, render_template, redirect, flash)

from helper import send_marketing_message

app = Flask(__name__)

app.secret_key = 'ABC'

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    'Homepage.'

    return render_template('homepage.html')


@app.route('/send-text', methods=['POST'])
def send_text():
    '''Send a chosen marketing message to the subscriber.'''

    marketing_message = request.form.get('message')
    send_marketing_message(marketing_message)

    return redirect('/')

if __name__ == '__main__':
    app.debug = False
    app.jinja_env.auto_reload = app.debug
    DEBUG = 'NO_DEBUG' not in os.environ
    PORT = int(os.environ.get('PORT', 5000))
    app.run(port=PORT, host='0.0.0.0', debug=DEBUG)
