from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, DecimalField, IntegerField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired

class ImageForm(FlaskForm):
    imageName = StringField('Image Name', [validators.Length(min=5, max=10)])
    imageFile = FileField('Image/Icon File', validators=[
        FileAllowed(['jpg'], 'Images Only!')
    ])
    submit = SubmitField('Save Picture')
