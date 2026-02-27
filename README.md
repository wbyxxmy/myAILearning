# AI学习指南 - 面向开发者

> 从AI工具小白到高效AI辅助开发的完整学习路径

## 📚 学习路线图

这是一个为传统开发者量身打造的AI辅助开发学习指南，帮助你逐步掌握AI工具，提升开发效率。

### 学习阶段

```
第一阶段: AI工具认知 → 第二阶段: 上手实践 → 第三阶段: 深度应用 → 第四阶段: 工作流整合
    (1-2周)              (2-4周)              (4-8周)              (持续优化)
```

## 📖 目录结构

### [01 - AI工具概览](./01-AI工具概览/README.md)
了解主流AI编程工具的特点、优势和适用场景
- **Cursor**: 专为编程设计的AI编辑器
- **GitHub Copilot**: 代码补全和建议工具
- **Claude/ChatGPT**: 通用AI助手在编程中的应用
- **工具对比**: 各工具的优缺点和选择建议

### [02 - 入门指南](./02-入门指南/README.md)
快速上手AI编程工具
- 工具安装与配置
- 第一个AI辅助编程项目
- Prompt工程基础
- 常见问题与解决方案

### [03 - 进阶技能](./03-进阶技能/README.md)
提升AI辅助开发效率
- 高效代码生成技巧
- AI辅助代码审查
- AI辅助重构
- AI辅助调试

### [04 - 高级技巧](./04-高级技巧/README.md)
深度应用AI进行复杂开发
- 架构设计与AI
- 复杂问题拆解
- AI辅助测试策略
- 性能优化

### [05 - 工作流集成](./05-工作流集成/README.md)
将AI无缝融入日常开发
- 开发工作流优化
- 团队协作最佳实践
- 实战案例分析
- 效率提升度量

## 🧭 专题学习导航（Prompt → RAG → Skill）

如果你想按“可落地链路”系统学习，建议走这条路线：

### 第一步：Prompt（先把任务描述清楚）
- [00 - Prompt 是什么](./notes/prompt/00_overview.md)
- [10 - 常用 Prompt 模式](./notes/prompt/10_prompt_patterns.md)
- [20 - Prompt 评估方法](./notes/prompt/20_prompt_evaluation.md)

### 第二步：RAG（让回答有依据）
- [00 - RAG 概览](./notes/rag/00_overview.md)
- [10 - Chunking 设计](./notes/rag/10_chunking.md)
- [20 - 检索与重排](./notes/rag/20_retrieval_and_rerank.md)
- [30 - 引用与 Grounding](./notes/rag/30_citations_and_grounding.md)
- [40 - RAG 评测](./notes/rag/40_rag_evaluation.md)

### 第三步：Skill/Tool（让 Agent 真正可执行）
- [00 - Tool 与 RAG 如何配合](./notes/skills/00_overview.md)
- [10 - Tool Schema 设计](./notes/skills/10_tool_schema_design.md)
- [20 - 安全/权限/幂等/审计](./notes/skills/20_safety_permissions_idempotency.md)

### 动手实践（最小可跑 Demo）
- [离线 RAG 最小 Demo](./demos/rag_min/README.md)
- 建议顺序：先构建索引，再运行查询，最后运行离线评测

## 🎯 学习建议

### 对于完全新手
1. 从 **01-AI工具概览** 开始，了解各工具的定位
2. 选择一个工具（推荐Cursor或Copilot）
3. 按照 **02-入门指南** 完成第一个项目
4. 逐步学习进阶和高级技巧

### 对于有一定了解的开发者
1. 快速浏览 **01-AI工具概览** 补充知识盲点
2. 直接进入 **03-进阶技能** 或 **04-高级技巧**
3. 重点学习 **05-工作流集成** 提升团队效率

### 对于想提升效率的团队
1. 重点关注 **05-工作流集成**
2. 学习团队协作最佳实践
3. 建立适合自己团队的AI开发规范

## 💡 核心理念

### AI工具不是替代，而是增强
- AI帮你写重复代码，你专注于架构和业务逻辑
- AI提供建议，你做最终决策
- AI加速迭代，你把控质量

### 渐进式学习
- 不要试图一次性学会所有工具
- 在实际项目中逐步应用
- 持续优化你的AI工作流

### 保持批判性思维
- AI生成的代码需要审查
- 理解代码比生成代码更重要
- 安全性和质量不能妥协

## 🚀 快速开始

### 5分钟体验
1. 安装 [Cursor](https://cursor.sh) 或启用 [GitHub Copilot](https://github.com/features/copilot)
2. 打开一个简单项目
3. 尝试用自然语言描述你想要的功能
4. 看AI如何帮你生成代码

### 第一周目标
- [ ] 完成至少一个AI工具的安装和配置
- [ ] 使用AI工具完成一个小功能
- [ ] 理解AI工具的基本工作原理
- [ ] 学会编写有效的提示词(Prompt)

### 第一个月目标
- [ ] 熟练使用1-2个AI工具
- [ ] 在日常开发中使用AI提升效率30%+
- [ ] 掌握代码生成、重构、调试的AI辅助技巧
- [ ] 建立自己的AI辅助开发工作流

## 📚 推荐资源

### 工具官方文档
- [Cursor Documentation](https://docs.cursor.com)
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [Claude Documentation](https://docs.anthropic.com)

### 社区资源
- GitHub上的AI辅助开发实践案例
- 各大技术社区的AI编程讨论
- YouTube上的实战教程

## 🤝 贡献指南

欢迎贡献你的学习笔记、实践经验和案例！

1. Fork 本仓库
2. 创建你的特性分支
3. 提交你的更改
4. 发起 Pull Request

## 📝 更新日志

- 2024-02: 创建完整的学习目录结构
- 2026-02: 补充 Prompt / RAG / Skill 专题教程与离线 RAG 最小 Demo
- 持续更新中...

## ⚖️ 许可证

MIT License - 自由使用和分享

---

**开始你的AI辅助开发之旅吧！** 🚀
