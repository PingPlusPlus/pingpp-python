# -*- coding: utf-8 -*-

import pingpp
from flask import Flask, request, Response
import json
import random

app = Flask(__name__)


@app.route('/redenvelope', methods=['POST'])
def do_redenvelope():
    print request.url
    params = request.get_json()

    orderno = random.randint(10000000, 99999999999)
    if isinstance(params, dict):
        params['order_no'] = orderno
        params['app'] = dict(id='app_1Gqj58ynP0mHeX1q')
        params['currency'] = 'cny'
        params['client_ip'] = '127.0.0.1'
        params['subject'] = 'Your Subject'
        params['body'] = 'Your Body'
        params['extra'] = dict(nick_name='Nick Name', send_name='Send Name')
        params['recipient'] = 'Openid'
        params['description'] = 'Your Description'
    print params

    pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
    pingpp.private_key_path = 'your_rsa_private_key.pem'

    response_redenvelope = pingpp.RedEnvelope.create(api_key=pingpp.api_key,
                                                     **params)
    print 'Response_redenvelope: ' + str(response_redenvelope)
    return Response(json.dumps(response_redenvelope),
                    mimetype='application/json,charset=UTF-8')

if __name__ == '__main__':
    app.run(debug=True, port=8888, host='0.0.0.0')
