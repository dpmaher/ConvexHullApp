from flask import Flask, render_template, request
import sys, json
from lib import computationalGeometry as cg

app = Flask(__name__)

@app.route('/', methods=['POST'])
def parse_points():
    js_data = request.get_json()
    hull = cg.compute_convexhull(cg.form_point_list(js_data["X"], js_data["Y"]))
    X = [p.x for p in hull]
    Y = [p.y for p in hull]
    returnPts = json.dumps({ "X" : X, "Y" : Y})
    return returnPts

@app.route('/')
def index():
    return render_template("convexhull.html");

if __name__ == '__main__':
    app.run(debug=True)
