# Android Architecture & Design

Codex 桌面端的 Android 架构、UIUX、Review 与发布准备技能包，版本 **0.6.1**。只提供规则与评测资源，不包含 App、MCP 服务或自动发布功能。

## 默认与范围

新增／授权调整区域默认 XML MVVM、独立 Compose 屏幕轻量 MVI、Clean 边界与 Material 3；优先已有适用方案，无特定要求时选择官方推荐或 Retrofit／OkHttp 等成熟库。UseCase、多模块、离线同步和框架按需引入，不因模式完整而生成。

[技能入口](skills/android-architecture-design/SKILL.md)只定义公共边界和任务索引；[公共流程](skills/android-architecture-design/references/workflow.md)统一需求、冲突、验证与交付；[Review](skills/android-architecture-design/references/code-review.md)统一写完后及提交前检查。其他专项仅按触及范围加载，不递归读全套。

| 任务 | 专项 |
| --- | --- |
| 老旧／混用项目 | [渐进修改与互操作](skills/android-architecture-design/references/legacy-hybrid.md)：保留已有适用方案，按宿主与状态边界修改 |
| 架构／模块／选型升级 | [分层](skills/android-architecture-design/references/architecture.md)、[模块化](skills/android-architecture-design/references/modularization.md)、[选型与维护](skills/android-architecture-design/references/technology-selection.md) |
| UIUX | [XML](skills/android-architecture-design/references/xml-mvvm.md)、[Compose](skills/android-architecture-design/references/compose-mvi.md)、[Material 3](skills/android-architecture-design/references/material3-uiux.md) |
| 数据与生命周期 | [并发／弱网](skills/android-architecture-design/references/data-consistency.md)、[迁移](skills/android-architecture-design/references/data-migrations.md)、[后台](skills/android-architecture-design/references/background-work.md) |
| 性能与隐私 | [运行／诊断](skills/android-architecture-design/references/runtime-performance.md)、[Gradle](skills/android-architecture-design/references/build-performance.md)、[安全](skills/android-architecture-design/references/security-privacy.md) |
| 发布 | [release 验证](skills/android-architecture-design/references/testing-release.md)、[Play 适配](skills/android-architecture-design/references/google-play-release.md) |

用户明确要求和项目约定优先于插件默认；系统行为和适用发布要求不能靠偏好宣称通过。官方来源见 [索引](skills/android-architecture-design/references/sources.md)。Play 专项不固定版本门槛／截止日期，实际提交必须查询当前官方要求。

## 使用与包装

`plugin.json` 为 portable 入口，`.codex-plugin/plugin.json` 为兼容入口；两者共享一个技能目录。源码尚未在此对话中安装或发布。按宿主支持的本地导入方式选择根目录；没有导入入口时，可使用完整技能目录或明确让代理读取该 SKILL.md，不能把手动读规则称作已安装。

```text
使用 $android-architecture-design，在现有项目实现搜索页。
沿用当前依赖与导航，完成后校对和 Review，说明原因及实际验证。
```

```text
使用 $android-architecture-design，Review 本次变更的逻辑、typo、反模式、
Android 惯例、性能和泄漏风险。只报告有依据的问题，先不修改或提交。
```

```text
使用 $android-architecture-design，检查 Google Play 发布准备。
按预计提交日期核对政策、target 适配和实际产物，报告阻塞，不上传或送审。
```

## 验证与维护

```sh
python3 scripts/validate_plugin.py
python3 -m unittest discover -s tests -v
python3 scripts/run_regressions.py --help
```

另用 Codex skill-creator 的 `quick_validate.py` 校验技能。第一项只检查包结构／引用和可达性，第二项测试校验器行为；Kotlin 回归需本地 Kotlin/JDK，使用方法和实际覆盖见 [评测说明](evals/README.md)。Android 片段未构建成 App，不能把纯 Kotlin 或结构通过冒称 UI／泄漏运行通过，也不能冒称模型行为评测通过。

插件变更规则见 [维护说明](MAINTENANCE.md)，版本记录见 [CHANGELOG](CHANGELOG.md)。历史行为回归见 [0.5.0 记录](evals/results/0.5.0-local.md)，本轮精简与边界复查见 [0.6.1 记录](evals/results/0.6.1-local.md)。
