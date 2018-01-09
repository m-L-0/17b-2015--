# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField,FileField
# from wtforms.validators import Required,DataRequired
# from werkzeug import secure_filename
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess string'


# class NameForm(FlaskForm):
#     file = FileField(u'只能上传图片！')
#     submit = SubmitField(u'上传')

# @app.route('/', methods=["GET","POST"])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         filename = secure_filename(form.photo.data.filename)
#         form.photo.data.save('uploads/' + filename)
#     else:
#         filename = None
#     return render_template('index.html',form = form)
import os

from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(photos, u'只能上传图片！'), 
        FileRequired(u'文件未选择！')])
    submit = SubmitField(u'上传')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data, name='img/')
        file_url = photos.url(filename)
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)


if __name__ == '__main__':
    app.run()

