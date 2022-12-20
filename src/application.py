from flask import Flask, Response, request, redirect, session, render_template_string
from flask.templating import render_template
import json
from flask_cors import CORS
from orders import OrdersResource
from users import UsersResource
from products import ProductsResource

# Create the Flask application object.
application = Flask(__name__)
CORS(application)

@application.route("/")
def landing():
    return json.dumps({"msg": "Connected to microservice3"})

@application.route("/orders", methods=["GET"])
def get_all_orders():
    result = OrdersResource.get_orders()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/orders/<order_id>", methods=["GET"])
def get_order_by_id(order_id):
    result = OrdersResource.get_order_by_id(order_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/users", methods=["GET"])
def get_all_users():
    result = UsersResource.get_users()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    result = UsersResource.get_user_by_id(user_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/products", methods=["GET"])
def get_all_products():
    result = ProductsResource.get_products()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/products/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    result = ProductsResource.get_product_by_id(product_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/create_product", methods=["POST"])
def create_product():
    #data = json.loads(request.data)
    data = json.loads(list(request.form.to_dict())[0])

    product_id = data["product_id"]
    name = data["name"]
    category = data["category"]
    price = data["price"]
    print(f"Creating product {product_id} : {name}")
    if not ProductsResource.create_product(product_id, name, category, price):
        Response("Unable to add data", status=201, content_type="text/plain")

    return redirect(f'/products/{product_id}')



if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5013)