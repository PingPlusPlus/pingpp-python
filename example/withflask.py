__author__ = 'Lekton'

import pingpp
from flask import Flask,request,Response
import json
import random
import string

app = Flask(__name__)


@app.route('/pay', methods=['POST'])
def do_charge():
    print request.url
    form = request.get_json()
    print form
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    if isinstance(form, dict):
        form['order_no'] = salt
        form['app'] = dict(id="app_id")
        form['currency'] = "cny"
        form['client_ip'] = "192.168.1.1"
        form['subject'] = "test-subject"
        form['body'] = "test-body"
    print form
    pingpp.api_key = "sk_live_1SujP4z9mLq54CKqbDqvDqH8"
    response_charge = pingpp.Charge.create(api_key="key", **form)
    print "Response_Charge: " + str(response_charge)
    return Response(json.dumps(response_charge), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True,port=8888,host="0.0.0.0")