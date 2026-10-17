# 测试与 release 质量

公共执行／交付见 [workflow.md](workflow.md)，审查时点见 [code-review.md](code-review.md)；这里仅规定 release 与验证选择。

| 变更 | 相关证据 |
| --- | --- |
| 纯逻辑／状态 | 成功、失败、边界、取消／竞态；可控 fake 与调度，避免固定 sleep 和真实生产调用 |
| 数据／后台 | 映射、事务、迁移、重复工作、恢复和账号隔离 |
| UI／导航 | 关键任务、语义、输入、返回、状态恢复；预览辅助外观检查 |
| 系统／SDK | 代表低版本和目标版本，涉及的权限／窗口／后台行为 |
| release | 实际优化产物的反射／序列化、资源、深链、JNI 和 SDK；debug 成功不能替代 |

按风险选择代表场景，不要求所有修改跑整表或达到统一覆盖率。优先项目已有 Wrapper、variant、CI 与测试框架；失败区分回归、既有问题和环境限制，不删测试或反复重跑到偶然通过。

## 发布前

- 核对 applicationId、versionCode 序列、flavor、生产环境、合并 Manifest、debuggable、日志及调试入口。保持应用身份与既有签名，区分 upload key／app signing key；不把密钥写入仓库或输出。
- 保持适用 R8／资源压缩并验证关键路径；keep 规则最小化，不保留全部类或关闭压缩掩盖错误。mapping／原生符号与实际发布版本对应。
- 基于最终 AAB／生成安装产物检查 ABI、拆分资源及第三方原生库；使用旧版本覆盖升级验证数据库、会话和后台任务，不用卸载重装替代。
- Play 政策与资格见 [google-play-release.md](google-play-release.md)。轨道、上传、送审、rollout 按已有授权执行；不能把暂停 rollout 当数据库／APK 天然可降级。

报告实际版本／variant、命令、设备和结果／限制；产物、上传、审核及正式可用分别说明。发布后诊断复用已有渠道，见 [runtime-performance.md](runtime-performance.md)，不自动引入监控平台。

依据：[测试选择](https://developer.android.com/training/testing/fundamentals/what-to-test)、[R8](https://developer.android.com/build/shrink-code)、[签名](https://developer.android.com/studio/publish/app-signing)、[Bundle](https://developer.android.com/studio/publish/upload-bundle)。
