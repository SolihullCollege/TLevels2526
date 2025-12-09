from flask import Flask

app = Flask(__name__)

@app.route('/zaid')
def introduce_zaid():
    return """
<h1>Student Introduction</h1>
<p>Hello, my name is Zaid and I'm using Flask.</p>
<p>This is a simple web application built with Flask.</p>
"""

if __name__ == '__main__':
    app.run(debug=True)
