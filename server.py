from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, flash,
                   session, request)

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(port=PORT, host='0.0.0.0', debug=DEBUG)
