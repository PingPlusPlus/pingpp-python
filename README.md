# PingPP-Python SDK ReadMe
----------

## 简介

pingpp 文件夹下是 Python SDK 文件，
example 文件夹里面是简单的接入示例，该示例仅供参考。

## 安装

	pip install pingpp
	
或使用setup.py手动安装
	
    python setup.py install

## 使用
#### 在接口调用之前，需执行如下代码：
```python
// 导入pingpp模块
import pingpp

// 设置API-KEY
pingpp.api_key = 'API-KEY'
```

## Pagination 分页
```python
chs = pingpp.Charge.all()
```

## Expanding 展开对象
```python
ch = pingpp.Charge.retrieve(id='CHARGE-ID', expand='app')
```
## Metadata 元数据
```python
ch = pingpp.Charge.create(
    order_no='1234567890',
    amount=1,
    app=dict(id='APP-ID'),
    channel='upmp',
    currency='cny',
    client_ip='CLIENT-IP',
    subject='test-subject',
    body='test-body',
    metadata=dict(color='red')
)
```
## 创建Charge对象
```python
ch = pingpp.Charge.create(
    order_no='1234567890',
    amount=1,
    app=dict(id='APP-ID'),
    channel='upmp',
    currency='cny',
    client_ip='CLIENT-IP',
    subject='test-subject',
    body='test-body',
)
```
    
## 查询 Charge 对象
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
```
    
## 创建 Refund 对象
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.create(description='desc', amount=1)
```
    
## 查询 Refund 对象
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.retrieve('REFUND-ID')
```
    
## 查询 Refund 对象列表
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
res = ch.refunds.all(limit=3)
```
    
## 集成与 C-SDK 通信的 HTTP 接口
以Flask为例：
```
pip install flask
```
可以使用以下的样例代码:
```
import pingpp
from flask import Flask,request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def do_charge():
    form = request.get_json()
    response_charge = pingpp.Charge.create(api_key="YOUR_KEY", **form)
    return str(response_charge)
#本例用Content-Type:application/json形式的请求举例
if __name__ == '__main__':
    app.run(debug=True)
```
执行此脚本:
```
python xxx.py
```
向这个地址发送一个**POST**请求
(请务必用标准Json，并附带**Content-Type:application/json**的HTTP Header)
```
http://127.0.0.1:5000/
```
检查结果
It's Done!