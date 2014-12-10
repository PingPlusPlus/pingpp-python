__author__ = 'Lekton'

import pingpp
from flask import Flask,request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def do_charge():
    form = request.get_json()
    pingpp.api_key = "sk_test_G4W184yvjXbLOq5SS8LWjHyP"
    response_charge = pingpp.Charge.create(api_key="sk_test_G4W184yvjXbLOq5SS8LWjHyP", **form)
    return str(response_charge)

if __name__ == '__main__':
    app.run(debug=True)