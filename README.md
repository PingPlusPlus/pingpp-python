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
[示例代码](example/)

### 初始化
```python
pingpp.api_key = 'YOUR_KEY'
```

### 开启日志
```python
pingpp.log = 'debug'  # 支持 debug 和 info
```

或者设置环境变量 `PINGPP_LOG`
```bash
export PINGPP_LOG=debug
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

重试延时设置（秒）
```python
pingpp.network_retry_delay = 0.5
```

### 支付
```python
ch = pingpp.Charge.create(
    order_no='201123456789',
    channel='alipay',
    amount=100,
    subject='Item Subject',
    body='Item Body',
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
params = {
    "app": {"id": "APP_ID"},
    "limit": 3,
}
pingpp.Charge.list(**params)
```

### 线下渠道交易撤销
```python
pingpp.Charge.reverse('CHARGE_ID')
```

### 退款
```python
re = pingpp.Charge.refund("CHARGE_ID"
                          description='Your Descripton',
                          amount=1)
```

### 退款列表
```python
params = {
    'limit': 3,
}
refunds = pingpp.Charge.list_refunds('CHARGE_ID', **params)
```

### 退款查询
```python
re = pingpp.Charge.retrieve_refund('CHARGE_ID', 'REFUND_ID')
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
pingpp.RedEnvelope.list()
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
pingpp.Transfer.list()
```

## Batch Refunds 批量退款
### 创建 Batch refund 对象
```python
pingpp.BatchRefund.create（
    "app": 'APP_ID',
    "batch_no": "batchrefund2010801001",
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
params = {
    "app": 'APP_ID',
    "batch_no": "batchrefund2010801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_L8qn10mLmr1GS8e5OODmHaL4",
        "ch_fdOmHaLmLmr1GOD4qn1dS8e5"
    ]
}
pingpp.BatchTransfer.create(**params)
```

### 查询批量付款
```python
pingpp.BatchTransfer.retrieve('BATCH_TRANSFER_ID')
```

### 查询批量付款列表
```python
pingpp.BatchTransfer.list(app="APP_ID", per_page=3)
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
    app='APP_ID',
    charge='CHARGE_ID',
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
params = {
    "app": 'APP_ID',
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

pingpp.Order.create(**params)
```

### 商品订单支付

```python
params = {
    "charge_amount": 10,
    "channel": "balance"
}
pingpp.Order.pay("ORDER_ID", **params)
```

### 商品订单取消

```python
pingpp.Order.cancel("ORDER_ID")
```

### 商品订单查询
```python
pingpp.Order.retrieve("ORDER_ID")
```

### 商品订单列表

```python
pingpp.Order.list()
```

### 商品订单charge列表查询
```python
pingpp.Order.list_charges("ORDER_ID")
```

### 商品订单charge查询
```python
pingpp.Order.retrieve_charge("ORDER_ID", "CHARGE_ID")
```

### 商品订单退款
```python
params = {
    "description": "Your description",
    "charge": "CHARGE_ID",
    "charge_amount": 10
}
pingpp.Order.refund("ORDER_ID", **params)
```

### 商品订单退款查询
```python
pingpp.Order.retrieve_refund("ORDER_ID", "REFUND_ID")
```

### 商品订单退款列表查询
```python
params = {
    "per_page": 3
}
pingpp.Order.list_refunds("ORDER_ID", **params)
```

## 账户系统
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
### 用户充值查询
```python
pingpp.Recharge.retrieve("RECHARGE_ID")
```
### 用户充值列表
```python
params = {
    "page": 1,
    "per_page": 3,
}
pingpp.Recharge.list(**params)
```

### 用户充值退款创建
```python
params = {
    "description": "Your description",
    "metadata": {}
}
pingpp.Recharge.refund("RECHARGE_ID", **params)
```

### 用户充值退款查询
```python
pingpp.Recharge.retrieve_refund("RECHARGE_ID", "REFUND_ID")
```

### 用户充值退款列表
```python
params = {
    "page": 1,
    "per_page": 3,
}
pingpp.Recharge.list_refunds("RECHARGE_ID", **params)
```

### 创建账户
```python
params = {
    "id": "user_001", # id 唯一
    "address": "address_1",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {},
    "mobile": None,
    "name": "Your user name"
}
pingpp.User.create(app="APP_ID", **params)
```

### 获取账户列表
```python
params = {
    "page": 1,
    "per_page": 3,
}
pingpp.User.list(app="APP_ID", **params)
```

### 获取账户详细信息
```python
pingpp.User.retrieve("user_001", app="APP_ID")
```

### 更新账户信息
```python
params = {
    "address": "address_1",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {},
    "mobile": None,
    "name": "Your user name"
}
pingpp.User.update("user_001", app="APP_ID", **params)
```

### 用户账户交易明细
```python
pingpp.BalanceTransaction.retrieve("TXN_ID",
                                   app="APP_ID")
```

### 用户账户交易查询列表
```python
params = {
    "page": 1,
    "per_page": 3,
}
pingpp.BalanceTransaction.list(app="APP_ID", **params)
```

### 余额转账
```python
pingpp.BalanceTransfer.create(app="APP_ID", **params)
```

### 余额提现申请
```python
params = {
    "user": "user_001",
    "amount": 20000,
    "user_fee": 50,
    "description": "Description",
    "extra": {
        "card_number": "6225210207073918",
        "user_name": "姓名",
        "open_bank_code": "0102",
        "prov": "上海",
        "city": "上海"
    }
}
pingpp.Withdrawal.create(app="APP_ID", **params)
```

### 余额提现明细
```python
pingpp.Withdrawal.retrieve("WITHDRAWAL_ID", app="APP_ID")
```

### 余额提现取消
```python
pingpp.Withdrawal.cancel("WITHDRAWAL_ID", app="APP_ID")
```

### 余额提现列表
```python
params = {
    "page": 1,
    "per_page": 3,
    "user": "user_001"
}
pingpp.Withdrawal.list(app="APP_ID", **params)
```

## 优惠券
### 创建单个优惠券
```python
params = {
    "coupon_template": "300116082415452100000700",
}
pingpp.Coupon.create("user_001", **params)
```

### 更新优惠券
```python
params = {
    "coupon_template": "300116082415452100000700",
    "metadata": {
        "key": "value"
    }
}
pingpp.Coupon.update("user_001", "coupon_id_001", **params)
```

### 删除优惠券
```python
pingpp.Coupon.delete("user_001", "coupon_id_001")
```

### 查询优惠券
```python
pingpp.Coupon.retrieve("user_001", "coupon_id_001")
```

### 查询用户优惠券列表
```python
pingpp.Coupon.list("user_001", per_page=3)
```

## 优惠券模板
### 创建优惠券模板
```python
params = {
    "name": "25OFF",
    "type": 1,
    "percent_off": 25,
    "amount_available": 10000,
    "max_circulation": 1000,
    "metadata": {
    },
    "expiration": null
}
pingpp.CouponTemplate.create(**params)
```

### 获取优惠券模板列表
```python
pingpp.CouponTemplate.list(per_page=3)
```

### 获取优惠券模板明细
```python
pingpp.CouponTemplate.retrieve("COUPON_TMPL_001")
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
pingpp.CouponTemplate.list_coupons("COUPON_TMPL_001", per_page=3)
```

### 创建单个优惠券
```python
pingpp.CouponTemplate.create_coupons("COUPON_TMPL_001", **params)
```

### 创建批量付款
```python
params = {
    "app": "APP_ID",
    "batch_no": "batchrefund20100801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_L8qn10mLmr1GS8e5OODmHaL4",
        "ch_fdOmHaLmLmr1GOD4qn1dS8e5"
    ]
}
pingpp.BatchTransfer.create(**params)
```

### 查询批量付款
```python
pingpp.BatchTransfer.retrieve('BATCH_TRANSFER_ID')
```

### 查询批量付款列表
```python
params = {
    "page": 1,
    "per_page": 3
}
pingpp.BatchTransfer.list(**params)
```

### 批量提现确认
```python
params = {
    "withdrawals": [
        "1701611150302360654",
        "1701611151015078981"
    ]
}
pingpp.BatchWithdrawal.create(app="APP_ID", **params)
```

### 批量提现确认查询
```python
pingpp.BatchWithdrawal.retrieve("BATCH_WITHDRAWAL_ID", app="APP_ID")
```

### 创建子商户
```python
params = {
    'display_name': 'sub_app_display_name',
    'user': 'user_101',
    'metadata': {
        'key': 'value'
    },
    'description': 'Your description'
}
sub_app = pingpp.SubApp.create(app="APP_ID", **params)
```

### 查询子商户
```python
pingpp.SubApp.retrieve("app_1Gqj58ynP0mHeX1q", app="APP_ID")
```

### 删除子商户
```python
pingpp.SubApp.delete("app_1Gqj58ynP0mHeX1q", app="APP_ID")
```

### 查询子商户列表
```python
pingpp.SubApp.list(app="APP_ID")
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
pingpp.SubApp.create_channel("app_1Gqj58ynP0mHeX1q", app="APP_ID", **params)
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
pingpp.SubApp.update_channel("app_1Gqj58ynP0mHeX1q", 'alipay', **updateParams)
```
### 删除子商户渠道参数
```python
pingpp.SubApp.delete_channel('app_1Gqj58ynP0mHeX1q', 'alipay')
```

### 获取子商户渠道参数
```python
pingpp.SubApp.retrieve_channel('app_1Gqj58ynP0mHeX1q', 'alipay')
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
pingpp.SettleAccount.create('user_001', app="APP_ID", **params)

