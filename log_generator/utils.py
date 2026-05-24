import uuid
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_trace_id():
    return str(uuid.uuid4())

def generate_status_code():
    return random.choices(
        [200, 201, 400, 401, 403, 404, 429, 500, 502, 503, 504],
        weights=[80, 5, 3, 2, 1, 2, 1, 3, 1, 1, 1]
    )[0]

def generate_latency(status_code):

    latency_map = {

        200: (50, 250),
        201: (80, 300),

        400: (100, 400),
        401: (80, 350),
        403: (100, 400),
        404: (50, 200),
        429: (300, 1200),

        500: (1000, 4000),
        502: (1500, 5000),
        503: (2000, 6000),
        504: (3000, 10000)
    }

    min_latency, max_latency = latency_map.get(
        status_code,
        (100, 500)
    )

    return random.randint(min_latency, max_latency)

def generate_severity(status_code):

    severity_map = {

        200: "INFO",
        201: "INFO",

        400: "WARN",
        401: "WARN",
        403: "WARN",
        404: "WARN",
        429: "WARN",

        500: "ERROR",
        502: "ERROR",
        503: "CRITICAL",
        504: "CRITICAL"
    }

    return severity_map.get(status_code, "INFO")


def generate_error_message(status_code):

    error_map = {

        400: [
            "Bad request",
            "Invalid request payload",
            "Malformed request body",
            "Missing required parameters",
            "Invalid input format"
        ],

        401: [
            "Unauthorized access",
            "Invalid authentication token",
            "Token expired",
            "Authentication failed"
        ],

        403: [
            "Access forbidden",
            "Insufficient permissions",
            "User role not authorized"
        ],

        404: [
            "Resource not found",
            "API endpoint does not exist",
            "Requested item unavailable"
        ],

        429: [
            "Rate limit exceeded",
            "Too many requests",
            "Request throttled"
        ],

        500: [
            "Internal server error",
            "Unhandled server exception",
            "Unexpected backend failure",
            "Application crash detected"
        ],

        502: [
            "Bad gateway",
            "Upstream service unavailable",
            "Dependency service failure"
        ],

        503: [
            "Service unavailable",
            "Server overloaded",
            "Temporary maintenance outage"
        ],

        504: [
            "Gateway timeout",
            "Database timeout",
            "Downstream service timeout",
            "Request processing timeout"
        ]
    }

    if status_code in [200, 201]:
        return ""

    return random.choice(
        error_map.get(status_code, ["Unknown error"])
    )

def generate_timestamp():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    random_date = fake.date_time_between(
        start_date=start_date,
        end_date=end_date
    )

    return random_date.isoformat()