# Material 3 UIUX

先明确页面任务、信息层级、主要操作、返回和相关异常，再选组件。仅覆盖本次需求；预览假数据明确标识，不添加虚构业务入口。

## 组件与主题

新增／授权迁移区域优先标准 M3 与既有设计系统；XML 用兼容 Material Components，Compose 用 M3。旧主题共存按 [legacy-hybrid.md](legacy-hybrid.md)，不全局强换。语义色与 on-color、字体／形状／间距沿既有资源／token，不把所有点击对象都做 Card。

检查产品支持的浅深色；动态色按平台／品牌需要启用并有静态回退。品牌定制允许，实验 API／Expressive 全面改版不默认引入。

状态按场景表达初始加载、刷新、空、错误、校验、权限、提交与完成；可并存，刷新失败不必清内容，不强制每页所有状态。

## 无障碍与适配

- 交互目标通常至少 48dp × 48dp，图标视觉和触摸范围分开，不相互重叠。正文对比度目标 4.5:1，大字 3:1，按实际前景背景／透明度核对，不能凭 token 名称保证通过。
- 有意义图标有名称，装饰图标不重复朗读；自定义控件补语义、角色、状态和操作，检查阅读顺序／焦点。contentDescription 不等于无障碍完成。
- 支持字体缩放、长文案、资源化、数量／格式与 RTL，不固定高度裁字或拼接翻译句子。错误提供可操作恢复，不只错误码。
- 以可用窗口空间选择布局和适用导航／多栏，保持已有目的地；检查相关旋转、多窗口、折叠与阅读宽度，不按设备型号硬判。
- 系统栏／缺口／IME insets 只在正确边界处理，避免重复 padding；返回／edge-to-edge 按目标系统核对，不降低 target 逃避适配。动效有语义并尊重系统设置。

按影响检查浅深色、大字、相关窗口和异常状态及关键流程 TalkBack／键盘；不能渲染时说明未验证，不宣称全面符合规范。

依据：[M3](https://m3.material.io/foundations)、[Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)、[Views](https://developer.android.com/develop/ui/views/theming/look-and-feel)、[无障碍](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)、[自适应](https://developer.android.com/develop/ui/compose/layouts/adaptive)。
