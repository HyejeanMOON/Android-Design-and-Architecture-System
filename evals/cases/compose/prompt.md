# 任务

Review input 中的 Compose 源码切片。产品要求每次进入该 Route 的 composition 时刷新一次，普通重组不应重复刷新；UI 的既有极简显示无需改版。只报告有依据的问题，不更换 UI／DI／导航框架，不因 BasicText 是底层组件就自动判为缺陷。没有执行 UI 测试时说明限制。

refresh 回调由装配端提供，它会触发真实请求；这里只展示接口以隔离后端。不要因未给出完整 Repository／网络实现虚构其他错误。
