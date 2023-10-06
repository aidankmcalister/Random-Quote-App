from flask import Flask, render_template
from quote_generator import get_random_quote
app = Flask(__name__)


@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run()
