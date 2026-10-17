# Compose：轻量 MVI

独立新屏幕默认 Action → ViewModel → [UseCase] → Repository → immutable UiState → Screen；无需额外 Store 框架。旧 Compose MVVM 和 XML 内嵌组件按 [legacy-hybrid.md](legacy-hybrid.md)，不自动迁移或另造状态层。

- ViewModel 暴露只读 StateFlow 和动作入口；页面按需定义 UiState／sealed Action，Action 不是 android.content.Intent。复杂转换可提取纯 reducer，简单转换不强制单独文件。
- Route 获取状态拥有者、按版本感知生命周期收集并连接导航；复用 Screen／组件接收状态和回调，不依赖 Repository／NavController／ViewModel。
- Composable 函数体不执行业务 IO 或重复派发加载。Effect 的 key、取消和清理匹配真实语义；关键结果及导航按 [architecture.md](architecture.md) 管理，不默认 Effect 总线。
- 局部可丢弃状态用 remember，适合恢复的输入用 rememberSaveable；业务状态归 ViewModel，不镜像两份 UiState。集合不能外部原地变更，稳定性注解不能掩盖可变性。
- 列表使用真实身份 key，按需 contentType；优化需热点依据，不批量添加 remember／derivedStateOf／@Stable。M3 及主题默认仅适用于新增／授权迁移区域。

验证相关动作转换、重组无重复工作、错误／取消及重返行为。依据：[Compose 架构](https://developer.android.com/develop/ui/compose/architecture)、[UI 事件](https://developer.android.com/topic/architecture/ui-layer/events)。MVI、Route／Screen 划分为插件约定。