# 创建结算账号-支付宝渠道
params = {
    "channel": "alipay",
    "recipient": {
        "account": "account@domain.com",
        "name": "李四",
        "type": "b2c"  # 转账类型。b2c：企业向个人付款。
    }

}
pingpp.SettleAccount.create('user_001', app="APP_ID", **params)

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
pingpp.SettleAccount.create('user_001', app="APP_ID", **params)
```

### 查询结算账号
```python
pingpp.SettleAccount.retrieve('user_001', 'SETTLE_ACCOUNT_ID', app="APP_ID")
```

### 删除结算账号
```python
pingpp.SettleAccount.delete('user_001', 'SETTLE_ACCOUNT_ID', app="APP_ID")
```

### 查询结算账号列表
```python
pingpp.SettleAccount.list('user_001', app="APP_ID")
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
pingpp.Royalty.update(**params)
```

### 查询分润对象
```python
pingpp.Royalty.retrieve('ROYALTY_ID')
```

### 查询分润对象列表
```python
params = {
    'page': 1,
    'per_page': 3
}
pingpp.Royalty.list(**params)
```

### 创建分润结算对象
```python
params = {
    "payer_app": "APP_ID",
    "method": "unionpay",
    "recipient_app": "APP_ID_2",
    "created": {
        "gt": 1488211200,
        "lte": 1488297600
    }
}
pingpp.RoyaltySettlement.create(**params)
```

### 查询分润结算对象
```python
pingpp.RoyaltySettlement.retrieve('ROYALTY_SETTLEMENT_ID')
```

### 更新分润结算对象
```python
# 更新分润结算对象-确认
pingpp.RoyaltySettlement.confirm('ROYALTY_SETTLEMENT_ID')
# 更新分润结算对象-取消
pingpp.RoyaltySettlement.cancel('ROYALTY_SETTLEMENT_ID')
```

### 查询分润结算列表
```python
pingpp.RoyaltySettlement.list(**params)
```

### 查询分润明细
```python
params = {
    "page": 1,
    "per_page": 15
}
pingpp.RoyaltyTransaction.list(**params)
```

### 查询分润明细列表
```python
pingpp.RoyaltyTransaction.retrieve('ROYALTY_TRANSACTION_ID')
```

**详细信息请参考 [API 文档](https://pingxx.com/document/api?python)。**
