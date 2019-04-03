from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_pyfile("config.py")

from .helper import allowed_file, upload_file_to_s3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if 'user_file' not in request.files:
        return "Please select a file to upload."
    
    if request.method == 'POST':
        return_file = request.files['user_file']
        print(return_file.content_type)
        if return_file and allowed_file(return_file.filename):
            return_file.filename = secure_filename(return_file.filename)
            output = upload_file_to_s3(return_file, app.config['S3_BUCKET'])
            return output, 200
        else:
            return redirect('/')
    """
    These attributes are also available

    return_file.filename # The actual name of the file
    return_file.content_type 
    return_file.content_length
    return_file.mimetype
    """
    
