# Pingpp Python SDK
----------

## 简介
pingpp 文件夹下是 Python SDK 文件，<br>
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
pingpp.api_key = 'APP-KEY'
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
    app=dict(id='YOUR-APP-ID'),
    client_ip='127.0.0.1'

)
```

### 查询
```python
pingpp.Charge.retrieve('CHARGE-ID')
```

```python
pingpp.Charge.all()
```

### 退款
``` python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.create()
```

### 退款查询

```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.retrieve('REFUND-ID')
```

```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.retrieve('REFUND-ID')
```

### 微信红包
```python
pingpp.RedEnvelope.create()
```

### 查询
```python
pingpp.RedEnvelope.retrieve('RED-ID')
```

```python
pingpp.RedEnvelope.all()
```
### 查询 event
```python
pingpp.Event.retrieve('RED-ID')
```

## 查询 event 列表
```python
pingpp.Event.all()
```

### 微信企业付款

```python
tr = pingpp.Transfer.create(
    order_no='1234567890',
    channel='wx_pub',
    amount=100,
    currency='cny',
    app=dict(id='YOUR-APP-ID'),
    type='b2c',
    recipient='youropenid',
    extra=dict(user_name='User Name', force_check=True),
    description='description'
)
```

### 查询
```python
pingpp.Transfer.retrieve('TR-ID')
```

```python
pingpp.Transfer.all()
```

**详细信息请参考 [API 文档](https://pingxx.com/document/api?python)。**
