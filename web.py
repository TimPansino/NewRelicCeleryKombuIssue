import time
from flask import Flask
from tasks import rand_int_task

app = Flask(__name__)


@app.route("/")
def root():
    i = rand_int_task.delay(10)
    j = rand_int_task.delay(add=20)

    while not i.ready():
        time.sleep(0.1)
    i = i.result

    while not j.ready():
        time.sleep(0.1)
    j = j.result

    return f"Your random numbers are: {i}, {j}"


if __name__ == "__main__":
    app.run(port=8000)
