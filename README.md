# 从交易所批量提取代币到指定网络 - python - binance

这个repo通过binance提供的sdk实现了批量提取代币的功能。这样的话，钱包资金的来源是币安的热钱包。如果钱包之间没有转账，应该是查不到的。

# 快速开始
1. 复制文件并重命名 `cp addresses_example.json addresses.json`， `cp .env.sample .env`
2. 把两个文件的配置换成自己的。
3. 在 `withdraw_from_binance.py` 脚本里面，输入自己的input【提现金额，币的名称，目标链】。运行脚本 `python withdraw_from_binance.py`。

具体攻略可以看：[here](https://mirror.xyz/june023.eth/95W6kVB2bYmfsxusay13Jah_HNP6nBFZc5PnhKCGSRg)

其他相关链接：
- 如何批量撸空头 - Arbitrum Odyssey： [here](https://mirror.xyz/june023.eth/RK8m0Vwy7lZZYa6vyylms4eazr1WnzOE8uBgHBcpoC8)
- 如何批量生成以太坊钱包：[here](https://mirror.xyz/june023.eth/UdcUu0L-xLzsFIbaR_amRMfxlWSLN0jUTgjlTsLjOrM)


# 关于我
- Mirror链接： https://mirror.xyz/june023.eth
- Twitter链接：https://twitter.com/june023_eth
