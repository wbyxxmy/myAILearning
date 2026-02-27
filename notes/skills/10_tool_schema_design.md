# Skill/Tool 教程 10：工具的 schema 怎么设计才不乱？

工具（Tool/Skill）一旦进入工程化，就要像 API 一样“可依赖”。最重要的是：输入输出结构固定，错误可解释。

## 1. 为什么一定要 schema
没有 schema，模型会：
- 乱填字段
- 字段类型不一致（数字/字符串混用）
- 成功/失败格式混乱，后续步骤无法自动处理

因此建议你为每个工具规定：
- 输入字段（必填/可选）
- 输出字段（成功/失败）
- 错误码与错误信息

## 2. 成功响应建议包含哪些字段
最小集合：
- `ok: true`
- `data: ...`（结构化）
- `meta: ...`（可选，比如耗时、请求 id）

## 3. 失败响应建议包含哪些字段
最小集合：
- `ok: false`
- `error_code: ...`（可枚举）
- `message: ...`（人类可读）
- `retryable: true/false`（是否可重试）

## 4. 幂等性与权限（写入类工具必须考虑）
写入类工具（例如“提交代码”“创建工单”）建议：
- 设计幂等键（同一个请求重复执行不会产生重复副作用）
- 记录审计信息（谁在什么时候做了什么）
- 做权限控制与人工确认（尤其生产环境）

## 5. 与本仓库 demo 的连接点
你可以把 `ingest.py` / `query.py` 视作两个“本地工具”：
- `build_index(docs_dir, out_dir)`
- `search(query, index_dir, top_k)`

当你后续接入 Agent 框架时，就把这两个脚本封装成真正的 Tool 即可。

---

## 📌 导航
- 上一章：[Skill/Tool 教程 00：为什么 Agent 需要工具](./00_overview.md)
- 下一章：[Skill/Tool 教程 20：安全、权限、幂等与审计](./20_safety_permissions_idempotency.md)
- 返回总览：[根目录学习导航](../../README.md#-专题学习导航prompt--rag--skill)
