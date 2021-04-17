from flask import Flask, render_template, request, redirect, url_for
import subprocess
import sys
import os

app = Flask(__name__)

posttitle = ""

@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def query():
    nlp_class = "None"
    if request.form.get('PostTitle'):
        posttitle = request.form['PostTitle']
        if posttitle != None:
            # Call NLP with post title, save as nlp_class
            result = subprocess.run(['python', 'henlo.py', posttitle], capture_output=True, text=True)
            nlp_class = result.stdout
            with open('user_data.csv', 'a+') as file:
                file.write(posttitle+",")
                file.write(str(nlp_class).rstrip() +",")
            return render_template('classify.html', post_title = posttitle, nlp_class = nlp_class)
    return render_template('error.html')

@app.route('/store', methods=['GET', 'POST'])
def classify():
    button_class = ""
    if request.form.get('agree'):
        button_class = request.form['agree']
        with open('user_data.csv', 'a') as file:
            file.write(button_class+"\n")

    return render_template('thx.html')

if __name__ == '__main__':
    app.run(debug=True)