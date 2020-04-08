from flask import Flask, render_template, request

app = Flask(__name__)
entries = []

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        entries.append(entry_content)
    
    return render_template('home.html', entries=entries)