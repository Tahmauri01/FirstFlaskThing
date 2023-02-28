from flask import Flask, render_template, request


app = Flask(__name__)

todo=["Create a game", "Get a job"]

@app.route("/")
def index():
    return render_template(
        "todo.html.jinja",
        
    )




@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    todo.append(new_todo)