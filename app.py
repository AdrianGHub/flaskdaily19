import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
entries = []

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get('content')
        date_content = datetime.datetime.today().strftime('%b %d')
        entries.append({'content': entry_content, 'date': date_content })
    
    return render_template('home.html', entries=entries)