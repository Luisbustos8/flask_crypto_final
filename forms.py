from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired, ValidationError

def valida_posibilidad_compra(form, field):
    if field.data == form.from_currency.data:
        raise ValidationError("Solo conversión entre monedas distintas.")
    elif field.data != "BTC" and form.from_currency.data == "EUR":
        raise ValidationError("Solo conversión de EUR a BTC.")
    elif field.data == "EUR" and form.from_currency.data != "BTC":
        raise ValidationError("Solo conversión de otras criptomonedas a BTC.")



class PurchaseForm(FlaskForm):
    
    Moneda_from = SelectField(label= "from_currency", choices=[(moneda, moneda) for moneda in Monedas_posibles])
    Moneda_to = SelectField(label="to_currency", choices=[(moneda, moneda) for moneda in Monedas_posibles], validators=[valida_posibilidad_compra])
    Cantidad_from = FloatField("form_quantity", validators=[DataRequired(message="Por favor, introduzca una cantidad numérica superior a cero")])
    Cantidad_to = HiddenField("to_quantity")
    #Botón calculadora 
    calcular = SubmitField("fas fa-calculator")

    #Botón inferior
    aceptar =  SubmitField("fas fa-check")

    def validate_Cantidad_from(self,field): 
        if field.data < 0: 
            raise ValidationError("Por favor, introduzca una cantidad positiva")