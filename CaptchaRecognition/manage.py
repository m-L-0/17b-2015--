from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FileField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    file = FileField(u'只能上传图片！')
    submit = SubmitField(u'上传')

@app.route('/')
def index():
    form = NameForm()
    return render_template('index.html',form = form)


