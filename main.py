#based on this tutorial: https://www.youtube.com/watch?v=MwZwr5Tvyxo

from flask import Flask, render_template, url_for, flash, redirect
from forms import NewStudentForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0081a596b5b56f84e2fea0187c3b648c' #A random token. Has to do with cookies and security. 

#dummy data for students
students = [
	{
		'SIN': '123 456 789',
		'Name': 'John',
		'DOB': '01/01/2009',
		'Sex': 'Male',
		'Lang': 'English',
		'Education': 'Grade 7',
		'SchoolName': 'ABCSchool',
		'SchoolST': '01/01/2013',
		'SchoolET': '01/01/2027',
	},
	{
		'SIN': '000 000 000',
		'Name': 'Mary',
		'DOB': '01/01/2011',
		'Sex': 'Feale',
		'Lang': 'English',
		'Education': 'Grade 6',
		'SchoolName': 'ABCSchool',
		'SchoolST': '01/01/2015',
		'SchoolET': '01/01/2029'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title='Home')

@app.route("/students") #localhost:5000/students
def allstudents():
	return render_template('students.html', students=students)

@app.route("/addstudent", methods=['GET', 'POST'])
def addstudent():
	form = NewStudentForm()
	if form.validate_on_submit():
		flash(f'Student Added: {form.name.data}','success')
		return redirect(url_for('allstudents'))
	return render_template('addstudent.html', title='Add Student', form=form)


if __name__ == '__main__':
    app.run(debug=True)