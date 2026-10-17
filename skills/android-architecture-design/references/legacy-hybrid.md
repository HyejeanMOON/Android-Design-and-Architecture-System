# 老旧 XML／Compose 混用

仅在触及旧实现、两套 UI 边界或迁移时读取。混用不是缺陷；只确认本次宿主、导航、状态拥有者、主题、数据入口和实际版本，不先做全仓盘点。

## 修改边界

- 修旧页面：沿用适用 UI、LiveData／Flow／Rx、DataBinding、DI 和导航；不为局部改动自动迁移。
- XML 内嵌 Compose：接收宿主状态／回调，不额外造 MVI／ViewModel。独立新 Compose 屏幕才按默认采用轻量 MVI 并接入既有导航，Fragment 仍可作宿主。
- 明确迁移：按业务切片替换，检查旧新契约和数据，不能连带迁移无关工具链、存储和模块。发布要求不因项目老旧而豁免。

## 互操作检查

- Fragment 内 ComposeView 的 composition 释放跟随 View 生命周期；按现有版本选择适用策略，例如 `DisposeOnViewTreeLifecycleDestroyed`。池化 RecyclerView／其他宿主策略不同，不能全局套用。多个 ComposeView 使用可恢复且独立的 ID。
- AndroidView／AndroidViewBinding 的创建、更新、复用、回调和资源释放按实际 API 管理；onReset／onRelease 等有版本条件，不为使用新回调强升工具链，不释放共享资源。
- 核对 Fragment／Activity／导航图／Compose 获取的 ViewModel 实例与作用域；同一业务状态不在两侧各造一份，跨页局部状态也不强行合并。桥接不形成双向更新环、重复订阅／请求或结果消费。
- 保留导航所有权及参数／返回结果；检查返回、深链、焦点／滚动／IME 与 insets 是否重复处理。重返、View 重建和恢复后不能保留旧 View／闭包或错误状态。
- Material 2／AppCompat 与 M3 可渐进共存；XML 主题不自动传给 Compose。新增／授权迁移区域优先 M3 并复用设计语义，不擅自全局换主题或制造局部割裂。

按变更选择进入／返回、旋转、View 重建、进程恢复及相关异常，保留旧用户数据；不以清数据／重装代替升级验证。Review 区分本次缺陷、历史风险与可选迁移建议，动态验证限制沿公共流程报告。

依据：[迁移策略](https://developer.android.com/develop/ui/compose/migrate/strategy)、[Compose in Views](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/compose-in-views)、[Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose)。
