from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    code = StringField(
        'code', [
            DataRequired(
                message="Данное поле не может быть пустым!"), Length(
                min=10)])