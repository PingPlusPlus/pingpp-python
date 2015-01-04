# -*- coding: utf-8 -*-
import urllib

from pingpp import http_client, util


class WxpubOauth:
    """
    用于微信公众号OAuth2.0鉴权，用户授权后获取授权用户唯一标识openid
    WxpubOAuth中的方法都是可选的，开发者也可根据实际情况自行开发相关功能
    详细内容可参考http://mp.weixin.qq.com/wiki/17/c0f37d5704f0b64713d5d2c37b468d75.html
    """

    @staticmethod
    def get_openid(app_id, app_secret, code):
        """
        获取微信公众号授权用户唯一标识
        :param app_id: 微信公众号应用唯一标识
        :param app_secret: 微信公众号应用密钥（注意保密）
        :param code: 授权code, 通过调用WxpubOAuth.createOauthUrlForCode来获取
        :return: openid 微信公众号授权用户唯一标识, 可用于微信网页内支付
        """
        url = WxpubOauth.create_oauth_url_for_openid(app_id, app_secret, code)
        client = http_client.new_default_http_client()
        rbody, rcode = client.request('GET', url, {})
        if rcode == 200:
            data = util.json.loads(rbody)
            return data['openid']

        return None

    @staticmethod
    def create_oauth_url_for_code(app_id, redirect_url, more_info=False):
        """
        用于获取授权code的URL地址，此地址用于用户身份鉴权，获取用户身份信息，同时重定向到$redirect_url
        :param app_id: 微信公众号应用唯一标识
        :param redirect_url: 授权后重定向的回调链接地址，重定向后此地址将带有授权code参数，
                             该地址的域名需在微信公众号平台上进行设置，
                             步骤为：登陆微信公众号平台 => 开发者中心 => 网页授权获取用户基本信息 => 修改
        :param more_info: FALSE 不弹出授权页面,直接跳转,这个只能拿到用户openid
                          TRUE 弹出授权页面,这个可以通过 openid 拿到昵称、性别、所在地，
        :return: 用于获取授权code的URL地址
        """
        data = dict()
        data['appid'] = app_id
        data['redirect_uri'] = redirect_url
        data['response_type'] = 'code'
        data['scope'] = 'snsapi_userinfo' if more_info else 'snsapi_base'
        data['state'] = 'STATE#wechat_redirect'
        query_str = urllib.urlencode(data)
        print query_str

        return "https://open.weixin.qq.com/connect/oauth2/authorize?" + query_str

    @staticmethod
    def create_oauth_url_for_openid(app_id, app_secret, code):
        """
        获取openid的URL地址
        :param app_id: 微信公众号应用唯一标识
        :param app_secret: 微信公众号应用密钥（注意保密）
        :param code: 授权code, 通过调用WxpubOAuth.createOauthUrlForCode来获取
        :return: 获取openid的URL地址
        """
        data = dict()
        data['appid'] = app_id
        data['secret'] = app_secret
        data['code'] = code
        data['grant_type'] = 'authorization_code'
        query_str = urllib.urlencode(data)

        return "https://api.weixin.qq.com/sns/oauth2/access_token?" + query_str