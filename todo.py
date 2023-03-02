from flask import Flask, render_template, request, redirect


app = Flask(__name__)

todos=["Create a game", "Get a job"]

@app.route("/")
def index():
    return render_template(
        "todo.html.jinja",
        todo = todos
    )




@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    todos.append(new_todo)
    return redirect("/")