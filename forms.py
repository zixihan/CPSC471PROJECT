from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class NewStudentForm(FlaskForm):
	name = StringField('Student\'s Full Name',
								validators = [DataRequired()])
	sin = StringField('SIN',
								validators = [DataRequired()])
	dob = StringField('Date of Birth (dd/mm/yyyy)',
								validators = [DataRequired()])
	sex = StringField('Sex',
							validators = [DataRequired()])
	lang = StringField('Language',
							validators = [DataRequired()])
	education = StringField('Grade Level',
							validators = [DataRequired()])
	schoolname = StringField('School Name')
	schoolST = StringField('School Start Date')
	schoolET = StringField('School End Date')
	
	flagLD = BooleanField('General Learning Disability')
	flagADHD = BooleanField('Attention Deficit Hyperactivity Disorder')
	flagASD = BooleanField('Autism Spectrum Disorder')
	flagGifted = BooleanField('Gifted')

	submit = SubmitField('Add Student')