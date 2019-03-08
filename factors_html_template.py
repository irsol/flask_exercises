from flask import Flask, render_template
import random

app = Flask(__name__)


def factors(num):
    return [x for x in range(1, num + 1) if num % x == 0]


@app.route("/")
def home():
    n = random.randint(2, 1000)
    # template name and passing variables into the template
    return render_template("index.html", random_num=n)


# convert integers to numbers
@app.route("/factors/<int:n>")
def show_factors(n):
    # template name and passing variables into the template
    return render_template("factors.html", number=n, factors=factors(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
