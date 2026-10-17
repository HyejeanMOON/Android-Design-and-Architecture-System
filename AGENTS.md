# 本仓库的工作约定

- 修改完代码以后，解释修改的内容以及为何这样修改。
- 修改完成后按 `skills/android-architecture-design/references/code-review.md` 校对并自审；已获授权提交时在提交前再次核对最终内容。此仓库重点检查规则语义、typo、示例、引用、清单和兼容性，不虚构 Android 运行检查，也不因本规则自动执行 Git 提交或安装 hook。
- 本仓库是 Codex Android 架构与设计插件源码，不是 Android App；不要自行创建 Android 工程或添加 Gradle 工具链。
- Android 开发规则的唯一入口是 `skills/android-architecture-design/SKILL.md`，详细规则放在其 `references/` 中，避免在多个入口维护不一致的副本。
- 区分官方建议、用户选择和插件约定；不得将 XML MVVM、Compose MVI 或严格 Clean 分层声称为 Google 的唯一官方架构。
- 公共流程唯一来源是 `references/workflow.md`，专项只保留本领域约束。插件维护按 `MAINTENANCE.md`，不把作者维护／评测流程加载成 Android 用户每次任务的要求。
- 修改插件后运行技能结构校验和本仓库 `scripts/validate_plugin.py`；脚本改动运行 `tests`，样例逻辑改动运行对应回归。这些检查不能证明 Android 设备行为或模型行为正确。
