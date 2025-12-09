from flask import Flask

app = Flask(__name__)

@app.route('/zaid')
def introduce_zaid():
    return """
<h1>Student Introduction</h1>
<p>Hello, my name is Zaid and I'm using Flask.</p>
<p>This is a simple web application built with Flask.</p>
"""

@app.route('/rhys')
def introduce_rhys():
    return '''
    <h1>Student Introduction</h1>
    <p>wake up in the morning feeling like.</p>
    <p>wake up in the morning feeling like</p>
            '''
@app.route('/Josh')
def introduce_josh():
    return '''
    <h1>Student Introduction</h1>
    <p>Hello! I'm josh using Flask.</p>
    <p>This is a simple web application built with Flask mmmmmmmmm.</p>
            '''

@app.route('/Alex')
def introduce_student():
    return '''
    <h1>Hello my name is Alex</h1>
    <p>I am a student who is learning Flask and GitHub.</p>
    <p>This is a simple web application that was built up with Flask.</p>
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
