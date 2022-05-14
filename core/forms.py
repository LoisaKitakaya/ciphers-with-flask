from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class CipherForm(FlaskForm):

    text = TextAreaField('Your Text:', render_kw={"rows":15}, validators=[DataRequired()])

    key = IntegerField('Encryption/Decryption key:', default=0, validators=[DataRequired()])

    submit = SubmitField('Submit')