# 03 - 进阶技能

> 提升AI辅助开发效率，从会用到用好

## 📋 目录

1. [高效代码生成技巧](#高效代码生成技巧)
2. [AI辅助代码审查](#ai辅助代码审查)
3. [AI辅助重构](#ai辅助重构)
4. [AI辅助调试](#ai辅助调试)

---

## 高效代码生成技巧

### 🎯 原则：从"生成代码"到"指导AI写出好代码"

### 技巧1: 上下文驱动生成

#### ❌ 低效方式
```typescript
// 让AI凭空生成
"写一个用户API服务类"
```

#### ✅ 高效方式
```typescript
// 提供现有代码上下文
// 已有: AuthService, HttpClient
// 现在需要: UserService
// 让AI基于现有模式生成

// 在Cursor中:
// 1. 打开 AuthService.ts
// 2. Ctrl+K: "参考AuthService的模式，创建UserService"
```

#### 实战示例

**现有代码：**
```typescript
// services/AuthService.ts
export class AuthService {
  constructor(private http: HttpClient) {}
  
  async login(email: string, password: string) {
    return this.http.post('/auth/login', { email, password });
  }
}
```

**Prompt:**
```
"参考AuthService的模式，创建UserService，包含：
- getProfile()
- updateProfile()
- deleteAccount()
使用相同的HttpClient依赖注入模式"
```

### 技巧2: 渐进式生成

**场景：** 创建一个复杂的表单组件

#### 第1轮：骨架
```
"创建一个React用户注册表单组件的基础结构，
包含name, email, password字段"
```

#### 第2轮：验证
```
"在现有表单基础上添加表单验证：
- name: 2-50个字符
- email: 有效邮箱格式
- password: 最少8位，包含数字和字母"
```

#### 第3轮：UI优化
```
"添加：
- 实时验证提示
- 密码强度指示器
- 提交按钮加载状态"
```

#### 第4轮：集成
```
"集成现有的useAuth hook进行实际注册"
```

### 技巧3: 模式复制

#### 场景：保持代码一致性

**策略：**
```
"参考以下模式：
[粘贴现有好的示例代码]

按照相同模式实现 [新功能]"
```

**示例：**
```
"参考以下Repository模式：

class UserRepository {
  async findById(id: string) { ... }
  async create(data: User) { ... }
}

按照相同模式实现ProductRepository"
```

### 技巧4: 类型优先

#### TypeScript开发技巧

**步骤1: 先定义类型**
```typescript
// 让AI先生成完整的类型定义
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

interface UserService {
  getUser(id: string): Promise<User>;
  updateUser(id: string, data: Partial<User>): Promise<User>;
  deleteUser(id: string): Promise<void>;
}
```

**步骤2: 基于类型生成实现**
```
"基于UserService接口，实现完整的类，使用HttpClient"
```

**好处：**
- AI生成的代码类型安全
- 减少类型错误
- 代码更规范

### 技巧5: 测试驱动生成

#### 先写测试再生成实现

**步骤1: 生成测试**
```
"为一个排序函数生成Jest测试用例：
- 正常排序
- 空数组
- 单元素
- 已排序数组
- 包含重复元素"
```

**步骤2: 基于测试生成实现**
```
"根据以上测试用例，实现通过所有测试的排序函数"
```

### 技巧6: 增量补全

#### 利用Copilot的上下文理解

```typescript
// 写注释，让Copilot理解意图
// 获取用户列表，支持分页和搜索
async function getUsers(
  // Copilot会建议参数类型
  page: number,
  pageSize: number,
  search?: string
): Promise<{ users: User[]; total: number }> {
  // Copilot会建议完整实现
}
```

### 技巧7: 批量生成

#### 场景：生成重复性代码

**示例：生成CRUD endpoints**

```
"生成RESTful API endpoints的Express路由：
资源：Product
操作：GET, POST, PUT, DELETE
包含：
- 参数验证
- 错误处理
- 统一响应格式"
```

---

## AI辅助代码审查

### 🎯 目标：让AI成为你的Code Reviewer

### 审查类型1: 代码质量检查

#### Prompt模板
```
"审查以下代码，检查：
1. 代码规范（命名、格式）
2. 潜在Bug
3. 性能问题
4. 可读性
5. 改进建议

[粘贴代码]"
```

#### 实战示例

**提交给AI审查的代码：**
```javascript
function getData(url) {
  return fetch(url).then(r => r.json());
}

async function main() {
  const data = await getData('/api/users');
  for (var i = 0; i < data.length; i++) {
    console.log(data[i]);
  }
}
```

**AI反馈：**
```
问题发现：
1. ❌ 缺少错误处理
2. ⚠️ 使用var而非const/let
3. ⚠️ 可以用更现代的for...of
4. ⚠️ 缺少类型定义

改进建议：
[AI提供改进后的代码]
```

### 审查类型2: 安全审查

#### Prompt模板
```
"从安全角度审查以下代码：
- SQL注入风险
- XSS风险
- 认证/授权问题
- 敏感数据泄露
- 其他安全问题

[粘贴代码]"
```

#### 示例
```javascript
// 不安全的代码
app.get('/user', (req, res) => {
  const id = req.query.id;
  db.query(`SELECT * FROM users WHERE id = ${id}`, (err, result) => {
    res.json(result);
  });
});
```

**AI会指出：**
- ❌ SQL注入风险
- ❌ 缺少认证检查
- ❌ 敏感数据直接暴露

### 审查类型3: 性能审查

#### 使用Claude进行深度分析

```
"分析以下代码的性能问题：

[粘贴代码]

重点关注：
- 时间复杂度
- 不必要的循环
- 内存使用
- 可优化的点"
```

#### 实战案例

**原始代码：**
```javascript
function findDuplicates(arr) {
  const duplicates = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j] && !duplicates.includes(arr[i])) {
        duplicates.push(arr[i]);
      }
    }
  }
  return duplicates;
}
```

**AI分析：**
```
问题：
- 时间复杂度O(n³) - 嵌套循环 + includes
- 空间复杂度可优化

优化方案：
[使用Set，O(n)实现]
```

### 审查类型4: 架构审查

#### 审查设计模式和架构

```
"从软件设计角度评审：
[粘贴多个文件的代码]

关注：
1. 是否遵循SOLID原则
2. 是否有代码重复
3. 模块划分是否合理
4. 依赖关系是否清晰
5. 可测试性"
```

### 建立审查清单

#### 创建自定义审查模板

```markdown
## 我的代码审查清单

### 功能性
- [ ] 实现了所有需求
- [ ] 边界情况处理
- [ ] 错误处理完整

### 代码质量
- [ ] 命名清晰
- [ ] 函数单一职责
- [ ] 避免魔法数字
- [ ] 注释适当

### 性能
- [ ] 无明显性能瓶颈
- [ ] 合理的时间复杂度
- [ ] 资源正确释放

### 安全
- [ ] 输入验证
- [ ] 无注入风险
- [ ] 敏感数据保护

### 可维护性
- [ ] 代码易读
- [ ] 结构清晰
- [ ] 遵循项目规范
```

**使用方式：**
```
"根据以上清单审查代码：
[粘贴代码]"
```

---

## AI辅助重构

### 🎯 目标：安全、高效地改进代码

### 重构类型1: 提取函数

#### 场景：函数太长

**原始代码：**
```typescript
function processOrder(order: Order) {
  // 验证订单
  if (!order.items || order.items.length === 0) {
    throw new Error('Empty order');
  }
  
  // 计算总价
  let total = 0;
  for (const item of order.items) {
    total += item.price * item.quantity;
  }
  
  // 应用折扣
  if (order.coupon) {
    total *= (1 - order.coupon.discount);
  }
  
  // 保存订单
  db.save(order);
  
  // 发送邮件
  sendEmail(order.email, `Order confirmed: ${total}`);
}
```

**Prompt：**
```
"重构这个函数，提取出独立的小函数：
- 订单验证
- 价格计算
- 折扣应用
- 订单保存
- 通知发送"
```

### 重构类型2: 设计模式应用

#### 场景：多个if-else

**原始代码：**
```typescript
function processPayment(type: string, amount: number) {
  if (type === 'credit') {
    // 信用卡支付逻辑
  } else if (type === 'debit') {
    // 借记卡支付逻辑
  } else if (type === 'paypal') {
    // PayPal支付逻辑
  } else if (type === 'crypto') {
    // 加密货币支付逻辑
  }
}
```

**Prompt：**
```
"使用策略模式重构这段代码，
使其易于添加新的支付方式"
```

### 重构类型3: 类型改进

#### 场景：使用any或缺少类型

**原始代码：**
```typescript
function formatUser(user: any) {
  return {
    name: user.name,
    email: user.email,
    age: user.age
  };
}
```

**Prompt：**
```
"为这个函数添加完整的TypeScript类型定义，
包括输入输出类型和可能的null处理"
```

### 重构类型4: 现代化

#### 场景：老式JavaScript代码

**原始代码：**
```javascript
var users = [];

function addUser(name, email) {
  var user = {
    id: users.length + 1,
    name: name,
    email: email
  };
  users.push(user);
  return user;
}

function findUser(id) {
  for (var i = 0; i < users.length; i++) {
    if (users[i].id === id) {
      return users[i];
    }
  }
  return null;
}
```

**Prompt：**
```
"现代化这段代码：
- 使用ES6+语法
- 使用TypeScript
- 使用类
- 使用Map而非数组存储"
```

### 重构类型5: 性能优化

#### 步骤1: 识别瓶颈
```
"分析这段代码的性能瓶颈：
[粘贴代码]"
```

#### 步骤2: 针对性优化
```
"优化这段代码的性能，
重点优化 [AI指出的瓶颈]"
```

#### 步骤3: 验证改进
```
"对比优化前后的时间/空间复杂度"
```

### 安全重构的原则

#### ⚠️ 重要提醒

1. **小步重构**
   - 一次只改一个地方
   - 每步都测试

2. **保持功能不变**
   ```
   "重构以下代码，改进 [具体方面]，
   但保持功能完全一致"
   ```

3. **先写测试**
   ```
   "在重构前，先为现有代码生成测试用例"
   ```

4. **渐进式进行**
   ```
   不要："完全重写这个模块"
   而是："先重构最复杂的那个函数"
   ```

---

## AI辅助调试

### 🎯 目标：快速定位和修复问题

### 调试策略1: 错误信息分析

#### 基础模板
```
"我遇到以下错误：

错误信息：
[完整的错误堆栈]

相关代码：
[出错的代码]

请：
1. 解释错误原因
2. 提供修复方案
3. 说明如何避免"
```

#### 实战示例

**错误：**
```
TypeError: Cannot read property 'map' of undefined
  at UserList.render (UserList.tsx:15)
```

**提供给AI：**
```
"错误信息：Cannot read property 'map' of undefined

代码：
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => <li>{user.name}</li>)}
    </ul>
  );
}

请分析并修复"
```

### 调试策略2: 逻辑错误

#### 场景：代码运行但结果不对

**模板：**
```
"这段代码的预期行为是 [描述预期]
但实际结果是 [描述实际]

代码：
[粘贴代码]

请帮我找出逻辑错误"
```

#### 技巧：提供测试用例
```
"测试用例：
输入：[1, 2, 3, 4, 5]
预期输出：[2, 4, 6, 8, 10]
实际输出：[2, 4, 6, 8]

代码：
[粘贴代码]"
```

### 调试策略3: 性能问题

#### 使用Claude进行分析

```
"这段代码运行很慢：

代码：
[粘贴代码]

数据规模：
- 用户数：10,000
- 每个用户的订单：平均100个

请：
1. 分析性能瓶颈
2. 提供优化方案
3. 给出时间复杂度对比"
```

### 调试策略4: 并发问题

#### Race Condition调试

```
"我的代码有时工作正常，有时出错：

代码：
[异步代码]

怀疑是并发问题，请帮我：
1. 识别潜在的竞态条件
2. 提供修复方案"
```

### 调试策略5: 集成问题

#### API调用调试

```
"我在调用API时遇到问题：

API文档：
[API规格]

我的代码：
[调用代码]

错误：
[响应或错误]

请帮我找出问题"
```

### 高级调试技巧

#### 使用Cursor的调试功能

1. **选中报错代码**
2. **Ctrl+K** 输入：`"Fix this error"`
3. **查看建议** 并应用

#### 结合传统调试

```typescript
// 1. 先用AI理解代码流程
"解释这段代码的执行流程：
[复杂代码]"

// 2. 基于理解添加日志
console.log('[AI建议的关键点]', variable);

// 3. 运行并收集日志

// 4. 把日志给AI分析
"根据以下日志分析问题：
[日志输出]"
```

### 调试清单

```markdown
遇到Bug时的步骤：

1. [ ] 复现问题
   - 记录复现步骤
   - 记录预期vs实际

2. [ ] 收集信息
   - 错误消息
   - 堆栈跟踪
   - 相关代码
   - 输入数据

3. [ ] AI初步分析
   - 粘贴错误和代码给AI
   - 获取可能的原因

4. [ ] 验证假设
   - 按照AI建议添加日志
   - 或使用debugger

5. [ ] 应用修复
   - 理解修复方案
   - 应用并测试

6. [ ] 防止复发
   - 添加测试用例
   - 更新文档
```

---

## 🎯 进阶检查清单

完成以下任务，确认你已掌握进阶技能：

- [ ] 能利用上下文生成高质量代码
- [ ] 会使用AI进行全面的代码审查
- [ ] 能安全地进行AI辅助重构
- [ ] 会用AI快速定位和修复Bug
- [ ] 理解何时该信任AI，何时该质疑

---

## 🎬 下一步

准备好迎接更大的挑战了吗？

👉 [进入高级技巧](../04-高级技巧/README.md)

学习架构设计、复杂问题解决等高级应用。

---

## 💡 实践建议

> **30天挑战**  
> 接下来30天，每天用AI：
> - 生成至少一个功能
> - 审查至少一段代码
> - 重构至少一个函数
> - 解决至少一个Bug
>
> 30天后，这些技能会成为肌肉记忆！
