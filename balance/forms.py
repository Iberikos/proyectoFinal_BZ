from flask_wtf import FlaskForm
from wtforms import  SelectField, FloatField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange

Coins=[('EUR', 'Euro (€)'), 
        ('BTC', 'Bitcoin (BTC)'), 
        ('ETH', 'Ethereum (ETH)'), 
        ('XRP', 'Ripple (XRP)'), 
        ('LTC', 'Litecoin (LTC)'),
        ('BCH', 'Bitcoin Cash (BCH)'), 
        ('BNB', 'Binance (BNB)'), 
        ('USDT', 'Tether (USDT)'), 
        ('EOS', 'EOS (EOS)'), 
        ('BCHSV', 'Bitcoin Cash SV (BCHSV)'), 
        ('XLM', 'Stellar Lumens (XLM)'), 
        ('ADA', 'Cardano (ADA)'), 
        ('TRX', 'Tronix (TRX)') 
]


class MovFormulary(FlaskForm):
        date = HiddenField()
        time = HiddenField()
        coinFrom = SelectField(choices = Coins)
        coinTo = SelectField(choices = Coins)
        cantFrom = FloatField("Quantity from: ", validators=[DataRequired(message="Informe una cantidad"),
                                                        NumberRange(message="Informe un número positivo", min=0.01)])
                                                        
        cantTo = FloatField("Quantity to: ")
        pu = FloatField("P.U: ")
        cantToH = HiddenField()
        puH = HiddenField()
        calcular = SubmitField("calcular")
        aceptar = SubmitField("Aceptar")
        