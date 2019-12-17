from flask import Flask, render_template


app = Flask(__name__)


page = """
<html>
<head>
<title>Enter a title, displayed at the top of the window.</title>
</head>
<body>
<h1>Online Calculator</h1>
<p>Simplified version of Modern Calculator</p>
<div>
Calculated Value: {0}
</div>
<hr>
<p>Finally, link to <a href="/index">Home page</a> in your own Web site.</p>
<!-- And add a copyright notice.-->
<p>&#169; Pitta Publishers, 2019</p>
</body>
</html>
"""

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/add/<a>/<b>")
def add(a, b):
    return page.format(str(int(a) + int(b)))

@app.route("/sub/<a>/<b>")
def sub(a,b):
    return page.format(str(int(a) - int(b)))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
