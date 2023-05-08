
from flask_wtf import FlaskForm
from wtforms import StringField, URLField ,  TextAreaField, IntegerField,BooleanField,SelectField
from wtforms.validators import NumberRange, URL


class AddPetForm(FlaskForm):
    """form for adding snacks"""

    name = StringField("Pet Name")
    species = SelectField("Species", choices = [("dog","dog"),("cat","cat"),("porcupine","porcupine")])
    img_url = URLField("image url", validators=[URL(require_tld=False)])
    age = IntegerField("age", validators=[NumberRange(min=0, max=30)])
    comment = TextAreaField("comments")
    available = BooleanField("is Available?")
    
