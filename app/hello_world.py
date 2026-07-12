from flask import Flask
import threading

app = Flask(__name__)

load_running = False


def generate_cpu_load():
    while True:
        total = 0

        for number in range(1000000):
            total += number * number


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/health")
def health():
    return "OK"


@app.route("/load")
def load():
    global load_running

    if not load_running:
        load_running = True

        for _ in range(2):
            threading.Thread(
                target=generate_cpu_load,
                daemon=True
            ).start()

        return "CPU load started"

    return "CPU load already running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)