from flask import Flask, jsonify, request
from models.poisson import poisson_probability
from models.kelly import kelly_formula
from crawlers.match_results import fetch_results

app = Flask(__name__)

@app.route("/api/poisson")
def poisson():
    lmbda = float(request.args.get("lambda"))
    result = {k: poisson_probability(lmbda, k) for k in range(6)}
    return jsonify(result)

@app.route("/api/kelly")
def kelly():
    prob = float(request.args.get("prob"))
    odds = float(request.args.get("odds"))
    result = kelly_formula(prob, odds)
    return jsonify({"kelly": result})

@app.route("/api/results")
def results():
    return jsonify(fetch_results())
