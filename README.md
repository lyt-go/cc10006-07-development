# 实时数据湖仓一体化平台

面向实时数据入湖、流批一体处理、湖仓分层存储、元数据统一管理、数据合并优化与增量查询服务的实时数据湖仓工程平台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 实时入湖 | `streaming` | 接入流 | 流编号、数据源类型、消费组名称 |
| 湖格式管理 | `lakeformat` | 表格式 | 格式编号、表名称、湖格式类型 |
| 数据合并 | `compaction` | 合并策略 | 策略编号、目标表名、触发文件数 |
| 统一元数据 | `catalog` | 目录条目 | 条目编号、目录层级、表名 |
| 快照管理 | `snapshotmgr` | 表快照 | 快照编号、所属表名、快照ID |
| 表优化 | `icebergopt` | 优化计划 | 计划编号、目标表名、优化类型 |
| Schema注册 | `schemareg` | Schema版本 | 版本编号、主题名称、Schema类型 |
| 增量查询 | `increment` | 增量视图 | 视图编号、基表名称、增量字段 |
| 文件布局 | `filelayout` | 布局策略 | 策略编号、表名、分区路径模式 |
| 冷热分层 | `coldstore` | 分层策略 | 策略编号、表名、热数据天 |
| 数据分支 | `databranch` | 分支定义 | 分支编号、分支名称、源分支名 |
| 检查点管理 | `checkpoint` | 检查点 | 检查点编号、关联流编号、检查点时间 |
| 分区水位 | `watershed` | 水位标记 | 标记编号、表名、分区键值 |
| 过期清理 | `gcpolicy` | 清理策略 | 策略编号、表名、快照保留数 |
| 索引加速 | `indexing` | 索引定义 | 索引编号、表名、索引列 |
| 标签标记 | `tagassign` | 表标签 | 标签编号、表名、标签名 |
| 访问日志 | `accesslog` | 访问记录 | 记录编号、表名、查询类型 |
| 故障恢复 | `failover` | 恢复方案 | 方案编号、关联任务、故障类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

领域：数据工程
子方向：数仓与数据湖
