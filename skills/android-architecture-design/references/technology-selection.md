# 技术选型与依赖维护

## 缺省选择

用户明确要求 → 项目已有且仍适用的方案 → 适用的 Google／AndroidX 推荐方案 → 成熟且维护中的第三方库。官方示例采用某库不等于正式强制推荐；下表不是整套必装清单。

| 能力 | 默认候选和边界 |
| --- | --- |
| 语言／异步 | 新代码 Kotlin、coroutines／Flow；保留 Java 互操作 |
| UI／状态 | 按 UI 技术选择 Compose Material 3／XML Material Components、Lifecycle／ViewModel |
| REST／HTTP | Retrofit + OkHttp；原始 HTTP／下载可仅用 OkHttp，非 REST 协议另评估 |
| JSON | 新 Kotlin 项目优先考虑 kotlinx.serialization；已有适用 Moshi／Gson 保留，按契约和 converter 选主要方案 |
| 存储 | Room 用于结构化查询／事务，DataStore 用于小型设置；不无故迁移已有方案，不等同加密凭据库 |
| DI | 确需框架时优先 Hilt；小图可手工注入，已有适用 Koin／Dagger 保留 |
| 后台／分页 | 持久可延期任务考虑 WorkManager；大数据分页考虑 Paging，只按需求引入 |
| 图片 | 新 Compose 优先考虑 Coil；XML 复用已有 Glide／Coil，按需网络与 decoder |
| 导航／测试 | 复用匹配现有 UI 的 AndroidX／既有测试方案，不自动迁移框架 |

第三方默认是插件偏好。引入说明需求、已有能力为何不足、维护方、许可证与兼容性即可，不每个库新建 ADR。使用已有版本目录／集中管理及适用 BOM，不用动态版本或重复管理体系。

网络配置封装在 data 边界；复用适当作用域客户端／loader，不强制不同安全边界共享实例。不对所有库包一层万能接口。

## 升级与废弃 API

升级、已知风险、政策期限或当前任务被旧 API 阻塞时才启动维护，不因启用技能扫描并升级整个仓库。

1. 记录当前版本与直接／传递依赖；核对维护方发布说明、迁移说明、已知风险和相关官方兼容表。没有信息时标注未核实，不编造最新稳定版本或漏洞结论。
2. 确认受影响的 AGP／Gradle／JDK、Kotlin／Compose compiler／KSP、SDK／NDK 及相关库组合；这些是调查项，不代表每次全升级。遵守目标版本实际机制，不照抄旧插件配置。
3. 选择解决需求或风险的最小可维护组合；不盲目长期钉死旧版本，也不自动追新。必要且已授权的兼容调整可完成；可选大迁移提出建议，不扩大范围。
4. 检查废弃 API 的替代是否满足旧系统和现有行为，保留必要兼容分支；不要只消除警告却改变语义。验证编译／lint、关键行为、适用 release 与迁移；更新实际锁定／目录，不硬 force 传递版本隐藏冲突。
5. 记录破坏性变化、回退条件与剩余问题。涉及持久格式时按 [data-migrations.md](data-migrations.md) 处理，回退依赖不等于可回退用户数据。

依据：[升级策略](https://developer.android.com/build/version-upgrade-strategies)、[AGP](https://developer.android.com/build/releases/about-agp)、[Hilt](https://developer.android.com/training/dependency-injection/hilt-android)、[Data 层](https://developer.android.com/topic/architecture/data-layer)、[Retrofit](https://github.com/lysine-dev/retrofit)、[OkHttp](https://github.com/lysine-dev/okhttp)、[serialization](https://kotlinlang.org/docs/serialization.html)、[Coil](https://coil-kt.github.io/coil/)。
