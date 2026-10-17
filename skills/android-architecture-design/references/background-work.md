# 后台任务与进程生命周期

涉及离开页面后继续执行、上传／同步／定时或进程恢复时读取。后台线程与持久任务不是同一概念。

| 工作需要 | 优先考虑 |
| --- | --- |
| UI 可见期间订阅／动画 | UI／View 生命周期，离开后取消 |
| 屏幕业务请求、配置变化后保留 | ViewModel scope；进程结束不会自动恢复 |
| 应用存活期间跨屏工作 | 注入的应用级 scope，明确所有者、取消与错误处理；不默认 GlobalScope |
| 需持久调度的可延期工作 | WorkManager，明确约束、重试与业务身份 |
| 精确定时或用户可感知的持续工作 | 按当前官方指南评估 Alarm／前台服务／其他专用 API 及权限、配额、Play 资格；不把所有任务塞进 Worker |

WorkManager 支持持久调度，不保证准点、无限运行或每次恰好一次；系统配额、Doze、约束和 force-stop 都有影响。不能承诺强行停止后依然准时执行，也不能将划掉任务、系统杀进程和 force-stop 混为一谈。

- 用业务身份和适当 unique work／替换策略控制重复调度，命名按账号／租户隔离；KEEP／REPLACE 等按实际语义选择，不全局统一套用。
- Worker 不持有 View／Activity；参数保存小型 ID，载荷与进度按需持久化，避免依赖内存单例。重试／重启可能重入，写操作按契约幂等。
- 停止和取消需要协作处理并释放资源；退出账号时处理相应工作与凭据，不能让旧任务以新身份继续。
- 网络、充电等约束按需求设置；仅暂时错误重试并有退避，不对认证或校验失败无限 retry。实际结果通过 Repository 状态回到 UI，不用后台任务直接操纵界面。
- 验证重复入队、约束不满足／恢复、进程重建、取消和账号切换；涉及权限／系统限制时按目标 OS 核对。未运行的场景如实列出，不以无限前台服务规避系统限制。

依据：[后台任务选择](https://developer.android.com/develop/background-work/background-tasks)、[持久任务](https://developer.android.com/develop/background-work/background-tasks/persistent)、[管理工作](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/manage-work)。
