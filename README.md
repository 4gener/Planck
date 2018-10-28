# Planck
ymh说的都队 @BitRunHackathon 20181026-Shanghai



### 项目介绍

本次活动我们选择了由 BitMart 提供的题目：用 Bancor 协议开发一个分布式交易中心。开发初期项目使用链外模拟后端，最大程度上复原了链上账户间交易/转账的流程。在踩完 Bancor 协议的坑之后，我们在链上重新实现了它的相关操作。最终实现了我们的交易平台 Planck ，通过发行的 YMHC 作为智能货币，保证了多币种之间的流通性。



### 项目特色

- 使用多个连接器实现币种流通
- 币种价格实时计算，最大程度复原真实币市
- 为自定义发币功能提供了后续开发的接口（时间来不及）



### 项目合约

- [Adaptor.sol](https://github.com/igululu/Planck/blob/master/contract/Adaptor.sol)

  使智能合约网络上的连接代币互相转化，提高货币流通性。

- [YMHC.sol](https://github.com/igululu/Planck/blob/master/contract/YMHC.sol)

  发币合约，为连接器编写更新了 `nbTransfer` 等方法。

- [aETHConnector.sol](https://github.com/igululu/Planck/blob/master/contract/aETHConnector.sol)

  [vETHConnector.sol](https://github.com/igululu/Planck/blob/master/contract/vETHConnector.sol)

  连接器合约，跨合约调用了 `nbTransfer` 方法等




### 致谢

感谢 @sunrye 的详细指导



### Front End Repo

https://github.com/minghuiyang1998/kyber-network