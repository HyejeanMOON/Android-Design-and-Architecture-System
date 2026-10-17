---
name: android-architecture-design
description: 为原生 Android 开发、UIUX、Review 与发布准备提供架构和质量约束，适用于老旧 XML／Compose 混用项目；默认 XML MVVM、独立 Compose 屏幕轻量 MVI、Clean 边界与 Material 3。不用于 Flutter、Web 或插件自身维护。
---

# Android Architecture & Design

按 [公共流程](references/workflow.md) 确定任务范围、规则优先级、验证与交付。先读实际项目，不把默认规范变成旧项目全量迁移要求；用中文解释修改及原因。

新增／授权调整默认采用 XML MVVM、独立 Compose 屏幕轻量 MVI、Clean 职责边界和 Material 3；复用现有适用方案，缺省选官方推荐或成熟库。UseCase、多模块、通用框架、离线同步和监控均按真实需求引入。

代码写完后与已授权提交前，按 [Review](references/code-review.md) 校对和审查；内容未变可复用有效测试证据。不得编造业务、版本、验证或发布资格，不因本技能擅自提交／发布。

## 按触及范围读取

链接用于定位，不要求递归加载。只选择本次直接相关项；小修改不做全仓审计，不生成成套报告。

| 任务 | 参考 |
| --- | --- |
| 旧项目／混用／渐进迁移 | [legacy-hybrid.md](references/legacy-hybrid.md) |
| 分层／模块／选型升级 | [架构](references/architecture.md)、[模块](references/modularization.md)、[选型](references/technology-selection.md) |
| XML／Compose／UIUX | [XML](references/xml-mvvm.md)、[Compose](references/compose-mvi.md)、[Material 3](references/material3-uiux.md) |
| 并发弱网／迁移／后台 | [数据](references/data-consistency.md)、[迁移](references/data-migrations.md)、[后台](references/background-work.md) |
| 性能诊断／构建／安全 | [运行](references/runtime-performance.md)、[Gradle](references/build-performance.md)、[安全](references/security-privacy.md) |
| release／Play 适配 | [产物验证](references/testing-release.md)、[Play](references/google-play-release.md) |

新 API、版本、平台行为及政策以适用官方来源核对，见 [sources.md](references/sources.md)；无法确认则说明限制。
