from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.fields import EmailField


app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

def uoft_email_check(form, field):
    if "utoronto" not in field.data.lower():
        raise ValidationError('Please enter a valid UofT email address.')
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email address!')
            
        session['name'] = form.name.data
        session['email'] = form.email.data
        
        return redirect(url_for('index'))
    return render_template('index.html', 
                           form=form, 
                           name=session.get('name'),
                           email=session.get('email'),
                           current_time=datetime.utcnow())

@app.route('/reset')
def reset():
    session.pop('name', None)
    session.pop('email', None)
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)