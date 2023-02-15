from flask import Flask  # First we imported the Flask class.

app = Flask(__name__)  # next we create an instance of this class.


@app.route('/')  # We then use the route() decorator to tell Flask what url should trigger our function.
def hello_form():
    return '<p>Hello, this is a form!<p>'


if __name__ == '__main__':
    app.run(debug=True)
