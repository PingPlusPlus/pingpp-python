# 2.4.0
- 修改
    - 自动重试机制
    - 由于pycrypto官方已[不再维护](https://github.com/dlitz/pycrypto/issues/173),将 pycrypto 改为推荐的 pycryptodome
    - 合并账户系统到主分支

# 2.3.0
- 增加
    - `/v1/transfer` `/v1/batch_transfer` 新增余额渠道示例
    - 余额充值接口
    - 余额转账接口
    - 余额赠送接口
    - 订单charge列表,查询接口
    - 分润模板接口
- 修改
    - 原v1/recharge 接口废弃,请使用/v1/APP_ID/recharges接口
    - 账户系统1.3.1子商户对象新增level,parent_app 字段,创建参数新增 parent_app 参数,包括子商户创建,查询,列表
    - 原 asset_transactions transaction_statistics接口下线
    - order退款列表order_refund变更为refund对象,order消费订单支持charge接口退款
    - 原order退款创建、查询列表返回的order_refund变更为refund对象.
    - order对象新增charge对象列表，actual_amount参数;
    - 订单支付接口支持传商户订单号,此时支付的商户订单号不等于订单的商户订单号
    - 原用户余额转账transfers 接口废弃请使用 balance_transfers 接口
    - 原余额提现withdrawals废弃 请使用/v1/apps/APP_ID/withdrawals 接口
    - 原余额收款接口 receipts 废弃,请使用 balance_bonus 接口

# 2.2.0
- 增加:
    - 子商户接口
    - 子商户渠道参数配置接口
    - 结算账号接口
    - 分润接口
    - 分润结算接口
    - 分润结算明细接口
- 修改
    - 企业清算明细新增user_fee_total user_fee_recharge user_fee_balance_transfer
    - 企业交易明细接口去除 fee 和 user_fee 字段,新增method、order_no、transaction_no source_url字段,查询列表新增 method order_no transaction_no asset_account 参数
    - 订单创建uid改为选填 order创建新增receipt_app、service_app、royalty_users字段.返回对象新增available_methods receipt_app service_app
    - user对象新增type,related_app,settle_accounts字段.查询user对象列表新增type查询参数.

# 2.1.0
- 增加:
    - 企业付款SDK更新接口
    - 请求认证接口接口
    - 报关接口接口
    - 批量退款接口
    - 订单创建更新查询删除支付接口
    - 用户充值接口接口
    - 企业清算账户交易明细接口
    - 用户接口
    - 余额转账接口
    - 优惠券及优惠券模板接口
    - 企业清算账户额度统计,批量提现确认创建查询接口
- 修改
    - 请求签名方法更新
    - 完善Demo示例

# 2.0.12
- 增加：
    - customs 报关接口

# 2.0.11
- 修复：
    - python2 报错信息无法解析的问题

# 2.0.10
- 增加：
    - 添加设置私钥内容方式
- 修复：
    - python3 不兼容问题

# 2.0.9
- 修复：
    - python3 不兼容问题

# 2.0.8
- 更改：
    - 增加请求签名

# 2.0.7
- 更改：
    - wxpub auth 获取 code 时的参数固定顺序

# 2.0.6
- 更改：
    - wxpub auth 获取 code 时的 bug

# 2.0.5
- 增加：
    - 增加微信企业付款

# 2.0.4
- 更改：
    - 更改在 python3.4 中 pip install 出错的问题

# 2.0.3
- 增加：
    - 新增 event 查询，新增京东手机网页支付

# 2.0.1
- 增加：
    - 新增微信红包

# 2.0.0
- 更改：
    - 添加新渠道：百付宝、百付宝WAP、微信公众号支付
