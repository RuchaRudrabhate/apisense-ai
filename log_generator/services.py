"""
This Script defined the E-commerce services and its endpoints.
with related scripts, generator.py logs will be generated for this endpoints. 
"""

SERVICES = {
    "auth-api": [
        "/login",
        "/logout",
        "/validate-token",
        "/refresh-token",
        "/register"
    ],

    "user-api": [
        "/profile",
        "/update-profile",
        "/address",
        "/wishlist"
    ],

    "product-api": [
        "/products",
        "/search",
        "/product/{id}",
        "/categories",
        "/recommendations"
    ],

    "inventory-api": [
        "/stock",
        "/reserve-stock",
        "/release-stock"
    ],

    "cart-api": [
        "/add-cart",
        "/remove-cart",
        "/get-cart",
        "/update-quantity"
    ],

    "order-api": [
        "/create-order",
        "/order-history",
        "/cancel-order",
        "/order-status"
    ],

    "payment-api": [
        "/process-payment",
        "/payment-status",
        "/refund",
        "/payment-methods"
    ],

    "shipping-api": [
        "/shipping-rates",
        "/track-order",
        "/delivery-status"
    ],

    "notification-api": [
        "/send-email",
        "/send-sms",
        "/send-push"
    ],

    "review-api": [
        "/add-review",
        "/reviews",
        "/ratings"
    ]
}