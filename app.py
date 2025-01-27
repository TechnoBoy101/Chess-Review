from flask import Flask, render_template, request
from test import review

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('review.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        link = request.form['link']
        review(link)
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
