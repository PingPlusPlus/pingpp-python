# -*- coding: utf-8 -*-

import urllib
import warnings
import sys

from pingpp import api_requestor, error, util


def convert_to_pingpp_object(resp, api_key):
    types = {'charge': Charge, 'list': ListObject,
             'refund': Refund, 'red_envelope': RedEnvelope,
             'event': Event, 'transfer': Transfer,
             'Order': Order, 'CouponTemplate': CouponTemplate,
             'User': User, 'Withdrawal': Withdrawal,
             'Coupon': Coupon, 'BatchTransfer': BatchTransfer,
             'BatchRefund': BatchRefund,
             'Identification': Identification, 'OrderRefunds': OrderRefunds,
             "Recharge": Recharge, 'settle_account': SettleAccount,
             'royalty_settlement': RoyaltySettlement,
             'royalty_transaction': RoyaltyTransaction,
             'royalty_template': RoyaltyTemplate,
             'balance_bonus': BalanceBonus,
             }

    if isinstance(resp, list):
        return [convert_to_pingpp_object(i, api_key) for i in resp]
    elif isinstance(resp, dict) and not isinstance(resp, PingppObject):
        resp = resp.copy()
        klass_name = resp.get('object')
        if isinstance(klass_name, basestring):
            klass = types.get(klass_name, PingppObject)
        else:
            klass = PingppObject
        return klass.construct_from(resp, api_key)
    else:
        return resp


class PingppObject(dict):
    def __init__(self, id=None, api_key=None, **params):
        super(PingppObject, self).__init__()

        self._unsaved_values = set()
        self._transient_values = set()

        self._retrieve_params = params
        self._previous_metadata = None

        object.__setattr__(self, 'api_key', api_key)

        if id:
            self['id'] = id

    def __setattr__(self, k, v):
        if k[0] == '_' or k in self.__dict__:
            return super(PingppObject, self).__setattr__(k, v)
        else:
            self[k] = v

    def __getattr__(self, k):
        if k[0] == '_':
            raise AttributeError(k)

        try:
            return self[k]
        except KeyError as err:
            raise AttributeError(*err.args)

    def __setitem__(self, k, v):
        if v == "":
            raise ValueError(
                "You cannot set %s to an empty string. "
                "We interpret empty strings as None in requests."
                "You may set %s.%s = None to delete the property" % (
                    k, str(self), k))

        super(PingppObject, self).__setitem__(k, v)

        # Allows for unpickling in Python 3.x
        if not hasattr(self, '_unsaved_values'):
            self._unsaved_values = set()

        self._unsaved_values.add(k)

    def __getitem__(self, k):
        try:
            return super(PingppObject, self).__getitem__(k)
        except KeyError as err:
            if k in self._transient_values:
                raise KeyError(
                    "%r.  HINT: The %r attribute was set in the past."
                    "It was then wiped when refreshing the object with "
                    "the result returned by Pingpp's API, probably as a "
                    "result of a save().  The attributes currently "
                    "available on this object are: %s" %
                    (k, k, ', '.join(self.keys())))
            else:
                raise err

    def __delitem__(self, k):
        raise TypeError(
            "You cannot delete attributes on a PingppObject. "
            "To unset a property, set it to None.")

    @classmethod
    def construct_from(cls, values, api_key):
        instance = cls(values.get('id'), api_key)
        instance.refresh_from(values, api_key)
        return instance

    def refresh_from(self, values, api_key=None, partial=False):
        self.api_key = api_key or getattr(values, 'api_key', None)

        # Wipe old state before setting new.  This is useful for e.g.
        # updating a customer, where there is no persistent card
        # parameter.  Mark those values which don't persist as transient
        if partial:
            self._unsaved_values = (self._unsaved_values - set(values))
        else:
            removed = set(self.keys()) - set(values)
            self._transient_values = self._transient_values | removed
            self._unsaved_values = set()

            self.clear()

        self._transient_values = self._transient_values - set(values)

        for k, v in values.iteritems():
            super(PingppObject, self).__setitem__(
                k, convert_to_pingpp_object(v, api_key))

        self._previous_metadata = values.get('metadata')

    def request(self, method, url, params=None):
        if params is None:
            params = self._retrieve_params

        requestor = api_requestor.APIRequestor(self.api_key)
        response, api_key = requestor.request(method, url, params)

        return convert_to_pingpp_object(response, api_key)

    def __repr__(self):
        unicode_repr = self.to_str()

        if sys.version_info[0] < 3:
            return unicode_repr.encode('utf-8')
        else:
            return unicode_repr

    def __str__(self):
        return util.json.dumps(
            self, ensure_ascii=True,
            sort_keys=True, indent=2)

    def to_str(self):
        return util.json.dumps(
            self, ensure_ascii=False,
            sort_keys=True, indent=2)

    def to_dict(self):
        warnings.warn(
            'The `to_dict` method is deprecated and will be removed in '
            'version 2.0 of the Ping++ bindings. The PingppObject is '
            'itself now a subclass of `dict`.',
            DeprecationWarning)

        return dict(self)

    @property
    def pingpp_id(self):
        return self.id


