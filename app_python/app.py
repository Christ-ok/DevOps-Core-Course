import logging
import os
import platform
import socket
from datetime import datetime, timezone
from flask import Flask, jsonify, request

app = Flask(__name__)

START_TIME = datetime.now(timezone.utc)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

ENDPOINTS = [
    {"path": "/", 
      "method": "GET", 
      "description": 
      "Service information"
    },

    {"path": "/health", 
      "method": "GET", 
      "description": "Health check"
    },
]


def get_uptime_human(seconds: int) -> str:
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes"


@app.route("/")
def index():
    uptime_seconds = int((datetime.now(timezone.utc) - START_TIME).total_seconds())

    logger.info("GET / from %s", request.remote_addr)

    return jsonify({
        "service": {
            "name": "devops-info-service",
            "version": "1.0.0",
            "description": "DevOps course info service",
            "framework": "Flask"
        },
        "system": {
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "cpu_count": os.cpu_count(),
            "python_version": platform.python_version()
        },
        "runtime": {
            "uptime_seconds": uptime_seconds,
            "uptime_human": get_uptime_human(uptime_seconds),
            "current_time": datetime.now(timezone.utc).isoformat(),
            "timezone": "UTC"
        },
        "request": {
            "client_ip": request.remote_addr,
            "user_agent": request.headers.get("User-Agent"),
            "method": request.method,
            "path": request.path
        },
        "endpoints": ENDPOINTS
    })


@app.route("/health")
def health():
    uptime_seconds = int((datetime.now(timezone.utc) - START_TIME).total_seconds())
    logger.info("GET /health from %s", request.remote_addr)
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": uptime_seconds
    }), 200


@app.errorhandler(404)
def not_found(error):
    logger.info("404 Not Found: %s", request.path)
    return jsonify({"error": "Not Found", "path": request.path}), 404


@app.errorhandler(500)
def server_error(error):
    logger.error("500 Internal Server Error: %s", error)
    return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("DEBUG", "False").lower() == "true"

    logger.info("Starting service on %s:%s (debug=%s)", host, port, debug)
    app.run(host=host, port=port, debug=debug)