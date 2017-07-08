from flask_wtf import Form
from wtforms import StringField, BooleanField,PasswordField,FloatField,SelectField,SelectMultipleField,TextAreaField,DecimalField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


AVAILABLE_CHOICES = [('Essendon','Essendon'),('Collingwood','Collingwood'),('St Kilda','St Kilda'),('Richmond','Richmond')]

class ConstraintForm(Form):
    Constraint1_Flt = FloatField('Constraint1_Flt'  ,validators=[DataRequired()])
    Constraint2_Bool = BooleanField('Constraint2_Bool')
    Constraint3_Str = StringField('Constraint3_Str')
    Constraint4_Sel =  SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    Constraint5_SelMult =SelectMultipleField('Available', choices=AVAILABLE_CHOICES)
    Constraint6_TxtArea =TextAreaField('Constraint6_TxtArea')
    Constraint7_Decimal =DecimalField('Constraint7_Decimal',places=2, rounding=None)