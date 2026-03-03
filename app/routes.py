from flask import Blueprint, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

main = Blueprint("main", __name__)

REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")

@main.route("/")
def home():
    REQUEST_COUNT.inc()
    return render_template(
        "index.html",
        message="Hello from Kubernetes Project!",
        version="dynamic"
    )

@main.route("/health")
def health():
    return "OK", 200

@main.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
