# 01 - AI工具概览

> 了解主流AI编程工具，选择最适合你的工具

## 🧭 关联专题跳转

- Prompt基础： [Prompt 教程 00](../notes/prompt/00_overview.md)
- RAG概览： [RAG 教程 00](../notes/rag/00_overview.md)
- Skill/Tool概览： [Skill/Tool 教程 00](../notes/skills/00_overview.md)
- 动手实践： [离线 RAG 最小 Demo](../demos/rag_min/README.md)

## 📋 目录

1. [Cursor - AI原生代码编辑器](#cursor)
2. [GitHub Copilot - 智能代码助手](#github-copilot)
3. [Claude & ChatGPT - 通用AI助手](#claude--chatgpt)
4. [工具对比与选择](#工具对比与选择)

---

## Cursor

### 🎯 定位
Cursor是一个**AI原生**的代码编辑器，基于VS Code构建，深度集成AI能力。

### ✨ 核心特性

#### 1. AI编辑器集成
- **Ctrl+K**: 行内AI命令，直接编辑选中代码
- **Ctrl+L**: AI对话面板，讨论代码问题
- **Tab补全**: 类似Copilot的智能补全
- **代码理解**: AI可以阅读整个项目上下文

#### 2. 独特优势
- **Codebase问答**: "这个项目的认证是怎么实现的？"
- **多文件编辑**: AI可以同时修改多个文件
- **终端集成**: AI可以帮你生成和解释命令
- **错误修复**: 点击错误，AI自动建议修复方案

### 💰 价格
- 免费版：有限制的AI调用次数
- Pro版：$20/月，无限AI调用

### 🎓 适合人群
- 想要最完整的AI编程体验
- 愿意尝试新工具
- 需要AI理解整个项目上下文
- 独立开发者或小团队

### 📚 学习资源
- [Cursor官网](https://cursor.sh)
- [Cursor文档](https://docs.cursor.com)
- [Cursor教程视频](https://www.youtube.com/results?search_query=cursor+tutorial)

---

## GitHub Copilot

### 🎯 定位
GitHub Copilot是**代码补全助手**，专注于在你编写代码时提供智能建议。

### ✨ 核心特性

#### 1. 智能代码补全
```python
# 你输入注释
def calculate_fibonacci(n):
    # Copilot自动生成代码
```

#### 2. 多编辑器支持
- VS Code (最佳支持)
- JetBrains IDEs
- Neovim
- Visual Studio

#### 3. Copilot Chat
- 在编辑器中直接对话
- 解释代码
- 生成测试
- 修复bug

#### 4. Copilot CLI
```bash
# 在终端中使用
gh copilot suggest "列出所有大于1GB的文件"
```

### 💰 价格
- 个人版：$10/月 或 $100/年
- 商业版：$19/月（企业功能）
- 免费：学生、教师、开源维护者

### 🎓 适合人群
- 已经在使用VS Code或JetBrains
- 需要稳定可靠的AI助手
- 注重代码补全效率
- 企业环境（有企业版支持）

### 📚 学习资源
- [Copilot官网](https://github.com/features/copilot)
- [Copilot文档](https://docs.github.com/copilot)
- [Copilot最佳实践](https://github.blog/copilot)

---

## Claude & ChatGPT

### 🎯 定位
**通用AI助手**，不是专为编程设计，但在编程任务中表现出色。

### Claude (by Anthropic)

#### ✨ 核心特性
- **超长上下文**: 可以处理整个代码文件或多个文件
- **代码理解**: 优秀的代码阅读和解释能力
- **结构化输出**: 输出格式规范，易于复制使用
- **Artifacts**: 可以生成可交互的代码预览

#### 💡 最佳应用场景
- 架构设计讨论
- 代码审查和重构建议
- 学习新技术和框架
- 复杂问题的解决方案设计
- 生成文档和测试用例

#### 💰 价格
- 免费版：Claude.ai，有使用限制
- Pro版：$20/月
- API：按token计费

### ChatGPT (by OpenAI)

#### ✨ 核心特性
- **GPT-4**: 强大的代码生成能力
- **代码解释器**: 可以执行Python代码
- **插件生态**: 丰富的扩展功能
- **自定义GPTs**: 创建专门的编程助手

#### 💡 最佳应用场景
- 快速原型设计
- 算法实现
- 学习编程概念
- 代码转换（如Python转JavaScript）
- 生成正则表达式和SQL查询

#### 💰 价格
- 免费版：GPT-3.5
- Plus版：$20/月（GPT-4访问）
- API：按token计费

### 🎓 适合人群
- 需要讨论复杂问题
- 学习新技术
- 不想安装额外工具
- 需要多领域AI助手（不只编程）

### 📚 学习资源
- [Claude官网](https://claude.ai)
- [ChatGPT官网](https://chat.openai.com)
- [Prompt工程指南](https://www.promptingguide.ai)

---

## 工具对比与选择

### 📊 功能对比表

| 特性 | Cursor | GitHub Copilot | Claude | ChatGPT |
|------|--------|----------------|--------|---------|
| **代码补全** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ |
| **项目理解** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **多文件编辑** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ |
| **编辑器集成** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ |
| **对话能力** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **上下文长度** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **学习成本** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **价格** | $20/月 | $10/月 | $20/月 | $20/月 |

### 🎯 选择建议

#### 场景1: 日常开发（选一个主力工具）
```
推荐组合：Cursor 或 GitHub Copilot
理由：深度集成，高效补全，workflow流畅
```

#### 场景2: 学习新技术
```
推荐组合：Claude 或 ChatGPT
理由：擅长解释概念，提供学习路径
```

#### 场景3: 架构设计
```
推荐组合：Claude + Cursor
理由：Claude讨论设计，Cursor实现代码
```

#### 场景4: 预算有限
```
推荐组合：GitHub Copilot ($10) + Claude免费版
理由：性价比最高，覆盖核心需求
```

#### 场景5: 追求极致
```
推荐组合：Cursor + Claude/ChatGPT + Copilot
理由：各取所长，覆盖所有场景
```

### 💡 我的推荐

#### 完全新手
**第一步**: 试用GitHub Copilot（学习成本最低）
**第二步**: 配合ChatGPT/Claude学习（免费版即可）
**第三步**: 根据需求考虑Cursor

#### 中级开发者
**主力**: Cursor（全能型）
**辅助**: Claude（架构讨论）

#### 高级开发者/团队
**主力**: GitHub Copilot（企业支持好）
**辅助**: Claude API（自动化workflow）

### 📈 投资回报率(ROI)

```
工具成本: $10-20/月
时间节省: 每天1-2小时
效率提升: 30-50%
学习周期: 1-2周

投资回报: 一周就能回本！
```

### ⚠️ 常见误区

#### 误区1: "我应该学会所有工具"
❌ 错误：分散精力  
✅ 正确：精通1-2个，了解其他

#### 误区2: "AI会替代我"
❌ 错误：恐惧AI  
✅ 正确：AI是助手，你是主导

#### 误区3: "免费工具足够了"
❌ 错误：节省小钱  
✅ 正确：付费工具ROI极高

#### 误区4: "AI生成的代码直接用"
❌ 错误：盲目信任  
✅ 正确：理解并审查所有代码

---

## 🎬 下一步

选好工具了吗？让我们开始实践！

👉 [进入入门指南](../02-入门指南/README.md)

学习如何安装、配置和使用这些工具。

---

## 💬 讨论

有问题或想分享你的工具使用经验？欢迎提Issue讨论！
