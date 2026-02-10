# 02 - 入门指南

> 快速上手AI编程工具，开启高效开发之旅

## 📋 目录

1. [工具安装与配置](#工具安装与配置)
2. [第一个AI辅助项目](#第一个ai辅助项目)
3. [Prompt工程基础](#prompt工程基础)
4. [常见问题与解决方案](#常见问题与解决方案)

---

## 工具安装与配置

### Cursor 安装

#### 步骤1: 下载安装
```bash
# 访问官网下载
https://cursor.sh

# 或使用包管理器 (macOS)
brew install --cask cursor

# Windows: 下载.exe安装包
# Linux: 下载AppImage
```

#### 步骤2: 导入VS Code设置
Cursor首次启动会提示导入VS Code的配置：
- ✅ 导入扩展
- ✅ 导入快捷键
- ✅ 导入主题和设置

#### 步骤3: 配置AI模型
1. 点击右上角设置图标
2. 选择 "Cursor Settings"
3. 在 "Models" 选项中配置：
   - GPT-4（推荐，最智能）
   - GPT-3.5（速度快）
   - Claude（长文本好）

#### 步骤4: 常用快捷键
```
Ctrl/Cmd + K    # 行内AI编辑
Ctrl/Cmd + L    # 打开AI对话
Tab             # 接受AI建议
Esc             # 拒绝AI建议
```

### GitHub Copilot 安装

#### 步骤1: 获取订阅
```bash
# 访问GitHub Copilot页面
https://github.com/features/copilot

# 学生/教师免费申请
https://education.github.com/
```

#### 步骤2: 安装扩展

**VS Code:**
1. 打开扩展市场（Ctrl+Shift+X）
2. 搜索 "GitHub Copilot"
3. 安装并重启

**JetBrains:**
1. File → Settings → Plugins
2. 搜索 "GitHub Copilot"
3. 安装并重启

#### 步骤3: 登录授权
1. 点击右下角Copilot图标
2. 选择 "Sign in to GitHub"
3. 浏览器完成授权

#### 步骤4: 验证安装
创建一个新文件，输入注释：
```python
# 写一个快速排序函数
```
等待Copilot的建议出现（灰色文本）

### Claude/ChatGPT 设置

#### Claude
```bash
# 访问Claude官网
https://claude.ai

# 注册账号（免费）
# 升级Pro（可选，$20/月）
```

#### ChatGPT
```bash
# 访问OpenAI官网
https://chat.openai.com

# 注册账号
# 升级Plus（可选，$20/月，使用GPT-4）
```

#### 浏览器插件（可选）
- ChatGPT/Claude侧边栏插件
- 快速访问AI助手
- 选中代码直接提问

---

## 第一个AI辅助项目

### 🎯 目标
使用AI工具从零构建一个 **待办事项Web应用**

### 项目规划（5个步骤）

#### 步骤1: 项目初始化（使用AI）

**Cursor示例:**
```
Ctrl+L 打开对话，输入：
"帮我创建一个React + TypeScript + Vite的待办事项应用项目结构"
```

**Copilot示例:**
```javascript
// 在新文件package.json中输入
// 创建一个React TypeScript项目配置
// Copilot会自动补全
```

**Claude/ChatGPT示例:**
```
提示词：
"我想创建一个待办事项Web应用，使用React和TypeScript。
请帮我：
1. 规划项目结构
2. 列出需要安装的依赖
3. 提供初始化命令"
```

#### 步骤2: 创建组件（AI生成）

**使用Cursor:**
```typescript
// 在 TodoList.tsx 中按 Ctrl+K
// 输入: "创建一个TodoList组件，包含添加、删除、完成功能"
```

**使用Copilot:**
```typescript
// 输入组件名和注释，让Copilot补全
interface Todo {
  // Copilot会建议完整的interface
}

function TodoList() {
  // Copilot会建议useState和处理函数
}
```

#### 步骤3: 添加样式（AI辅助）

**提示词模板:**
```
"为TodoList组件添加现代化的CSS样式：
- 使用Flexbox布局
- 添加悬停效果
- 使用柔和的配色方案
- 添加过渡动画"
```

#### 步骤4: 添加功能（迭代开发）

**功能清单:**
- ✅ 添加待办
- ✅ 删除待办  
- ✅ 标记完成
- ✅ 编辑待办
- ✅ 过滤显示（全部/已完成/未完成）
- ✅ 本地存储持久化

**AI辅助技巧:**
```
每次添加一个功能，使用：
"在现有TodoList基础上，添加编辑功能"
而不是：
"重写TodoList添加所有功能"
```

#### 步骤5: 测试和修复（AI协助）

**Bug修复流程:**
```
1. 复制错误信息
2. 粘贴到Cursor/Claude
3. 提问："这个错误是什么原因，怎么修复？"
4. 应用建议的修复
```

### 📝 完整示例

<details>
<summary>展开查看AI生成的TodoList组件</summary>

```typescript
import React, { useState, useEffect } from 'react';
import './TodoList.css';

interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState<'all' | 'active' | 'completed'>('all');

  // 从localStorage加载
  useEffect(() => {
    const saved = localStorage.getItem('todos');
    if (saved) setTodos(JSON.parse(saved));
  }, []);

  // 保存到localStorage
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, { id: Date.now(), text: input, completed: false }]);
      setInput('');
    }
  };

  const toggleTodo = (id: number) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id: number) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  return (
    <div className="todo-app">
      <h1>我的待办事项</h1>
      
      <div className="todo-input">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && addTodo()}
          placeholder="添加新任务..."
        />
        <button onClick={addTodo}>添加</button>
      </div>

      <div className="filters">
        <button onClick={() => setFilter('all')}>全部</button>
        <button onClick={() => setFilter('active')}>未完成</button>
        <button onClick={() => setFilter('completed')}>已完成</button>
      </div>

      <ul className="todo-list">
        {filteredTodos.map(todo => (
          <li key={todo.id} className={todo.completed ? 'completed' : ''}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span>{todo.text}</span>
            <button onClick={() => deleteTodo(todo.id)}>删除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
```
</details>

### 🎓 学习要点

#### ✅ 你学到了什么
1. 如何用AI快速搭建项目框架
2. 如何让AI生成组件代码
3. 如何迭代式开发
4. 如何用AI修复bug

#### ⚠️ 注意事项
- AI生成的代码要理解后再使用
- 复杂功能要拆分成小步骤
- 保持代码风格一致性
- 及时测试，不要堆积问题

---

## Prompt工程基础

### 什么是Prompt？

Prompt是你给AI的**指令**或**问题**，好的Prompt能让AI给出更准确的答案。

### 📏 Prompt金字塔（从差到好）

#### Level 1: 模糊的Prompt ❌
```
"写个函数"
```
**问题:** 太模糊，AI不知道写什么

#### Level 2: 基本的Prompt ⚠️
```
"写一个排序函数"
```
**问题:** 缺少细节，AI可能给出不符合需求的代码

#### Level 3: 清晰的Prompt ✅
```
"写一个JavaScript函数，实现快速排序算法，
输入是数字数组，输出是升序排列的新数组"
```
**优点:** 明确语言、算法、输入输出

#### Level 4: 优秀的Prompt ⭐
```
"写一个TypeScript函数实现快速排序：
- 输入: number[]
- 输出: number[] (升序)
- 要求: 使用就地排序优化内存
- 添加类型注释和注释说明
- 包含边界情况处理"
```
**优点:** 详细规格，包含约束和要求

#### Level 5: 专家级Prompt 🏆
```
"在现有的utils/sort.ts文件中，添加一个快速排序函数：

需求：
1. 函数签名: quickSort<T>(arr: T[], compareFn?: (a: T, b: T) => number): T[]
2. 支持自定义比较函数，默认数字升序
3. 使用就地排序优化空间复杂度
4. 添加JSDoc注释
5. 处理边界情况：空数组、单元素、已排序
6. 保持与现有代码风格一致

参考现有的 mergeSort 实现风格
```
**优点:** 上下文完整，考虑周全，与项目集成

### 🎯 编写好Prompt的5个技巧

#### 技巧1: 具体而非模糊
❌ "优化这个函数"  
✅ "优化这个函数的时间复杂度，从O(n²)降到O(n log n)"

#### 技巧2: 提供上下文
❌ "写一个API调用"  
✅ "在现有的React组件中，添加一个useEffect调用后端/api/users接口"

#### 技巧3: 指定格式和风格
❌ "生成测试用例"  
✅ "使用Jest框架生成单元测试，包含正常情况和边界情况"

#### 技巧4: 分步骤处理复杂任务
❌ "创建一个完整的用户管理系统"  
✅ "第一步：创建User类型定义和接口"

#### 技巧5: 包含约束和要求
❌ "写一个登录功能"  
✅ "写一个登录功能，使用JWT认证，包含密码加密，处理登录失败"

### 📚 Prompt模板库

#### 代码生成模板
```
"在 [文件路径] 中创建一个 [函数/类/组件]：
- 功能: [具体功能描述]
- 输入: [参数类型和说明]
- 输出: [返回值类型和说明]
- 约束: [性能/安全/风格要求]
- 示例: [使用示例]"
```

#### 代码重构模板
```
"重构以下代码 [粘贴代码]：
目标：[提升可读性/性能/可维护性]
要求：
- [具体改进点1]
- [具体改进点2]
- 保持功能不变
- 添加必要的注释"
```

#### Bug修复模板
```
"我遇到以下错误：
[错误信息]

相关代码：
[粘贴代码]

请帮我：
1. 解释错误原因
2. 提供修复方案
3. 建议如何避免类似问题"
```

#### 代码解释模板
```
"请解释以下代码：
[粘贴代码]

重点说明：
- 整体功能
- 关键算法/设计模式
- 潜在问题
- 改进建议"
```

### 🔄 迭代式Prompt

不要期望一次就完美，通过对话迭代改进：

```
你: "创建一个用户登录组件"
AI: [生成基础组件]

你: "添加表单验证"
AI: [添加验证]

你: "添加错误提示UI"
AI: [添加UI]

你: "改用Formik库重构"
AI: [重构]
```

---

## 常见问题与解决方案

### ❓ 问题1: AI生成的代码有bug

**症状:** 代码运行报错或逻辑不对

**解决方案:**
1. 复制完整错误信息给AI
2. 提问: "这段代码有问题：[错误]，请修复"
3. 理解修复原理，不要盲目应用
4. 如果多次修复失败，考虑换个思路重新生成

**预防措施:**
- 生成代码后立即测试
- 小步迭代，每次改动少
- 理解代码逻辑再使用

### ❓ 问题2: AI理解错我的需求

**症状:** 生成的代码不是我想要的

**解决方案:**
1. 检查Prompt是否够清晰
2. 提供更多上下文和示例
3. 使用"不是...而是..."纠正方向
   ```
   "不是使用Promise，而是使用async/await"
   ```
4. 分步骤拆解需求

**预防措施:**
- 写详细的Prompt
- 提供代码示例
- 先让AI确认理解再生成代码

### ❓ 问题3: AI补全太慢或不响应

**症状:** Copilot/Cursor反应慢

**解决方案:**
1. 检查网络连接
2. 检查API配额是否用完
3. 尝试切换AI模型
4. 重启编辑器
5. 检查是否在大文件中（>5000行）

**预防措施:**
- 使用付费版获得更好性能
- 避免在超大文件中使用
- 定期清理无用代码

### ❓ 问题4: 不知道何时该用AI

**症状:** 纠结是自己写还是用AI

**应该用AI的场景:**
- ✅ 重复性代码（CRUD、配置）
- ✅ 不熟悉的API使用
- ✅ 标准算法实现
- ✅ 测试用例生成
- ✅ 文档和注释

**应该自己写的场景:**
- ❌ 核心业务逻辑
- ❌ 复杂算法创新
- ❌ 安全敏感代码
- ❌ 性能关键路径（先用AI生成，再手动优化）

### ❓ 问题5: AI生成的代码风格不统一

**症状:** 每次生成的代码风格不一样

**解决方案:**
1. 在Prompt中明确要求风格
   ```
   "遵循现有代码风格，使用2空格缩进，TypeScript strict模式"
   ```
2. 提供项目配置文件（.eslintrc, .prettierrc）
3. 使用Cursor的"Use codebase style"选项
4. 生成后用Prettier/ESLint统一格式化

### ❓ 问题6: 担心AI代码安全性

**症状:** 不确定AI生成的代码是否安全

**解决方案:**
1. **永远不要**直接使用AI生成的认证/加密代码
2. 涉及安全的部分，AI生成后人工仔细审查
3. 使用安全检查工具：
   ```bash
   npm audit
   snyk test
   ```
4. 遵循安全最佳实践，不依赖AI判断

**安全清单:**
- [ ] 输入验证
- [ ] SQL注入防护
- [ ] XSS防护
- [ ] CSRF防护
- [ ] 敏感数据加密
- [ ] 权限检查

### ❓ 问题7: AI建议太多，选择困难

**症状:** Copilot给出多个建议，不知选哪个

**解决方案:**
1. 优先选择最简单的实现
2. 对比不同建议：
   - 可读性
   - 性能
   - 维护性
3. 当不确定时，问Claude/ChatGPT:
   ```
   "这两种实现哪个更好：
   [方案A]
   [方案B]
   从性能和可维护性角度分析"
   ```

### ❓ 问题8: 学习新语言/框架时如何用AI

**最佳实践:**

```
1. 先让AI解释核心概念
   "用简单的语言解释React Hooks"

2. 要求生成简单示例
   "给一个useState的最简单示例"

3. 逐步增加复杂度
   "在上面的基础上添加useEffect"

4. 对比传统写法
   "这个用类组件怎么写？"

5. 询问最佳实践
   "使用Hooks的常见陷阱和最佳实践"
```

---

## 🎯 入门检查清单

完成以下任务，确认你已经掌握基础：

- [ ] 成功安装并配置至少一个AI工具
- [ ] 完成第一个AI辅助的小项目
- [ ] 能写出清晰的Prompt让AI理解你的需求
- [ ] 会使用AI修复简单的bug
- [ ] 理解AI生成的代码并能解释
- [ ] 知道什么时候该用AI，什么时候该自己写

---

## 🎬 下一步

恭喜！你已经完成入门阶段。

👉 [进入进阶技能](../03-进阶技能/README.md)

学习更高效的AI辅助开发技巧。

---

## 💡 温馨提示

> 最好的学习方式是**在真实项目中使用**。  
> 不要只是练习，而要在你的工作项目中应用这些技能。  
> 一周后你会惊讶于效率的提升！