class PingppObjectEncoder(util.json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            '`PingppObjectEncoder` is deprecated and will be removed in '
            'version 2.0 of the Ping++ bindings.  PingppObject is now a '
            'subclass of `dict` and is handled natively by the built-in '
            'json library.',
            DeprecationWarning)
        super(PingppObjectEncoder, self).__init__(*args, **kwargs)


class APIResource(PingppObject):
    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    def refresh(self):
        self.refresh_from(self.request('get', self.instance_url()))
        return self

    @classmethod
    def class_name(cls):
        if cls == APIResource:
            raise NotImplementedError(
                'APIResource is an abstract class.  You should perform '
                'actions on its subclasses (e.g. Charge, Customer)')
        return str(urllib.quote_plus(cls.__name__.lower()))

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%ss" % (cls_name,)

    def instance_url(self):
        id = self.get('id')
        if not id:
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r' % (type(self).__name__, id), 'id')
        id = util.utf8(id)
        base = self.class_url()
        extn = urllib.quote_plus(id)
        return "%s/%s" % (base, extn)


class ListObject(PingppObject):
    def all(self, **params):
        return self.request('get', self['url'], params)

    def create(self, **params):
        if self['url'].startswith(u'/v1/charges'):
            return self.request('post', self['url'], params=params)
        return self.request('post', self['url'], params)

    def retrieve(self, id, **params):
        base = self.get('url')
        id = util.utf8(id)
        extn = urllib.quote_plus(id)
        url = "%s/%s" % (base, extn)

        return self.request('get', url, params)


class SingletonAPIResource(APIResource):
    @classmethod
    def retrieve(cls, api_key=None):
        return super(SingletonAPIResource, cls).retrieve(None, api_key=api_key)

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    def instance_url(self):
        return self.class_url()


# Classes of API operations


