from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Tahmauri": generate_password_hash("hello"),
    "Bobo": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


todos=["Create a game", "Get a job"]

@app.route("/")
@auth.login_required
def index():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM `Todos` ORDER BY `Complete` ASC;')

    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        todo = results
    )



@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO `Todos`(`Description`) VALUES ('"+new_todo+"')")
    return redirect("/")

@app.route("/complete", methods=["POST"])
def complete():
    todo_id = request.form['Todos_id']

    cursor = connection.cursor()

    cursor.execute(f"UPDATE `Todos` SET `Complete` = 1 WHERE `id` = {todo_id}")

    return redirect("/")


connection = pymysql.connect(
    host="10.100.33.60",
    user="tbobo",
    password="223068750",
    database="tbobo_Todos",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)