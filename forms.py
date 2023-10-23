from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length,NumberRange


class Form_rodada(FlaskForm):
    rodada = IntegerField('Pesquisar Rodada', validators=[DataRequired(),NumberRange(min=1,max=38)])
    botao = SubmitField('buscar')