class ListableAPIResource(APIResource):
    @classmethod
    def all(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def list(cls, api_key=None, **params):
        return cls.all(api_key, **params)


class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('post', url, params)

        return convert_to_pingpp_object(response, api_key)


class UpdateableAPIResource(APIResource):
    def __init__(self, id=None, api_key=None, **params):
        super(UpdateableAPIResource, self).__init__(id, api_key, **params)
        self.cancel = self.__cancel
        self.confirm = self.__confirm

    def __update_status(self, status):
        params = {'status': status}
        self.refresh_from(self.request('put', self.instance_url(), params))
        return self

    def __cancel(self):
        return self.__update_status('canceled')

    def __confirm(self):
        return self.__update_status('pending')

    @classmethod
    def _update_status(cls, id, status='canceled'):
        params = {'status': status}
        requestor = api_requestor.APIRequestor()
        _instance = cls(id)

        url = _instance.instance_url()
        response, api_key = requestor.request('put', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def cancel(cls, id):
        return cls._update_status(id)

    @classmethod
    def confirm(cls, id):
        return cls._update_status(id, 'pending')


class DeletableAPIResource(APIResource):
    def delete(self, **params):
        self.refresh_from(self.request('delete', self.instance_url(), params))
        return self


class Charge(CreateableAPIResource, ListableAPIResource):
    def refund(self, **params):
        url = self.instance_url() + '/refunds'
        self.refresh_from(self.request('post', url, params))
        return self

    def refund_list(self, **params):
        url = self.instance_url() + '/refunds'
        self.refresh_from(self.request('get', url, params))
        return self

    def refund_retrieve(self, refund_id):
        url = self.instance_url() + '/refunds/%s' % refund_id
        self.refresh_from(self.request('get', url))
        return self

    @classmethod
    def all(cls, app_id=None, api_key=None, **params):
        if params and params['app']['id'] is None:
            raise error.InvalidRequestError('Please pass app[id] as parameter', 'app[id]')
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def reverse(cls, charge_id=None, api_key=None, **params):
        url = cls.class_url() + '/%s/reverse' % charge_id
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('post', url, params)
        return convert_to_pingpp_object(response, api_key)


class RedEnvelope(CreateableAPIResource, ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'red_envelope'


class Event(ListableAPIResource):
    @classmethod
    def list(cls, api_key=None, **params):
        pass


class Transfer(CreateableAPIResource, ListableAPIResource):
    @classmethod
    def cancel(cls, id):
        params = {'status': 'canceled'}
        requestor = api_requestor.APIRequestor()
        _instance = cls(id)

        url = _instance.instance_url()
        response, api_key = requestor.request('put', url, params)
        return convert_to_pingpp_object(response, api_key)


class Refund(UpdateableAPIResource):
    def instance_url(self):
        self.id = util.utf8(self.id)
        self.charge = util.utf8(self.charge)
        base = Charge.class_url()
        cust_extn = urllib.quote_plus(self.charge)
        extn = urllib.quote_plus(self.id)
        return "%s/%s/refunds/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a refund without a charge ID. "
            "Use charge.refunds.retrieve('refund_id') instead.")


class Customs(CreateableAPIResource, ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'custom'


class BatchRefund(CreateableAPIResource, ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'batch_refund'


class BatchTransfer(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    @classmethod
    def class_name(cls):
        return "batch_transfer"


class Identification(CreateableAPIResource):
    @classmethod
    def class_name(cls):
        return 'identification'

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    def instance_url(self):
        return self.class_url()

class Order(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    @classmethod
    def pay(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key, **params)
        url = instance.instance_url() + '/pay'
        response, api_key = requestor.request('post', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def cancel(cls, id, api_key=None, **params):
        params['status'] = 'canceled'
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key, **params)
        url = instance.instance_url()
        response, api_key = requestor.request('put', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def _update_status(cls, id, status='canceled'):
        params = {'status': status}
        requestor = api_requestor.APIRequestor()
        _instance = cls(id)

        url = _instance.instance_url()
        response, api_key = requestor.request('put', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def charge_list(cls, id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/charges" % (instance.class_url(), id)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def charge_retrieve(cls, id, charge_id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/charges/%s" % (instance.class_url(), id, charge_id)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)


class OrderRefunds(CreateableAPIResource, ListableAPIResource):
    @classmethod
    def create(cls, api_key=None, order_id=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(order_id, api_key, **params)
        url = instance.instance_url(order_id)
        response, api_key = requestor.request('post', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def list(cls, api_key=None, order_id=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(order_id)
        response, api_key = requestor.request('get', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve(cls, api_key=None, order_id=None, refund_id=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(order_id, refund_id)
        response, api_key = requestor.request('get', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def class_url(cls, order_id=None, order_refunds_id=None):
        base_order_url = "/v1/orders/%s/order_refunds" % order_id
        return base_order_url if not order_refunds_id else "%s/%s" % (base_order_url, order_refunds_id)

    @classmethod
    def instance_url(cls, order_id=None, refund_id=None):
        return cls.class_url(order_id, refund_id)


class AppAPIResource(PingppObject):
    @classmethod
    def retrieve(cls, id, api_key=None, app=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh(app)
        return instance

    def refresh(self, app=None):
        self.refresh_from(self.request('get', self.instance_url(app)))
        return self

    @classmethod
    def class_name(cls):
        if cls == APIResource:
            raise NotImplementedError(
                'APIResource is an abstract class.  You should perform '
                'actions on its subclasses (e.g. Charge, Customer)')
        return str(urllib.quote_plus(cls.__name__.lower()))

    @classmethod
    def class_url(cls, app=None):
        cls_name = cls.class_name()
        if not app:
            from pingpp import app_id
            app = app_id
        return "/v1/apps/%s/%ss" % (app, cls_name)

    def instance_url(self, app=None):
        id = self.get('id')
        if not id:
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r' % (type(self).__name__, id), 'id')
        id = util.utf8(id)
        base = self.class_url(app)
        extn = urllib.quote_plus(id)
        return "%s/%s" % (base, extn)


class CreateableAppAPIResource(AppAPIResource):
    @classmethod
    def create(cls, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url(app)
        response, api_key = requestor.request('post', url, params)
        return convert_to_pingpp_object(response, api_key)


class ListableAppAPIResource(AppAPIResource):
    @classmethod
    def list(cls, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url(app)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)


class UpdateableAppAPIResource(AppAPIResource):
    def __init__(self, id=None, api_key=None, **params):
        super(UpdateableAppAPIResource, self).__init__(id, api_key, **params)
        self.cancel = self.__cancel
        self.confirm = self.__confirm
        self.delete = self.__delete
        self.update = self.__update

    @classmethod
    def _update_status(cls, id, app=None, method="post", status=None, **params):
        if status:
            params = {'status': status}
        requestor = api_requestor.APIRequestor()
        _instance = cls(id)
        url = _instance.instance_url()
        response, api_key = requestor.request(method, url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def update(cls, id, app=None, **params):
        return cls._update_status(id, app, 'put', **params)

    @classmethod
    def delete(cls, id, app=None, **params):
        return cls._update_status(id, app, 'delete', **params)

    @classmethod
    def cancel(cls, id, app=None):
        return cls._update_status(id, app, 'put', 'canceled')

    @classmethod
    def confirm(cls, id, app=None):
        return cls._update_status(id, app, 'put', 'pending')

    def __update_status(self, method='put', status=None):
        if status:
            params = {'status': status}
        self.refresh_from(self.request(method, self.instance_url(None), params))
        return self

    def __cancel(self, app=None):
        return self.__update_status('put', 'canceled')

    def __confirm(self, app=None):
        return self.__update_status('put', 'pending')

    def __update(self, app=None):
        return self.__update_status('post')

    def __delete(self, app=None):
        return self.__update_status('delete')


class CouponTemplate(CreateableAppAPIResource, ListableAppAPIResource, UpdateableAppAPIResource):
    def __init__(self, id=None, api_key=None, **params):
        super(CouponTemplate, self).__init__(id, api_key, **params)
        self.create_coupons = self.__create_coupons
        self.retrieve_coupons = self.__retrieve_coupons

    @classmethod
    def class_name(cls):
        return 'coupon_template'

    @classmethod
    def __operate_coupons(cls, api_key=None, app=None, coupon_tmpl=None, method='get', **params):
        _instance = cls(coupon_tmpl, api_key, **params)
        url = _instance.__return_req_url(app)
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request(method, url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def create_coupons(cls, api_key=None, app=None, coupon_tmpl=None, **params):
        response = cls.__operate_coupons(api_key, app, coupon_tmpl, method='post', **params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve_coupons(cls, api_key=None, app=None, coupon_tmpl=None, **params):
        response = cls.__operate_coupons(api_key, app, coupon_tmpl, method='get', **params)
        return convert_to_pingpp_object(response, api_key)

    def __create_coupons(self, app=None, **params):
        url = self.__return_req_url(app)
        self.refresh_from(self.request('post', url, params))
        return self

    def __retrieve_coupons(self, app=None):
        url = self.__return_req_url(app)
        self.refresh_from(self.request('get', url))
        return self

    def __return_req_url(self, app=None):
        return self.instance_url(app) + "/coupons"


class User(CreateableAppAPIResource, ListableAppAPIResource, UpdateableAppAPIResource, DeletableAPIResource):
    @classmethod
    def class_name(cls):
        return 'user'

    @classmethod
    def createBalanceTransfer(cls, api_key=None, app=None, user=None, **params):
        userObj = User(user, api_key=api_key)
        instance_url = userObj.instance_url(app) + "/transfers"
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('post', instance_url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def update(cls, api_key=None, app=None, user=None, **params):
        userObj = User(user, api_key=api_key)
        instance_url = userObj.instance_url(app)
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('put', instance_url, params)
        return convert_to_pingpp_object(response, api_key)


class UserAPIResource(PingppObject):
    @classmethod
    def retrieve(cls, id, api_key=None, app=None, user=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh(app, user)
        return instance

    def refresh(self, app=None, user=None, method='get'):
        self.refresh_from(self.request(method, self.instance_url(app, user)))
        return self

    @classmethod
    def class_name(cls):
        if cls == APIResource:
            raise NotImplementedError(
                'APIResource is an abstract class.  You should perform '
                'actions on its subclasses (e.g. Charge, Customer)')
        return str(urllib.quote_plus(cls.__name__.lower()))

    @classmethod
    def class_url(cls, app=None, user=None):
        cls_name = cls.class_name()
        if not app:
            from pingpp import app_id
            app = app_id
        return "/v1/apps/%s/users/%s/%ss" % (app, user, cls_name)

    def instance_url(self, app=None, user=None):
        id = self.get('id')
        if not id:
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r' % (type(self).__name__, id), 'id')
        id = util.utf8(id)
        base = self.class_url(app, user)
        extn = urllib.quote_plus(id)
        return "%s/%s" % (base, extn)


class CreateableUserAPIResource(UserAPIResource):
    @classmethod
    def create(cls, api_key=None, app=None, user=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url(app, user)
        response, api_key = requestor.request('post', url, params)
        return convert_to_pingpp_object(response, api_key)


class ListableUserAPIResource(UserAPIResource):
    @classmethod
    def list(cls, api_key=None, app=None, user=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url(app, user)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)


class UpdateableUserAPIResource(UserAPIResource):
    def __init__(self, id=None, api_key=None, **params):
        super(UpdateableUserAPIResource, self).__init__(id, api_key, **params)
        self.cancel = self.__cancel
        self.confirm = self.__confirm
        self.delete = self.__delete

    def __update_status(self, status, app=None, user=None):
        params = {'status': status}
        self.refresh_from(self.request('put', self.instance_url(app, user), params))
        return self

    def __cancel(self, app=None, user=None):
        return self.__update_status('canceled', app, user)

    def __confirm(self, app=None, user=None):
        return self.__update_status('pending', app, user)

    def __update(self, app=None, user=None, **params):
        return self.request('put', self.instance_url(app, user), params)

    def __delete(self, app=None, user=None):
        return self.__delete(app, user)

    @classmethod
    def _update_status(cls, id, app=None, user=None, status='canceled'):
        params = {'status': status}
        requestor = api_requestor.APIRequestor()
        _instance = cls(id)

        url = _instance.instance_url(app, user)
        response, api_key = requestor.request('put', url, params)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def __delete(cls, id, app=None, user=None):
        requestor = api_requestor.APIRequestor()
        _instance = cls(id)

        url = _instance.instance_url(app, user)
        response, api_key = requestor.request('delete', url)

        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def cancel(cls, id, app=None, user=None):
        return cls._update_status(id, app, user)

    @classmethod
    def confirm(cls, id, app=None, user=None):
        return cls._update_status(id, app, user, 'pending')


class BalanceTransaction(ListableAppAPIResource):
    @classmethod
    def class_name(cls):
        return 'balance_transaction'


class Withdrawal(CreateableUserAPIResource, ListableUserAPIResource, UpdateableUserAPIResource):
    @classmethod
    def class_name(cls):
        return "withdrawal"


class BatchWithdrawal(CreateableAppAPIResource, ListableAppAPIResource):
    @classmethod
    def class_name(cls):
        return "batch_withdrawal"


class Coupon(CreateableUserAPIResource, ListableUserAPIResource):
    @classmethod
    def class_name(cls):
        return 'coupon'

    @classmethod
    def delete(cls, id=None, app=None, api_key=None, user=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, user)
        response, api_key = requestor.request('delete', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def update(cls, id=None, app=None, api_key=None, user=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, user)
        response, api_key = requestor.request('put', url, params)
        return convert_to_pingpp_object(response, api_key)



class SubApp(CreateableAppAPIResource, ListableAppAPIResource, UpdateableAppAPIResource):
    @classmethod
    def class_name(cls):
        return 'sub_app'


class Channel(CreateableAppAPIResource, ListableAppAPIResource, UpdateableAPIResource):
    @classmethod
    def class_name(cls):
        return 'channel'

    def class_url(cls, app=None, sub_app_id=None, channel=None):
        app = util.utf8(app)
        sub_app_id = util.utf8(sub_app_id)
        if channel:
            channel = util.utf8(channel)
            return "/v1/apps/%s/sub_apps/%s/channels/%s" % (app, sub_app_id, channel)
        else:
            return "/v1/apps/%s/sub_apps/%s/channels" % (app, sub_app_id)

    def instance_url(self, app=None, sub_app_id=None, channel=None):
        return self.class_url(app, sub_app_id, channel)

    @classmethod
    def create(cls, api_key=None, app=None, sub_app_id=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, sub_app_id)
        response, api_key = requestor.request('post', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve(cls, api_key=None, app=None, sub_app_id=None, channel=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, sub_app_id, channel)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def update(cls, api_key=None, app=None, sub_app_id=None, channel=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, sub_app_id, channel)
        response, api_key = requestor.request('put', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def delete(cls, api_key=None, app=None, sub_app_id=None, channel=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, sub_app_id, channel)
        response, api_key = requestor.request('delete', url, params)
        return convert_to_pingpp_object(response, api_key)


class SettleAccount(CreateableUserAPIResource, UpdateableUserAPIResource, ListableUserAPIResource):
    @classmethod
    def class_name(cls):
        return 'settle_account'

    @classmethod
    def retrieve(cls, api_key=None, app=None, user=None, settle_account_id=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(settle_account_id, api_key)
        url = instance.instance_url(app, user)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def delete(cls, api_key=None, app=None, user=None, settle_account_id=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(settle_account_id, api_key)
        url = instance.instance_url(app, user)
        response, api_key = requestor.request('delete', url, params)
        return convert_to_pingpp_object(response, api_key)


class Royaltie(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    @classmethod
    def class_name(cls):
        return 'royaltie'

    @classmethod
    def update(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('put', url, params)
        return convert_to_pingpp_object(response, api_key)


class RoyaltySettlement(CreateableAPIResource, UpdateableAPIResource, ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'royalty_settlement'


class RoyaltyTransaction(ListableAPIResource):
    @classmethod
    def class_name(cls):
        return 'royalty_transaction'


class RoyaltyTemplate(CreateableAPIResource, UpdateableAPIResource, ListableAPIResource, DeletableAPIResource):
    @classmethod
    def class_name(cls):
        return 'royalty_template'

    @classmethod
    def update(cls, id, **params):
        _instance = cls(id)
        requestor = api_requestor.APIRequestor(_instance.api_key)
        url = _instance.instance_url()
        response, api_key = requestor.request('put', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def delete(cls, id, **params):
        _instance = cls(id)
        requestor = api_requestor.APIRequestor(_instance.api_key)
        url = _instance.instance_url()
        response, api_key = requestor.request('delete', url, params)
        return convert_to_pingpp_object(response, api_key)


class BalanceBonus(CreateableAppAPIResource, ListableAppAPIResource):
    @classmethod
    def class_name(cls):
        return 'balance_bonuse'


class BalanceTransfer(CreateableAppAPIResource, ListableAppAPIResource):
    @classmethod
    def class_name(cls):
        return 'balance_transfer'


class Recharge(CreateableAppAPIResource, ListableAppAPIResource):
    @classmethod
    def class_name(cls):
        return 'recharge'


class RechargeRefund(AppAPIResource):
    def __init__(self, id=None, api_key=None, **params):
        super(RechargeRefund, self).__init__(id, api_key, **params)

    @classmethod
    def class_name(cls):
        return 'recharge'

    @classmethod
    def create(cls, id=None, api_key=None, app=None, **params):
        instance = cls(id, api_key, **params)
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds" % (instance.class_url(), id)
        response, api_key = requestor.request('post', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve(cls, id, refund_id=None, api_key=None, app=None, **params):
        if not refund_id:
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r' % (type(cls).__name__, refund_id), 'id')
        instance = cls(id, api_key, **params)
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds/%s" % (instance.class_url(), id, refund_id)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)

    @classmethod
    def list(cls, id, api_key=None, app=None, **params):
        instance = cls(id, api_key, **params)
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds" % (instance.class_url(), id)
        response, api_key = requestor.request('get', url, params)
        return convert_to_pingpp_object(response, api_key)
