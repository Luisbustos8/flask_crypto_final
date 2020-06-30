from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField
from wtforms.validators import DataRequired

def valida_posibilidad_compra(form, field):
    if field.data == form.from_currency.data:
        raise ValidationError("Solo conversión entre monedas distintas.")
    elif field.data != "BTC" and form.from_currency.data == "EUR":
        raise ValidationError("Solo conversión de EUR a BTC.")
    elif field.data == "EUR" and form.from_currency.data != "BTC":
        raise ValidationError("Solo conversión de otras criptomonedas a BTC.")

class PurchaseForm(FlaskForm):
    from_currency = SelectField("from_currency")
    to_currency = SelectField("to_currency", validators=[valida_posibilidad_compra])
    form_quantity = FloatField("form_quantity", validators=[DataRequired(message="Por favor, introduzca una cantidad numérica superior a cero")])

