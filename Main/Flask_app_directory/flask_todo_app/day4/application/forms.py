from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todos 

class TodoForm(FlaskForm):
    task = StringField('Task',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField('Todo')

    def validate_task(self, task):
        all_todos = Todos.query.all()
        if task.data in all_todos:
            raise ValidationError('You already have that Todo')

class OrderForm(FlaskForm):
    order = SelectField('Order',
        choices = [
            ("old", "Oldest"),
            ("new","Newest"),
            ("complete", "Completed"),
            ("incomplete", "Incompleted")
        ]
    )

    submit = SubmitField('Order')
