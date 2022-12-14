from flask import Flask, Response, request, redirect, session
import json
from flask_cors import CORS
from orders import OrdersResource
from users import UsersResource
from products import ProductsResource

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/orders", methods=["GET"])
def get_all_orders():
    result = OrdersResource.get_orders()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/orders/<order_id>", methods=["GET"])
def get_order_by_id(order_id):
    result = OrdersResource.get_user_by_id(order_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/users", methods=["GET"])
def get_all_users():
    result = UsersResource.get_users()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    result = UsersResource.get_user_by_id(user_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/products", methods=["GET"])
def get_all_products():
    result = ProductsResource.get_orders()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/products/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    result = ProductsResource.get_product_by_id(product_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5013)