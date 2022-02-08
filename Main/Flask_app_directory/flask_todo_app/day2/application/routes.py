
from application import app, db
from application.models import Todos
from flask import render_template

@app.route('/')
def index():
    all_todos = Todos.query.all()
    return render_template('home.html', all_todos=all_todos)

@app.route('/add')
def add():
    latest_todo = Todos.query.order_by(Todos.id.desc()).first()
    if latest_todo:
        new_todo = Todos(task="New Todo"+str(latest_todo.id + 1))
    else: 
        new_todo = Todos(task="New Todo1")
    db.session.add(new_todo)
    db.session.commit()
    return "Added a new Todo"

@app.route('/complete/<int:id>')
def complete(id):
    todo = Todos.query.get(id)
    todo.completed = True
    db.session.commit()
    return "Todo is now complete"

@app.route('/incomplete/<int:id>')
def incomplete(id):
    todo = Todos.query.get(id)
    todo.completed = False
    db.session.commit()
    return "Todo is now incomplete"

@app.route('/update/<task>')
def update(task):
    latest_todo = Todos.query.order_by(Todos.id.desc()).first()
    latest_todo.task = task
    db.session.commit()
    return "Updated most recent Todo"

@app.route('/delete')
def delete():
    latest_todo = Todos.query.order_by(Todos.id.desc()).first()
    db.session.delete(latest_todo)
    db.session.commit()
    return "Deleted most recent Todo"
