# app.py
from flask import Flask
import os

app = Flask(__name__)

# Feature flag
NEW_FEATURE = os.getenv("NEW_FEATURE") == "true"


@app.route('/')
def hello_world():
    if NEW_FEATURE:
        return 'New Feature is ON!'
    else:
        return 'Old Feature is running.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')