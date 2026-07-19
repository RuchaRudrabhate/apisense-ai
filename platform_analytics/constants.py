"""
Centralized configuration values used across the Platform Analytics layer.
"""

# HTTP STATUS CATEGORIES

SUCCESS_STATUS_CODES = [200, 201]

CLIENT_ERROR_STATUS_CODES = [
    400,
    401,
    403,
    404,
    429
]

SERVER_ERROR_STATUS_CODES = [
    500,
    502,
    503,
    504
]

# DEFAULT PLATFORM THRESHOLDS

DEFAULT_THRESHOLDS = {

    "latency": {
        "healthy": 500,
        "warning": 1000,
        "critical": 3000
    },

    "error_rate": {
        "healthy": 5,
        "warning": 10,
        "critical": 25
    },

    "availability": {
        "healthy": 99.9,
        "warning": 99.0,
        "critical": 95.0
    }
}


# SERVICE SPECIFIC THRESHOLDS
# These override DEFAULT_THRESHOLDS

SERVICE_THRESHOLDS = {

    "auth-api": {
        "latency_warning": 400,
        "latency_critical": 800,
        "error_rate_warning": 3,
        "error_rate_critical": 8,
    },

    "user-api": {
        "latency_warning": 500,
        "latency_critical": 1000,
        "error_rate_warning": 5,
        "error_rate_critical": 10,
    },

    "product-api": {
        "latency_warning": 800,
        "latency_critical": 1500,
        "error_rate_warning": 8,
        "error_rate_critical": 15,
    },

    "inventory-api": {
        "latency_warning": 700,
        "latency_critical": 1200,
        "error_rate_warning": 5,
        "error_rate_critical": 10,
    },

    "cart-api": {
        "latency_warning": 600,
        "latency_critical": 1200,
        "error_rate_warning": 5,
        "error_rate_critical": 10,
    },

    "order-api": {
        "latency_warning": 700,
        "latency_critical": 1500,
        "error_rate_warning": 5,
        "error_rate_critical": 10,
    },

    "payment-api": {
        "latency_warning": 500,
        "latency_critical": 1000,
        "error_rate_warning": 3,
        "error_rate_critical": 8,
    },

    "shipping-api": {
        "latency_warning": 1000,
        "latency_critical": 2500,
        "error_rate_warning": 10,
        "error_rate_critical": 20,
    },

    "notification-api": {
        "latency_warning": 1500,
        "latency_critical": 3000,
        "error_rate_warning": 15,
        "error_rate_critical": 30,
    },

    "review-api": {
        "latency_warning": 1200,
        "latency_critical": 2500,
        "error_rate_warning": 10,
        "error_rate_critical": 20,
    }
}

# HEALTH SCORE

HEALTH_SCORE = {
    "EXCELLENT": 90,
    "GOOD": 75,
    "WARNING": 60,
    "CRITICAL": 40
}

# INCIDENT CONFIGURATION

INCIDENT = {
    "min_failed_requests": 10,
    "min_error_rate": 15,
    "min_latency": 1500
}

# TRAFFIC CONFIGURATION

TRAFFIC = {
    "low": 100,
    "medium": 500,
    "high": 1000
}

# SEVERITY LEVELS

SEVERITY = {
    "INFO": "INFO",
    "WARNING": "WARNING",
    "ERROR": "ERROR",
    "CRITICAL": "CRITICAL"
}

# REPORT CONFIGURATION

REPORT = {
    "top_services": 5,
    "top_errors": 10,
    "top_endpoints": 10
}