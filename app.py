from flask import Flask

app = Flask(__name__)

@app.route('/')
def introduce_student():
    return '''
    <h1>Student Introduction</h1>
    <p>Hello! I'm a student using Flask.</p>
    <p>This is a simple web application built with Flask.</p>
            '''
@app.route('/Josh')
def introduce_josh():
    return '''
    <h1>Student Introduction</h1>
    <p>Hello! I'm josh using Flask.</p>
    <p>This is a simple web application built with Flask mmmmmmmmm.</p>
            '''

if __name__ == '__main__':
    app.run(debug=True)
