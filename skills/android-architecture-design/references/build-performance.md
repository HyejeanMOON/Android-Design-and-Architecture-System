# Gradle 构建性能

仅优化目标 App 构建，不给插件仓库加 Gradle；运行时性能另查。先记录实际 Wrapper／AGP／Kotlin／JDK、相关插件和本地／CI 的 CPU、内存、容器限制。

用现有分析或本地 `--profile` 区分下载、配置、生成、编译和打包瓶颈；按需比较冷构建、无改动、局部实现／API 改动。variant、数据、缓存与机器条件可比，不默认清缓存。

| 候选 | 条件与验证 |
| --- | --- |
| `org.gradle.parallel=true` | 由一次 Gradle 调用调度独立模块；依赖仍会串行，不删边或多进程抢同一工作目录 |
| `org.gradle.workers.max` | 按有效 CPU／总内存调整，不固定高并行度；检查共享输出与资源争用 |
| `org.gradle.jvmargs`／`-Xmx` | 有 GC／OOM 证据且资源足够才增大，保留其他参数；连同 Kotlin Daemon、worker、IDE、模拟器预算，不统一强制某个堆大小 |
| `org.gradle.caching=true` | 验证可缓存任务输出真实 `FROM-CACHE`，不同于 `UP-TO-DATE` |
| `org.gradle.configuration-cache=true` | Wrapper／AGP／相关插件兼容后试用，确认配置实际复用；不忽略问题装作通过 |
| 增量编译 | 保留适用默认机制，定位失效原因，验证局部改动；不堆积旧属性 |
| KSP／kapt | 新处理器兼容时优先 KSP，既有迁移单独评估；增量能力取决于实际处理器 |

自定义任务正确声明输入／输出／依赖，避免配置期 IO 与提前求值，不强标 cacheable。避免惯例 `clean`、`--rerun-tasks`、`--refresh-dependencies`，必要诊断除外；不使用废弃 `android.enableBuildCache` 或未经核实的试验标志，不关闭必要测试／lint 加速。

修改项目配置，不默认改用户全局配置；本地和 CI 分别考虑。远程缓存和上传 Build Scan 按已有外部操作授权处理。一次调少量因素，比较结果并验证产物／相关测试，退化则撤回相关调整；必要时干净构建排除残留依赖。未测只称待测配置，不声称提速。

依据：[Android](https://developer.android.com/build/optimize-your-build)、[Gradle](https://docs.gradle.org/current/userguide/performance.html)、[增量任务](https://docs.gradle.org/current/userguide/incremental_build.html)、[Kotlin](https://kotlinlang.org/docs/gradle-compilation-and-caches.html)。以目标版本为准。
