from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors


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


connection = pymysql.connect(
    host="10.100.33.60",
    user="tbobo",
    password="223068750",
    database="tbobo_Todos",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

cursor = connection.cursor()

cursor.execute("SELECT * from `Todos`")

result = cursor.fetchall()

print(result)