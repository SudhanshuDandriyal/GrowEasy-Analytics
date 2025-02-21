from flask import Flask, request, render_template
import os
from process_data import generate_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        email = request.form['email']
        file_path = os.path.join('uploads', f"{email}.csv")
        file.save(file_path)
        generate_report(file_path, email)
        return "Report Generated and Sent!"
    return render_template('upload.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
