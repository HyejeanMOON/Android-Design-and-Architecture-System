# Google Play 与 target 适配

仅用于发布准备、政策警告、相关受限能力或 targetSdk 升级。产物技术检查由 [testing-release.md](testing-release.md) 负责，不再另起重复流程。

## 核对当前要求

按预计提交日期查询当前政策和可访问 Console，记录来源、核对／生效／截止日期及适用范围。区分设备类别、首次提交／更新／既有分发、轨道、地区和账号资格，确认实际 SDK／原生库／第三方 SDK 及使用能力。新提交门槛不等于已有应用分发门槛，Android Auto 不等于 Automotive OS。

本技能不固定 target API、Billing 或测试人数／天数等门槛；从 [target 官方要求](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en)、[账号测试资格](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)及对应页面核实。延期需应用实际资格／批准证据，不默认获得。来源冲突先核对时间和范围，不取最宽松值宣称合规。

未知项标待核实并继续独立本地工作；缺少 Console 证据不算已满足，也不自动认定违规。历史记录和博客只供追溯，不作为执行门槛。

## 系统与产物

- 分清 minSdk 安装范围、compileSdk 编译 API、targetSdk 行为目标；只改数字、提高 minSdk 排除旧用户不能代替适配。
- 检查升级跨度内相关版本的 all-app／target-specific 变化，映射实际使用的权限、后台／前台服务、闹钟、存储、组件／PendingIntent、导航、窗口／IME、返回及大屏行为。写清适用原因，不为未使用能力增加功能。
- 工具链／依赖只升级到必要兼容组合；临时 opt-out 必须仍受官方支持并记录范围／后续处理，不降低 target 或关检查绕过要求。代表旧系统、新目标系统和覆盖升级路径验证相关行为。
- 最终包连同传递 SDK 检查适用 ABI／64 位／原生 `.so`、[16 KB ELF／打包及运行兼容](https://developer.android.com/guide/practices/page-sizes)。业务 Kotlin 不代表无原生依赖；全部依赖均为 Kotlin／Java 时不无需求引入 NDK。改打包属性或隐藏警告不足以证明兼容。
- SDK 风险／到期按当前来源查；实际使用 Billing 时核对 [淘汰时间表](https://developer.android.com/google/play/billing/deprecation-faq)。是否须用 Play Billing 另按商品、地区和适用计划确认。

## Console 与政策材料

| 条件 | 核对内容 |
| --- | --- |
| 商店／App content | 真实功能、截图、广告、受众与分级，不虚构资质 |
| Data safety／隐私 | App／SDK 与服务端真实收集、共享、用途和删除；轨道豁免不推广，不采集不等于自动免申报 |
| 在线账号创建 | 适用时有应用内删除请求及应用外网页资源、关联数据处理；登出／停用不是删除 |
| 受限访问 | 可用审核访问方式、环境和说明，不伪造 URL／凭据 |
| 敏感／特殊类别 | 按实际权限、儿童、健康、金融、UGC、广告或订阅触发资格、披露及声明，不强加全部类别 |
| 账号／测试 | 实际开发者验证、地区、轨道、测试与 production access；源码不能证明资格，达到测试条件不等于自动批准 |

拒审保留脱敏原因、版本／轨道、来源和期限，区分代码、SDK、产物、申报、账号或后端问题后最小修复，不隐瞒权限或虚假申报。申诉、上传、送审与 rollout 按已有授权执行。

交付一份与版本对应的适用矩阵：要求／日期、来源、影响、状态、证据和剩余阻塞；可区分已验证、待验证、待信息、不适用及明确阻塞，本地通过不保证审核批准。

依据：[target 迁移](https://developer.android.com/google/play/requirements/target-sdk)、[审核准备](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en)、[Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)、[账号删除](https://support.google.com/googleplay/android-developer/answer/13327111)。
