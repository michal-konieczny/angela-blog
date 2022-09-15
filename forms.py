from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
import email_validator
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


class RegisterForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Sign Me Up!')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In!')


class CommentForm(FlaskForm):
    comment_text = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label='Submit Comment')
