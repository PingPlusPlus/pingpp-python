from pingpp import util


class PingppResponse:

    def __init__(self, body, code, headers):
        self.body = body
        self.code = code
        self.headers = headers
        self.data = util.json.loads(body)

    @property
    def pingplusplus_signature(self):
        try:
            return self.headers['x-pingplusplus-signature']
        except KeyError:
            return None
