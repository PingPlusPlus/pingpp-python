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

### 退款
``` python
ch = pingpp.Charge.retrieve('CHARGE_ID')
re = ch.refunds.create(
    amount=1,
    description='Refund Description'
)
```

### 退款查询
```python
ch = pingpp.Charge.retrieve('CHARGE_ID')
re = ch.refunds.retrieve('REFUND_ID')
```

```python
ch = pingpp.Charge.retrieve('CHARGE_ID')
res = ch.refunds.all(limit=3)
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
pingpp.BatchRefund.retrieve("batchrefund20160801001")
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
pingpp.BatchTransfer.retrieve('BATCH_0001')
```

### 查询批量付款列表
```python
pingpp.BatchTransfer.list()
```

### 更新批量付款对象 (仅unionpay渠道支持)
```python
pingpp.BatchTransfer.cancel('BATCH_0001')
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
pingpp.Customs.retrieve("14201607013878045463")
```

**详细信息请参考 [API 文档](https://pingxx.com/document/api?python)。**
