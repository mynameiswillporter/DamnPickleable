import os
import pickle

from flask import Flask
from flask import flash
from flask import render_template
from flask import request

from app.forms import UploadForm

from config import Config

from werkzeug.utils import secure_filename

from app.picklers import unpickle

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html', title='Index')

@app.route('/upload_pickle', methods=['GET', 'POST'])
def upload_pickle():
    # TODO Only allow a file to be uploaded if it has a valid API key
    # TODO Make this part of the api scheme
    form = UploadForm()
    description = "This is the vanilla insecure deserializtion via pickle vulnerability."
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.pickle_file.data:
                # Save the pickle file
                pickle_file = request.files[form.pickle_file.name]
                filename = secure_filename(pickle_file.filename)
                saved_filename = os.path.join(app.config['UPLOAD_DIR'],  filename)
                pickle_file.save(saved_filename)

                # Execute the pickle file
                with open(saved_filename, 'rb') as f:
                    obj = pickle.load(f)

                flash('Pickle file uploaded successfully.')
            else:
                flash('No pickle data')
        else:
            flash('Error, pickle not uploaded')

    return render_template('uploads.html', title='Vanilla Pickle RCE', description=description, form=form)

@app.route('/upload_safe_pickle', methods=['GET', 'POST'])
def upload_safe_pickle():
    # TODO Only allow a file to be uploaded if it has a valid API key
    # TODO Make this part of the api scheme
    form = UploadForm()
    description = "This insecure deserialization uses a custom depickler class that attempts to whitelist only safe functions. Think BlackHat Sour Pickles."
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.pickle_file.data:
                # Save the pickle file
                pickle_file = request.files[form.pickle_file.name]
                filename = secure_filename(pickle_file.filename)
                saved_filename = os.path.join(app.config['UPLOAD_DIR'],  filename)
                pickle_file.save(saved_filename)

                # Execute the pickle file
                data = None
                try:
                    with open(saved_filename, 'rb') as f:
                        data = f.read()
                        object = unpickle.loads(data)
                except Exception as e:
                    flash(e)

                flash('Pickle file uploaded successfully.')
            else:
                flash('No pickle data')
        else:
            flash('Error, pickle not uploaded')

    return render_template('uploads.html', title='Sour Pickles', description=description, form=form)
