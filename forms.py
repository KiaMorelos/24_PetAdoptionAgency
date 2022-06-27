from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired(message="Name field cannot be blank")])
    species = SelectField("Species",
    choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Pet Photo Url", validators=[Optional(), URL(require_tld=True, message="Please provide a valid url")])
    age = IntegerField("Age of Pet", validators=[Optional(), NumberRange(min=0, max=30, message="Submit an age between 0 and 30")])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing existing pets"""
    photo_url = StringField("Pet Photo Url", validators=[Optional(), URL(require_tld=True, message="Please provide a valid url")])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Is available for adoption?")
    photo_url = StringField("Pet Photo Url", validators=[Optional(), URL(require_tld=True, message="Please provide a valid url")])