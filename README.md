# Pingpp Python SDK
---

## 简介
pingpp 文件夹下是 Python SDK 文件，  
example 文件夹里面是简单的接入示例，该示例仅供参考。

## 安装
```
pip install pingpp
```
或使用 setup.py 手动安装
```
python setup.py install
```

## 接入方法

### 初始化
```python
pingpp.api_key = 'YOUR_KEY'
```

### 设置请求签名密钥
密钥需要你自己生成，公钥请填写到 [Ping++ Dashboard](https://dashboard.pingxx.com)  
设置你的私钥路径
```python
pingpp.private_key_path = '/path/to/your_rsa_private_key.pem'
```

### 设置重试
设置重试次数，`0` 表示不重试，默认为 `1`。
```python
pingpp.max_network_retries = 0
```

当服务端返回 `502` 时，是否根据返回内容(阿里高防返回)来判断是否重试。`False` 表示只要是 `502`，全部重试。默认为 `True`。
```python
pingpp.bad_gateway_match = False
```

### 支付
```python
ch = pingpp.Charge.create(
    order_no='123456789',
    channel='alipay',
    amount=1,
    subject='test-subject',
    body='test-body',
    currency='cny',
    app=dict(id='APP_ID'),
    client_ip='127.0.0.1'
)
```

### 查询
```python
pingpp.Charge.retrieve('CHARGE_ID')
```

```python
pingpp.Charge.all()
```

### 线下渠道交易撤销
```python
pingpp.Charge.reverse('ch_DqnrL8f5GCuLzvvLW1j5OWTK')
```

### 退款
```python
ch = pingpp.Charge.retrieve("CHARGE_ID")
ch.refunds.create(description='Your Descripton', amount=1)
```

### 退款列表
```python
params = {
    'limit': 3,
}
charge = pingpp.Charge.retrieve('ch_W5CCe9uPujnDLqvbvH9OOS8S')
charge.refund_list(**params)
```

### 退款查询
```python
charge = pingpp.Charge.retrieve('CHARGE_ID')
charge.refund_retrieve('REFUND_ID')
```

### 微信红包
```python
pingpp.RedEnvelope.create(
    order_no='123456789',
    channel='wx_pub',
    amount=100,
    subject='Your Subject',
    body='Your Body',
    currency='cny',
    app=dict(id='APP_ID'),
    extra=dict(send_name='Send Name'),
    recipient='User Openid',
    description='Your Description'
)
```

### 查询
```python
pingpp.RedEnvelope.retrieve('RED_ID')
```

```python
pingpp.RedEnvelope.all()
```

### 查询 event
```python
pingpp.Event.retrieve('EVENT_ID')
```

### 微信企业付款

```python
tr = pingpp.Transfer.create(
    order_no='1234567890',
    channel='wx_pub',
    amount=100,
    currency='cny',
    app=dict(id='APP_ID'),
    type='b2c',
    recipient='User Openid',
    extra=dict(user_name='User Name', force_check=False),
    description='Your Description'
)
```

### 查询
```python
pingpp.Transfer.retrieve('TRANSFER_ID')
```

```python
pingpp.Transfer.all()
```

## Batch Refunds 批量退款
### 创建 Batch refund 对象
```python
pingpp.BatchRefund.create（
    "app": app_id,
    "batch_no": "batchrefund20160801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_L8qn10mLmr1GS8e5OODmHaL4",
        "ch_fdOmHaLmLmr1GOD4qn1dS8e5"
    ]
)
```

### 查询 Batch refund 对象
```python
pingpp.BatchRefund.retrieve('BATCH_REFUND_ID')
```

### 查询 Batch refund 对象列表
```python
pingpp.BatchRefund.list()
```
## Batch Transfers 批量企业付款
### 创建批量付款
```python
req_params = {
    "app": app_id,
    "batch_no": "batchrefund20160801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_L8qn10mLmr1GS8e5OODmHaL4",
        "ch_fdOmHaLmLmr1GOD4qn1dS8e5"
    ]
}
pingpp.BatchTransfer.create(**req_params)
```

### 查询批量付款
```python
pingpp.BatchTransfer.retrieve('BATCH_TRANSFER_ID')
```

### 查询批量付款列表
```python
pingpp.BatchTransfer.list()
```

### 更新批量付款对象 (仅unionpay渠道支持)
```python
pingpp.BatchTransfer.cancel('BATCH_TRANSFER_ID')
```

## 身份证银行卡信息认证接口
```python
params = {
    "app": "APP_ID",
    "data": {
        "id_name": "张三",
        "id_number": "320291198811110000",
        "card_number": "6201111122223333"
    },
    "type": "bank_card"
}
pingpp.Identification.create(**params)
```

## 报关接口
### 请求报关接口
```python
pingpp.Customs.create(
    app='App ID',
    charge='Charge ID',
    channel='alipay',
    amount=100,  # 报关金额, 人民币单位：分
    customs_code='GUANGZHOU',
    trade_no='15112496832609'
)
```

### 查询报关接口
```python
pingpp.Customs.retrieve("CUSTOMS_ID")
```

## 订单
### 创建商品订单
```python
order_info = {
  "app": app_id,
  "uid": "15800973612",
  "merchant_order_no": "88888888888",
  "coupon":"300316082514255200000900",
  "amount": "30",
  "client_ip": "127.0.0.1",
  "currency": "cny",
  "subject": "test1",
  "body": "test1body1",
  "description": "test1-description",
  "time_expire": int(time.time()) + 1000
}

pingpp.Order.create(**order_info)
```

### 商品订单支付

```python
params = {
  "charge_amount": 0,
  "balance_amount": 10
}
pingpp.Order.pay( "order_0001", **params)
```

### 商品订单取消

```python
pingpp.Order.cancel("2011608250000000971")
```

### 商品订单查询
```python
pingpp.Order.retrieve("2011608250000000971")
```

### 商品订单列表

```python
pingpp.Order.all()
```

### 商品订单charge列表查询
```python
pingpp.Order.charge_list("2001708150000313781")
```

### 商品订单charge查询
```python
pingpp.Order.charge_retrieve("2001708150000313781", "ch_SS0GqLWrrD00Ga1e1GW9WXjP")
```

### 商品订单退款
```python
params = {
    "description": "Your description"
}
order_refund = pingpp.OrderRefunds.create(order_id="2011611140000003181", **params)
```
### 商品订单退款查询
```python
pingpp.OrderRefunds.retrieve(order_id="2011611140000003181", refund_id="re_HK0aXLnfjTy9u1aj14PCyzLG")
```

### 商品订单退款列表查询
```python
pingpp.OrderRefunds.list(order_id="2011611140000003181")
```

### 用户充值
```python
params = {
    "user": "user_test_01",
    "charge": {
        "amount": 100,
        "channel": "alipay_qr",
        "order_no": "8888888888888",
        "subject": "Your subject",
        "body": "Your body",
        "time_expire": "1502770016",
        "client_ip": "127.0.0.1",
        "extra": {}
    },
    "balance_bonus": {
        "amount": 100,
    },
    "from_user": "user_test_02",
    "description": "Your description",
    "metadata": {}
}

recharge = pingpp.Recharge.create(**params)
```
#### 用户充值查询
```python
pingpp.Recharge.retrieve("220170815426362060800000"))
```
#### 用户充值列表
```python
list_param = {
    "page": 1,
    "per_page": 10,
}
pingpp.Recharge.list(**list_param))
```

#### 用户充值退款创建
```python
refund_param = {
    "description": "Your description",
    "metadata": {}
}
pingpp.RechargeRefund.create("220170815426362060800000", **refund_param))
```

#### 用户充值退款查询
```python
pingpp.RechargeRefund.retrieve("220170815426362060800000", "re_PibXTGubzzbLf5Wvj1HyzLmT")
```

#### 用户充值退款列表
```python
pingpp.RechargeRefund.list("220170815426362060800000"))
```

## 账户系统
### 创建账户
```python
request_info = {
    "id": "test_user_0005", # id 唯一
    "address": "address_1",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {},
    "mobile": None,
    "name": "Your user name"
}
pingpp.User.create(app=app_id, **request_info)
```
### 获取账户列表
```python
pingpp.User.list()
```
### 获取账户详细信息
```python
pingpp.User.retrieve("test_user_0002", app=app_id)
```

### 更新账户信息
```python
request_info = {
    "address": "address_1",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {},
    "mobile": None,
    "name": "Your user name"
}
pingpp.User.update(app=app_id,user="USER_TEST_0001", **request_info)
```

### 用户账户交易明细
```python
pingpp.BalanceTransaction.retrieve(app=app_id, user="test_user_001",id="txn_14697807964587241560000001")
```
### 用户账户交易查询列表
```python
pingpp.BalanceTransaction.list(app=app_id,user="test_user_001")
```

### 余额转账
```python
pingpp.User.createBalanceTransfer(app=app_id, user="test_user_02")
```

### 余额提现申请
```python
request_info = {
    "amount": 20000,
    "user_fee": 50,
    "description": "test232description",
    "extra": {
        "card_number": "6225210207073918",
        "user_name": "姓名",
        "open_bank_code": "0102",
        "prov": "上海",
        "city": "上海"
    }
}
pingpp.Withdrawal.create(user="user_id_001", **request_info)
```

### 余额提现明细
```python
pingpp.Withdrawal.retrieve("withDrawal_0002", app=app_id, user="user_id_001")
```

### 余额提现取消
```python
pingpp.Withdrawal.cancel("withDrawl_0002")
```

### 余额提现列表
```python
pingpp.Withdrawal.list(user="user_id_001")
```

## 优惠券
### 创建单个优惠券
```python
params = {
    "coupon_template": "300116082415452100000700",
}
pingpp.Coupon.create(user="user_test_001", **params)
```

### 更新优惠券
```python
params = {
    "coupon_template": "300116082415452100000700",
    "metadata": {
        "key": "value"
    }
}
pingpp.Coupon.update("coupon_id_001", user="user_test_001", **params)
```

### 删除优惠券
```python
delete_coupon = pingpp.Coupon.delete("coupon_id_001", user="user_test_001")
```

### 查询优惠券
```python
pingpp.Coupon.retrieve("coupon_id_001", user="user_test_001")
```

### 查询用户优惠券列表
```python
pingpp.Coupon.list(user="user_test_001")
```

## 优惠券模板
### 创建优惠券模板
```python
params={
    "name": "25OFF",
    "type": 1,
    "percent_off": 25,
    "amount_available": 10000,
    "max_circulation": 1000,
    "metadata": {
    },
    "expiration": null
}
pingpp.CouponTemplate.create(app=app_id, **params)
```

### 获取优惠券模板列表
```python
pingpp.CouponTemplate.list()
```

### 获取优惠券模板明细
```python
pingpp.CouponTemplate.retrieve("coupon_id_001", user="user_test_001")
```

### 更新优惠券模板
```python
pingpp.CouponTemplate.update("COUPON_TMPL_001", **params)
```

### 删除优惠券模板
```python
pingpp.CouponTemplate.delete("COUPON_TMPL_001")
```

### 查询优惠券模板下的优惠券列表
```python
pingpp.CouponTemplate.retrieve_coupons(coupon_tmpl="COUPON_TMPL_001")
```

### 创建单个优惠券
```python
pingpp.CouponTemplate.create_coupons(app=app_id, coupon_tmpl="COUPON_TMPL_001")
```

### 创建批量付款
```python
req_params = {
    "app": app_id,
    "batch_no": "batchrefund20160801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_L8qn10mLmr1GS8e5OODmHaL4",
        "ch_fdOmHaLmLmr1GOD4qn1dS8e5"
    ]
}
pingpp.BatchTransfer.create(**req_params)
```

### 查询批量付款
```python
pingpp.BatchTransfer.retrieve('BATCH_0001')
```

### 查询批量付款列表
```python
pingpp.BatchTransfer.list()
```

### 批量提现确认
```python
params = {
    "withdrawals": [
        "1701611150302360654",
        "1701611151015078981"
    ]
}
pingpp.BatchWithdrawal.create(app=app_id, **params)
```

### 批量提现确认查询
```python
pingpp.BatchWithdrawal.retrieve("bw_123456",app=app_id)
```

### 创建子商户
```python
params = {
    'display_name': 'sub_app_display_name',
    'user': 'test_user_031',
    'metadata': {
        'key': 'value'
    },
    'description': 'Your description'
}
sub_app = pingpp.SubApp.create(app=pingpp.app_id, **params)
```
### 查询子商户
```python
pingpp.SubApp.retrieve(app=pingpp.app_id, id='app_1Gqj58ynP0mHeX1q')
```
### 删除子商户
```python
pingpp.SubApp.delete(app=app_id, id='app_1Gqj58ynP0mHeX1q')
```
### 查询子商户列表
```python
pingpp.SubApp.list(app=pingpp.app_id)
```
### 配置子商户渠道参数
```python
params = {
    "banned_msg": None,
    "channel": "alipay",
    "description": "Your description",
    "params": {
        "alipay_account": "Your alipay Account",
        "alipay_app_id": "Your Alipay App ID",
        "alipay_app_public_key": "-----BEGIN PUBLIC KEY-----\nMIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFb\nCNuJ2zVhBjp377rnWIlf0ogfW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJl\nkJ3\/DxZIqBc7i9j\/h75Lx\/0nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIv\nqNqEZwwAS7C\/rmn1AgMBAAE=\n-----END PUBLIC KEY-----",
        "alipay_app_public_key_rsa2": None,
        "alipay_mer_app_private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFbCNuJ2zVhBjp377rnWIlf0ogf\nW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJlkJ3\/DxZIqBc7i9j\/h75Lx\/0n\nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIvqNqEZwwAS7C\/rmn1AgMBAAEC\ngYBuV5mUaaoyXovA5J4Mj95DNj0hKMpOJkds70TBMNIhxqlsr5rVgnvSHCS8COLI\nCPdpGfT1gyCR9+kNQd+4xg6IeqDpL3CqIgtZi+qRGpVJgXW1x\/oZYzzpqD4Q0\/4U\nUmOp6Mo9bDPnYKSVgReWWNtCdKncWvBE4gbYadHXYva6FQJBALfW1SPWzA2i7fQu\ncG89pPkBQOMG\/pd8JyeBgEHOv2\/nBN9zqir\/zMMFd+EbI00A1goy1pu4IVvt+GFG\nq\/\/5ZE8CQQCp93SxpFjbB49s5F+Lvs0PR08IzfxY9eoCrd9xt4hXqmksUYcodBtu",
        "alipay_mer_app_private_key_rsa2": None,
        "alipay_pid": "alipay_pid",
        "alipay_refund_nopwd": False,
        "alipay_security_key": "alipay_security_key",
        "alipay_sign_type": "rsa",
        "alipay_version": 1,
        "fee_rate": 80
    }
}
pingpp.Channel.create(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', **params)
```
### 更新子商户渠道参数
```python
updateParams = {
    'description': 'Your Channel description',
    'params': {
        "alipay_account": "Your alipay Account",
        "alipay_app_id": "Your Alipay App ID",
        "alipay_app_public_key": "-----BEGIN PUBLIC KEY-----\nMIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFb\nCNuJ2zVhBjp377rnWIlf0ogfW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJl\nkJ3\/DxZIqBc7i9j\/h75Lx\/0nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIv\nqNqEZwwAS7C\/rmn1AgMBAAE=\n-----END PUBLIC KEY-----",
        "alipay_app_public_key_rsa2": None,
        "alipay_mer_app_private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFbCNuJ2zVhBjp377rnWIlf0ogf\nW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJlkJ3\/DxZIqBc7i9j\/h75Lx\/0n\nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIvqNqEZwwAS7C\/rmn1AgMBAAEC\ngYBuV5mUaaoyXovA5J4Mj95DNj0hKMpOJkds70TBMNIhxqlsr5rVgnvSHCS8COLI\nCPdpGfT1gyCR9+kNQd+4xg6IeqDpL3CqIgtZi+qRGpVJgXW1x\/oZYzzpqD4Q0\/4U\nUmOp6Mo9bDPnYKSVgReWWNtCdKncWvBE4gbYadHXYva6FQJBALfW1SPWzA2i7fQu\ncG89pPkBQOMG\/pd8JyeBgEHOv2\/nBN9zqir\/zMMFd+EbI00A1goy1pu4IVvt+GFG\nq\/\/5ZE8CQQCp93SxpFjbB49s5F+Lvs0PR08IzfxY9eoCrd9xt4hXqmksUYcodBtu",
        "alipay_mer_app_private_key_rsa2": None,
        "alipay_pid": "alipay_pid",
        "alipay_refund_nopwd": False,
        "alipay_security_key": "alipay_security_key",
        "alipay_sign_type": "rsa",
        "alipay_version": 1,
        "fee_rate": 80
    },
    'banned': False
}
pingpp.Channel.update(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', channel='alipay',
                                    **updateParams)
```
### 删除子商户渠道参数
```python
pingpp.Channel.delete(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', channel='alipay')
```
### 获取子商户渠道参数
```python
pingpp.Channel.retrieve(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', channel='alipay')
    print('retrieve sub_app channel list:', channel_list)
```
### 创建结算账号
```python
# 创建结算账号-中国银联渠道
params = {
    "channel": "unionpay",
    "recipient": {
        "account": "6214850266666666",
        "name": "11111111",
        "type": "b2c",  # 转账类型。b2c：企业向个人付款，b2b：企业向企业付款。
        "open_bank": "招商银行",
        "open_bank_code": "0308"
    }

}
pingpp.SettleAccount.create(app=pingpp.app_id, user='test_user_003', **params)
# 创建结算账号-支付宝渠道
params = {
    "channel": "alipay",
    "recipient": {
        "account": "account@domain.com",
        "name": "李四",
        "type": "b2c"  # 转账类型。b2c：企业向个人付款。
    }

}
pingpp.SettleAccount.create(app=pingpp.app_id, user='test_user_003', **params)
# 创建结算账号-微信渠道
params = {
    "channel": "wx_pub",
    "recipient": {
        "account": "your_open_id",
        "name": "王五",
        "type": "b2c",  # 转账类型。b2c：企业向个人付款。
        "force_check": False
    }

}
pingpp.SettleAccount.create(app=pingpp.app_id, user='test_user_003', **params)
```
### 查询结算账号
```python
pingpp.SettleAccount.retrieve(app=pingpp.app_id, user='test_user_003', settle_account_id='320117032014485200000201')
```
### 删除结算账号
```python
pingpp.SettleAccount.delete(app=pingpp.app_id, user='test_user_003', settle_account_id='320117032014485200000201')
```
### 查询结算账号列表
```python
pingpp.SettleAccount.list(app=pingpp.app_id, user='test_user_003')
```
### 批量更新分润对象
```python
params = {
    "ids": [
        "170301124238000111",
        "170301124238000211"
    ],
    "method": "manual",
    "description": "Your description"
}
pingpp.Royaltie.update(**params)
```
### 查询分润对象
```python
pingpp.Royaltie.retrieve('410170320160900002')
```
### 查询分润对象列表
```python
params = {
    'page': 1,
    'per_page': 15
}
pingpp.Royaltie.all(**params)
```
### 创建分润结算对象
```python
params = {
    "payer_app": pingpp.app_id,
    "method": "unionpay",
    "recipient_app": pingpp.app_id,
    "created": {
        "gt": 1488211200,
        "lte": 1488297600
    }
}
pingpp.RoyaltySettlement.create(**params)
```
### 查询分润结算对象
```python
pingpp.RoyaltySettlement.retrieve(id='430170320150300001')
```
### 更新分润结算对象
```python
# 更新分润结算对象-确认
pingpp.RoyaltySettlement.confirm(id='430170320150300001')
# 更新分润结算对象-取消
pingpp.RoyaltySettlement.cancel(id='430170320150300001')
```
### 查询分润结算列表
```python
pingpp.RoyaltySettlement.all(**params)
```
### 查询分润明细
```python
params = dict(
    page = 1,
    per_page = 15
)
pingpp.RoyaltyTransaction.all(**params)
```
### 查询分润明细列表
```python
pingpp.RoyaltyTransaction.retrieve(id='440170320155300006')
```


**详细信息请参考 [API 文档](https://pingxx.com/document/api?python)。**
