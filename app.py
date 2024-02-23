from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/test')
def about():
    return render_template('test.html')


if __name__ == "__main__": # If this app is not being called as part of a module, then:
    app.run(debug=True)
