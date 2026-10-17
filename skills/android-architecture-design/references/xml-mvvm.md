# XML：MVVM

新增／授权调整的 XML 屏幕默认：View → ViewModel → [UseCase] → Repository，状态反向驱动渲染。既有和混用边界按 [legacy-hybrid.md](legacy-hybrid.md)，不自动改造。

- Activity／Fragment 做绑定、渲染、平台交互和导航；业务调用与状态归 ViewModel。XML 表达式、Adapter 和 UI 回调不实现业务规则。
- 新绑定优先 ViewBinding，已有 DataBinding／LiveData 可保留；新状态可用只读 StateFlow。不要为统一换掉适用方案或制造第二份业务状态。
- Fragment 观察跟随 viewLifecycleOwner；Flow 用适用的生命周期感知收集，多个长期 collect 分别启动，避免相互阻塞。binding 在 onDestroyView 释放，不放进 ViewModel。
- 状态表达实际加载、内容、空、错误和输入／提交，不强制每页所有状态或刷新清空内容。RecyclerView 正确处理 diff、身份和失效 position。
- XML 的 M3 使用兼容 Material Components／Theme.Material3；Compose 库不能替代 XML 控件。既有主题和导航按混用规则保留。

检查相关交互及 View 重建后是否重复观察、泄漏或丢状态。依据：[架构建议](https://developer.android.com/topic/architecture/recommendations)、[Views Material](https://developer.android.com/develop/ui/views/theming/look-and-feel)。MVVM 命名与绑定偏好为插件约定。
