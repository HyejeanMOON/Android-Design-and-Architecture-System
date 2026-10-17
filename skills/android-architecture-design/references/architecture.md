# 分层与状态

官方推荐 UI／Data、UDF，Domain 按需。本插件的 Clean 依赖倒置是默认约定，不是官方唯一布局；旧项目变化按公共流程限制。

```text
编译（有独立业务边界时）：presentation → domain ← data；app 装配
运行：UI → ViewModel → [UseCase] → Repository 契约 → 实现 → DataSource
状态：可信数据 → 屏幕状态 → UI；动作反向进入状态拥有者
```

- Domain 是纯 Kotlin 业务模型、必要契约和有价值的 UseCase，不依赖 UI、Context、Room Entity 或网络 DTO；可按契约用协程／Flow。
- Data 封装数据源和一致性，UI／ViewModel 不直接访问 DAO、HTTP、DataStore。仅语义确有差异时映射模型，不能把内部 DTO 当公共业务契约。
- Presentation 提供只读状态和业务动作；权限、窗口与导航执行归 UI。app 复用既有 DI 或手工装配。
- 小功能可在同模块以包／契约隔离，ViewModel 直接调 Repository，无需空壳 UseCase。既有官方分层布局不因目录不同被全量重构。
- 状态放合适拥有者：局部展开／焦点／动画不全进 ViewModel。订阅策略按成本选，恢复只保存适合的小输入／ID，持久业务数据另存；配置变化存活不代表进程死亡恢复。
- ViewModel 不保留 View、Activity、binding、NavController 或短命 Context。纯 UI 导航可回调；业务结果先成状态，由 UI 导航并定义返回／重返策略。
- 关键结果不只靠易丢失的 Channel／SharedFlow／SingleLiveEvent，暂态消息可用确认状态；不承诺天然 exactly once。

并发／后台／模块细节按入口触发读取。依据：[官方建议](https://developer.android.com/topic/architecture/recommendations)、[Domain](https://developer.android.com/topic/architecture/domain-layer)、[事件](https://developer.android.com/topic/architecture/ui-layer/events)、[保存状态](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)。
