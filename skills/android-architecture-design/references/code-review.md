# 校对与 Review

只审本次变更和理解它所需的上下文，领域参考按实际问题加载，不扩展为全仓整改。

## 两个时点

- **写完后**：重新读实际变更，对照验收和契约，检查下表，运行适用验证。实现任务修复授权范围的问题后复查；只读审查仅报告发现／阻塞，不擅自修改。
- **已授权提交前**：核对仓库／分支／基线、真实 staged diff、新增／删除及用户原有改动；push／PR 核对最终提交范围。后续编辑、冲突解决或 rebase 改变内容时复查相关部分，未变化的有效测试不重跑。

未授权不自动提交／推送／装 hook，未到提交阶段或 Git 不可用不能冒称审过 staged diff。实现范围内的重大问题先修或如实披露，不能删测试、扩大 suppress 或关闭检查后称通过。

| 类别 | 校对与风险 |
| --- | --- |
| Typo | 命名、文案、资源、注释、测试和复制遗留；已上线字段／存储键不能按英语偏好直接更名 |
| 逻辑 | 分支、边界、空值、单位／时间、错误路径、竞态、重复提交、取消、重试和恢复副作用 |
| Anti-pattern | UI 直连数据源、循环依赖、全局可变状态、万能 Base／Store、空壳抽象、吞异常、无需求迁移 |
| Android | 生命周期、scope、主线程、UDF、恢复、权限／返回及 API 兼容；架构名称差异不直接算缺陷 |
| 性能 | 主线程 IO／解码、重复请求、重组副作用、列表／图片成本、无界缓存及后台频率 |
| 泄漏／资源 | 长寿命对象持有短寿命 UI、绑定／监听／协程未清理，异常和取消路径遗漏释放 |
| 回归／安全 | 旧数据、外部契约、release／R8、敏感日志、外部输入和验收缺口 |

## 泄漏证据

追踪 ViewModel／DI／单例／静态字段／闭包到 View、binding 或短命 Context 的引用；检查 Fragment View 生命周期、Compose Effect／AndroidView 清理和回调更新。不是所有 Adapter 都必须置空，局部状态不天然泄漏。

观察者、receiver、Handler、定时器和协程应有正确所有者及撤销；Cursor、流、播放器、相机／传感器在异常与取消时也需释放。WeakReference、Application Context、强制 GC、largeHeap 不是通用补丁。

报告长期持有者 → 引用链 → 应释放对象和触发条件。内存上涨／缓存／暂未 GC 不足以证明泄漏；必要时用已有 Profiler／heap 或检测工具复现重返、旋转、重建，无设备则说明仅静态检查，不自动加 SDK。

## 结论

发现给出严重度、位置、触发、影响、证据和最小建议；偏好、疑点、已确认缺陷分开，不凑数量。只报告实际检查范围与限制，未发现明确问题不是无缺陷保证。自审、编译、lint、逻辑审查和动态验证分别表述。

依据：[Kotlin 风格](https://developer.android.com/kotlin/style-guide)、[生命周期](https://developer.android.com/topic/libraries/architecture/views/coroutines-views)、[内存](https://developer.android.com/topic/performance/memory/manage-app-memory)。两个时点为用户约定。
