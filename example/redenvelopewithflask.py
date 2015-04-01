__author__ = 'Lian'

import pingpp
from flask import Flask,request,Response
import json
import random
import string

app = Flask(__name__)


@app.route('/redenvelope', methods=['POST'])
def do_redenvelope():
    print request.url
    form = request.get_json()
    print form
    orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    if isinstance(form, dict):
        form['order_no'] = orderno
        form['app'] = dict(id="YOUR-APP-ID")
        form['currency'] = "cny"
        form['client_ip'] = "127.0.0.1"
        form['subject'] = "Your Subject"
        form['body'] = "Your Body"
        form['extra'] = dict(nick_name='Nick Name', send_name='Send Name')
        form['recipient'] = 'Openid'
        form['description'] = 'Your Description'
    print form

    pingpp.api_key = "YOUR-KEY"
    response_redenvelope = pingpp.RedEnvelope.create(api_key=pingpp.api_key, **form)
    print "Response_redenvelope: " + str(response_redenvelope)
    return Response(json.dumps(response_redenvelope), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,port=8888,host="0.0.0.0")