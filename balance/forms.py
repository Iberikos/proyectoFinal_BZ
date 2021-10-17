from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MovFormulary(FlaskForm):
    cantFrom = FloatField("Quantity from: ", validators=[DataRequired(message="Informe una cantidad"),
                                                      NumberRange(message="Informe un número positivo", min=0.01)])
    cantTo = FloatField("Quantity To: ")
    pu = FloatField("Precio unitario: ")
    submit = SubmitField("Aceptar")
    calculadora = SubmitField("calcular")