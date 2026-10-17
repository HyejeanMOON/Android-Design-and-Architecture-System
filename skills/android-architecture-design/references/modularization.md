# 合理模块化

按稳定业务能力、功能职责或团队边界划分，目标是高内聚、低耦合与明确所有权；团队与模块不必一一对应。不按固定行数、每屏／每类型或模块数量判合规。

| 信号 | 判断 |
| --- | --- |
| 值得拆 | 独立变更／测试、复用、所有权或构建隔离收益明确 |
| 过细 | 薄壳转发、少量类型孤立、频繁同步修改，配置／API 成本大于隔离收益 |
| 过大 | 无关业务绑在一起、团队冲突、测试难隔离，小改动扩散到大量无关构建 |

小项目用包边界即可；规模需要时考虑 app 装配、feature、业务 data／可选 domain 和少量共享 core。不是脚手架清单，不自动每 feature 拆 api／impl／presentation／domain／data。无 Android 需求的纯业务模块优先 Kotlin／Java。

- 编译依赖有向无环，Clean 边界见 [architecture.md](architecture.md)；app 装配，core 不反向依赖 feature。
- feature 不访问另一 feature 内部实现，通过稳定业务契约／导航回调协作；不以全局事件总线绕循环，不互改 ViewModel。
- 不造万能 common/core，不为省映射泄露 DTO。默认 implementation，公共契约确需暴露依赖才 api，用可见性保护实现。
- DI 生命周期与状态拥有者一致，不复制多份本应共享的数据／会话；也不强制独立安全边界共享实例。
- 模块多不保证快：评估高扇入改动、串行链与配置成本，构建收益要测量。

仅在模块任务中简述职责／所有者如已知、公开能力、直接依赖和关键运行数据流，区别编译图与运行调用。检查装配、资源、循环依赖、测试和影响范围；局部功能不自动触发全仓拆分。

依据：[模块指南](https://developer.android.com/topic/modularization)、[常见模式](https://developer.android.com/topic/modularization/patterns)。
