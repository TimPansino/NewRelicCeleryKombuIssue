import time
from flask import Flask
from tasks import rand_int_task

app = Flask(__name__)


@app.route("/")
def root():
    result = rand_int_task.delay()
    while not result.ready():
        time.sleep(0.1)
    i = result.result

    return f"Your random number is: {i}"


if __name__ == "__main__":
    app.run(port=8000)
