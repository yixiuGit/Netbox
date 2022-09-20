from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NETBOX_NEW_OBJECT(FlaskForm):
    # api_attr = SelectField('Object Path ',choices=[('ipam.vlans', 'newVlan'),('newIP', '#'), ('newPrefix', '#')])  #for new single vlan
    # filter_key = SelectField('Filter Key',choices=[('vid', 'Vlan Number')])
    api_attr = SelectField('Object Path ', choices=[('ipam.prefixes', 'newPrefix'), ('newIP', '#'), ('newPrefix', '#')])  #for new prefixes
    filter_key = SelectField('Filter Key',choices=[('prefix', 'Prefixes')])
    filter_data = StringField('Filter Data', validators=[DataRequired()])
    filter_key1 = SelectField('Filter Key1',choices=[('status', 'Status')])
    filter_data1 = StringField('Filter Data1', validators=[DataRequired()])
    input_data = StringField('Input Data',validators=[DataRequired()])

    submit = SubmitField('Submit')
