from flask import Flask

app = Flask(__name__)

@app.route('/')
def introduce_student():
    return '''
    <h1>Student Introduction</h1>
    <p>Hello! I'm a student using Flask.</p>
    <p>This is a simple web application built with Flask.</p>
            '''

@app.route('/rhys')
def introduce_rhys():
    return '''
    <h1>Student Introduction</h1>
    <p>wake up in the morning feeling like.</p>
    <p>wake up in the morning feeling like</p>
            '''

if __name__ == '__main__':
    app.run(debug=True)
