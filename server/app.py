#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route("/contract/<int:id>")
def Contract(id):
    print("ID:", id)
    print("CONTRACTS:", contracts)
    for contract in contracts:
        if contract["id"] == id:
            response_body = contract["contract_information"]
            return make_response(response_body,200,{})
    return make_response(f"/contract/{id} does not exists", 404, {})
@app.route("/customer/<customer_name>")
def Customer(customer_name):
    if customer_name in customers:
        return make_response(f"{customer_name}",204,{})
    return make_response (f"/customer/{customer_name} does not exist",404,{})
if __name__ == '__main__':
    app.run(port=5555, debug=True)
