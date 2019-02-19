from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email


class PostForm(FlaskForm):

    title = StringField('Plog title',validators=[Required()])
    post = TextAreaField('What is on your mind?', validators=[Required()])
    submit = SubmitField('Publish')
    category = SelectField(
        "category",
        choices=[("life", "life")],validators = [Required()]
    )
   

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
   
    body = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
   name = StringField("Your Name")
   email = StringField("Email")
   submit= SubmitField('Subscribe')