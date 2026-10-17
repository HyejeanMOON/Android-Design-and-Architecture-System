# 运行时性能与故障诊断

只在性能／崩溃诊断任务或相关热点改动时使用；构建耗时见 [build-performance.md](build-performance.md)。

## 测量和优化

定义用户路径及指标：冷／温／热启动、首次可交互／完整显示、帧耗时、内存峰值、重复进入留存、耗电。记录设备／系统、variant、数据／网络、编译状态及重复次数；关键结论用接近生产的产物和真机复核，模拟器需说明限制。

按热点选择 Profiler／Trace／Perfetto／Macrobenchmark；细粒度计算再用 Microbenchmark。Baseline Profiles 需验证打包、生效和收益，不为小改动自动建 benchmark 模块。

| 热点 | 优先检查 |
| --- | --- |
| 启动／主线程 | Application／Provider／DI 初始化、同步 IO、解码、锁及重计算；按工作类型分派，不把所有工作丢到 IO 池 |
| Compose／Views | 状态读取范围、Effect key、列表身份、昂贵计算、重复绑定／布局；不批量加 remember、稳定性注解或更换控件 |
| 图片／列表 | 按显示尺寸解码、loader 复用、缓存容量与失效、按需分页；不无界缓存 |
| 内存／电量 | 生命周期持有链、资源释放、重复工作及后台频率；不强制 GC 或用永久轮询掩盖问题 |

缓存明确键、容量、失效和账号隔离。测量前后条件可比，报告波动与资源代价，不只选最快一次；没有实测只能称优化候选。泄漏证据规范见 [code-review.md](code-review.md)。

## 可观测性与诊断

优先现有日志、崩溃工具和 Android vitals，不自动接入监控 SDK 或持续监控。一次故障记录脱敏复现、应用版本／variant、系统设备、发生阶段和堆栈；混淆／JNI 堆栈使用同一发布版本的 mapping／符号。

错误上下文用稳定错误类别、操作名和必要的非敏感关联 ID，保留根因与异常链；日志不记录令牌、密码、完整响应或个人信息，不把用户 ID 直接当追踪标识。采样、限流、上传与保留期限按真实诊断需求和隐私约束设置，不每帧记录也不自动新增数据采集。

区分崩溃、ANR、取消、预期业务失败和系统杀进程。没有遥测数据不等于无问题，不同工具统计口径不能直接比较；先定位版本／设备与触发链，再做最小修复并验证。长期报警、rollout 和外部上传按已有授权执行，不凭诊断任务扩大操作范围。

依据：[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)、[Compose 性能](https://developer.android.com/develop/ui/compose/performance/bestpractices)、[Baseline Profiles 测量](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)、[Android vitals](https://developer.android.com/google/play/vitals)、[日志泄露风险](https://developer.android.com/privacy-and-security/risks/log-info-disclosure)。
