# -*- coding: utf-8 -*-

import pingpp
from flask import Flask, request, Response
import random

app = Flask(__name__)


@app.route('/create_red_envelope', methods=['POST'])
def create_red_envelope():
    print(request.url)
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
    print(params)

    pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
    pingpp.private_key_path = 'your_rsa_private_key.pem'

    red_envelope = pingpp.RedEnvelope.create(**params)
    print('Red Envelope: ', red_envelope.to_str())
    return Response(red_envelope.to_str(),
                    mimetype='application/json,charset=UTF-8')


if __name__ == '__main__':
    app.run(debug=True, port=8888, host='0.0.0.0')
