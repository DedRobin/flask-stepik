from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Length, InputRequired


class ProfileForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[Length(min=5, max=32), InputRequired()])
    password = PasswordField("Пароль", validators=[Length(min=9, max=24), InputRequired()])
    about_me = TextAreaField("О себе")
    submit = SubmitField("Submit")
