from flask import Flask, render_template
import random, os

app = Flask(__name__)

# list of cat images
images = [
    "http://tny.im/88H",
    "http://tny.im/88I",
    "http://tny.im/88J"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0")
