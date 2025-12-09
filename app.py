from flask import Flask

app = Flask(__name__)

@app.route('/')
def introduce_student():
    return '''
    <h1>Student Introduction</h1>
    <p>Hello! I'm a student using Flask.</p>
    <p>This is a simple web application built with Flask.</p>
            '''

@app.route('/Alex')
def introduce_student():
    return '''
    <h1>Hello my name is Alex</h1>
    <p>I am a student who is learning Flask and GitHub.</p>
    <p>This is a simple web application that was built up with Flask.</p>
            '''


if __name__ == '__main__':
    app.run(debug=True)
