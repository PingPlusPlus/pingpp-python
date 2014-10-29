# 安装
    python setup.py install

# 使用
#### 在接口调用之前，需执行如下代码：
    // 导入pingpp模块
    import pingpp
    
    // 设置API-KEY
    pingpp.api_key = 'API-KEY'

## Pagination 分页
    chs = pingpp.Charge.all()

## Expanding 展开对象
    ch = pingpp.Charge.retrieve(id='CHARGE-ID', expand='app')

## Metadata 元数据
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

## 创建Charge对象
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
    
## 查询 Charge 对象
    ch = pingpp.Charge.retrieve('CHARGE-ID')
    
## 创建 Refund 对象
    ch = pingpp.Charge.retrieve('CHARGE-ID')
    re = ch.refunds.create(description='desc', amount=1)
    
## 查询 Refund 对象
    ch = pingpp.Charge.retrieve('CHARGE-ID')
    re = ch.refunds.retrieve('REFUND-ID')
    
## 查询 Refund 对象列表
    ch = pingpp.Charge.retrieve('CHARGE-ID')
    res = ch.refunds.all(limit=3)
    