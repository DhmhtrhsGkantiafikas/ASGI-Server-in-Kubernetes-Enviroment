from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import REGISTRY, Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import os
import logging

# -----------------------
# 1️⃣ Δημιουργία FastAPI instance
# -----------------------
app = FastAPI(title="My DevOps Demo API")

# -----------------------
# 2️⃣ Configuration via environment
# -----------------------
APP_VERSION = os.getenv("APP_VERSION", "1.0")

# -----------------------
# 3️⃣ Logging setup
# -----------------------
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("fastapi_app")

# -----------------------
# 4️⃣ Metrics
# -----------------------
try:
    REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")
except ValueError:
    # Αν υπάρχει ήδη, πάρε το υπάρχον
    REQUEST_COUNT = REGISTRY._names_to_collectors['app_requests_total']
# -----------------------
# 5️⃣ Request model
# -----------------------
class Item(BaseModel):
    name: str
    quantity: int

# -----------------------
# 6️⃣ Routes
# -----------------------
@app.get("/")
def home():
    """Main endpoint"""
    REQUEST_COUNT.inc()  # αυξάνει τον counter
    logger.debug("Home endpoint visited")  # log στο console
    return {"message": "Hello from FastAPI", "version": APP_VERSION}

@app.post("/items")
def create_item(item: Item):
    """Accepts JSON with 'name' and 'quantity'"""
    REQUEST_COUNT.inc()  # μετράμε και αυτό το request
    logger.debug(f"Item received: {item}")
    # επιστρέφουμε status + τα δεδομένα που έλαβε
    return {"status": "created", "item": item}

@app.get("/metrics")
def metrics():
    """Prometheus metrics endpoint"""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "healthy"}