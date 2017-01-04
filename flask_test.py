from flask import Flask, url_for, render_template, request
#from werkzeug import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/<page>/')
def test(page):
    return render_template(page+'.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        #realname = secure_filename(f.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        file_dir=os.path.join(basedir, UPLOAD_FOLDER)
        f.save(os.path.join(file_dir, f.filename))
        return 'Upload successfully!'
    return

if __name__ == '__main__':
    #app.run(host='127.0.0.1')
    app.run(debug=True)

    #app.debug = True
    #app.run()
