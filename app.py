from flask import Flask

app = Flask(__name__)

@app.route('/')
def introduce_student():
    return '''
    <h1>Student Introduction</h1>
    <p>Hello! I'm a student using Flask.</p>
    <p>This is a simple web application built with Flask.</p>
            '''

@app.route('/lottie')
def intro_lottie():
    return'''
    <h1>Introduction<h1>
    <p>Hi. I'm Lottie.<p>
    <p>Something about flask idk.<p>
    '''
if __name__ == '__main__':
    app.run(debug=True)
