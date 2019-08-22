from flask import Flask, render_template, request
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


class RegisForm(FlaskForm):
    Firstname = StringField("FirstName", validators=[InputRequired()])
    Lastname = StringField("Lastname", validators=[InputRequired()])
    Email = StringField("Email", validators=[InputRequired("Please enter your email address."), Email("Please enter your email again.")])
    Username = StringField("Username", validators=[InputRequired()])
    Password = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Please enter your password 8 character.")])


@app.route('/')
def student():
    form = RegisForm()
    return render_template('regis.html', form=form)


@app.route('/regis', methods=["GET", "POST"])
def regis():
    form = RegisForm()
    if form.validate_on_submit():
        return "Ok"
    return render_template('regis.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
