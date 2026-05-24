"""
This Script defined the E-commerce services and its endpoints.
with related scripts, generator.py logs will be generated for this endpoints. 
"""

SERVICES = {
    "auth-api": [
        "/login",
        "/validate-token",
        "/logout"
    ],
    "product-api": [
        "/products",
        "/search",
        "/product/{id}"
    ],
    "cart-api": [
        "/add-cart",
        "/remove-cart",
        "/get-cart"
    ],
    "payment-api": [
        "/process-payment",
        "/payment-status"
    ],
    "order-api": [
        "/create-order",
        "/order-history"
    ]
}