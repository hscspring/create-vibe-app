---
title: 为了让AI干活儿，我竭尽所能——我的 Vibe Coding 认知升级之路
date: 2026-01-18 17:00:00
categories: Coding
tags: [AI, LLM, AGI, AI-Coding, CompoundEngineering, OpenSpec, context, kanban, spec, skill]
mathjax: false
---


AI Coding 已经疯了。

我也在一边根据本能在使用，同时也在学习一些新的技巧和方法。直到看到《[认知重建：Speckit 用了三个月，我放弃了——走出工具很强但用不好的困境 - 知乎](https://zhuanlan.zhihu.com/p/1993009461451831150)<sup>[1]</sup>》这篇文章，我觉得自己得系统梳理一下了。

这里就随便那么梳理一下吧，可能会比较乱。

<!--more-->

## 来自程序员的本能

去年 12 月才算正式开始使用，上来用的就是 TRAE 和 Antigravity，里面有 plan 模式。所以，最简单的方式就是：design-review-execute-review，实际上，我之前写的几个[项目](https://yam.gift/2026/01/01/AI/2026-01-01-From-AI-Coding-Watch-World-Future/)<sup>[2]</sup>都是这种风格。

简单项目这种方法应该足够了，但是后面新开了一个大项目，涉及到算法、后端、前端几个部分，每个部分也都不简单。这时候感觉之前那种简单的方式就不太够用了。其实，也不一定是不够用，只是说，再随便写一下 design 文档就太潦草了，需要更加细致的对任务和设计进行描述。随便写的后果就是很多细节完全不是想要的……

于是，我慢慢增加了 API 环节，先把模块间的“协议”定下来，变成了 design-api-review-execute-review，同时，由于项目有不同模块，我在每个模块下都增加了 design，并且因为更新比较频繁，我让它更新的时候同时更新 design。这样相当于给它一个统一的世界状态，不至于后面漂移的太厉害。

另外，虽然每次执行完都有 Walkthrough，但我还是会让它给我一段测试脚本和操作文档，这个主要用来人工验收。后面又继续增加了一些全局统一的约定，比如可能用到的 key、前端每次 run 之前先执行 `nvm use 22` 等等。总之，是摸着石头过河，边用边根据实际情况调整。

同时，对于比较大的项目，如果子项目之间是相互独立的，我会先完成子项目，然后其他用到它的地方会把它当做黑盒。

## 来自同行的经验

陆陆续续和一些同行交流（有时候就是看看群消息别人的讨论），又 get 到一些新的技巧和方法。

### reference

X 哥说让它基于已有项目修改会更加容易，或者给一段已有的实现。我很快就采用了，在项目根目录增加了 `reference` 文件夹，把要参考的代码都放里面。

### task

群里讨论的比较多的是 task 模式，后来有人专门把这个做成开源工具：[Vibe Kanban](https://www.vibekanban.com/docs)<sup>[3]</sup>，纯任务驱动 + GitHub 协作的模式，感觉都不需要看代码。

![](https://qnimg.lovevivian.cn/tool-kanban-1.jpg)

其实 plan 模式会提供 task 的，这个工具只是可视化+Git 规划、审查和管理代码，对我个人吸引力不太大。

### spec

同时，还知道了 [OpenSpec](https://github.com/Fission-AI/OpenSpec?tab=readme-ov-file#how-openspec-compares)<sup>[4]</sup>，算是一种规范驱动的开发模式。工作流程如下：

```bash
┌────────────────────┐
│ Draft Change       │
│ Proposal           │
└────────┬───────────┘
         │ share intent with your AI
         ▼
┌────────────────────┐
│ Review & Align     │
│ (edit specs/tasks) │◀──── feedback loop ──────┐
└────────┬───────────┘                          │
         │ approved plan                        │
         ▼                                      │
┌────────────────────┐                          │
│ Implement Tasks    │──────────────────────────┘
│ (AI writes code)   │
└────────┬───────────┘
         │ ship the change
         ▼
┌────────────────────┐
│ Archive & Update   │
│ Specs (source)     │
└────────────────────┘

1. Draft a change proposal that captures the spec updates you want.
2. Review the proposal with your AI assistant until everyone agrees.
3. Implement tasks that reference the agreed specs.
4. Archive the change to merge the approved updates back into the source-of-truth specs.
```

四步曲翻译成中文：

- 起草一份包含你想要的更新的变更提案。
2. AI 审查提案，直到所有地方对齐。
3. 实现符合约定规范的任务。
4. 归档该更改，将批准的更新合并回真实来源规范。

我觉得和自己的模式在本质上差不太多。

### multi-agent

这个模式早就知道的，也看很多人提到过，就是不同 agent 负责不同的角色，比如前端一个，后端一个，测试一个，不过我还没怎么用过。就是这个只是增加异步并发，其实并不是真正意义上的范式改进。再加上我自己是需要人工 review 代码的，所以那么快写完也没啥意义，就一直没用。说白了，感觉还是不是完全信任 AI，这点后面得改进。

### other trick

还有一些其他的方法技巧，也是在认知内的，并且时不时使用的。不过我觉得都算不上范式上的创新。

**测试**

包括让 AI 先写测试用例，用脚本、browser 测试等等。

**评审**

让 AI 自己评审代码，并强制 lint。人工审查关键逻辑，核心逻辑尽量理解，普通代码（尤其是 UI 相关）就大概看看。

**上下文知识库**

有点类似我之前提到那个动态更新的 design、api 文档、全局规范等，主动把上下文管理起来。这些都是项目的知识库。

## 系统性升级

来自开头提到的那篇文章，我看了三遍还意犹未尽，很多东西确实写到点子上了（不过讲真的有点乱）。而且，一看就是真正做过的经验之谈。这里只提取认知部分，其实具体操作都不重要。

### 第一性原理

真实的日常工作模式（我做了一些调整）:

- **任务管理**：Todo List 分优先级，或者就是某个需求文档。
- **简单任务 Fire and Forget**：低频低思考成本事项秒回即忘。
- **复杂任务 SOP 化**：脑内计划 + 执行机器模式 + 文档跟踪。
- **文档管理**：我会习惯性地先写一份大致的设计文档和API文档（是的，API 文档一定在代码之前搞定），主要目的是用来理思路（我一贯的观点：写代码不快是没想清楚不是打字慢）。同时做完后也会习惯性地写一份 README，讲使用流程。
- **窗口即上下文**：每个窗口对应一个具体的模块或功能，这里的窗口可以是文件的 tab，也可以是 terminal、浏览器之类。
- **备忘录**：记录死记硬背的内容（打包命令、数据库 IP 密码之类的信息，这个不太重要）。

作者说这是土方法，和 AI 比起来确实，不过确实很有效，而且按这个模式已经做了很多项目了，心智上比较熟悉，操作上比较熟练。我之前没有刻意主动地往这个角度想，但这个思考确实很有意义。

文章特别强调“过程”的价值，因为大部分真实场景的项目不是一锤子买卖，而是需要持续维护和迭代的。spec 关注规范和结果，但不关心过程，这就导致每次都是重来一遍，边际成本不变。真实的价值在过程中：

```text
执行 → 有问题 → 验证 → 排查 → 继续执行
                    ↓
            排查信息往往没被记录
                    ↓
        时间一久或换人，下次重新排查
```

我觉得有点自己之前提到的“记录更新变化”的那么一点意思。

### 复合工程

其实原文还有个上下文工程，不过这个属于我认知的一部分，前面也提到过，这里就不再赘述了。复合工程来自 Claude 和 Every 团队的实践交流，后面[开源](https://github.com/EveryInc/compound-engineering-plugin/tree/main)<sup>[5]</sup>了，它的目的是：**让每一单元的工程工作使后续工作变得更容易，而非更难。**

```text
Plan ──────→ Work ──────→ Review ──────→ Compound
详细规划     执行工作     质量检查       知识沉淀
   ↑                                       │
   └───────────────────────────────────────┘
            知识复合：下次规划更精准
```

思想看起来和我的想法是类似的（**过程文档化**），不过具体做法不太一样：我的太糙了没法看，这里的比较规范和细粒度。

复合工程的三个设计模式：

| 模式     | 核心思想                                     | 价值                 |
| -------- | -------------------------------------------- | -------------------- |
| 并行代理 | 多角度分析时启动多个专业代理，合并结果后继续 | 提高分析覆盖度和效率 |
| 意图路由 | 入口统一，根据意图自动路由到具体工作流       | 降低用户认知负担     |
| 知识复合 | 问题解决 → 文档化 → 未来查找 → 团队变聪明    | 边际成本递减         |

### 知识复合

单独拎出来，这个最重要。主要结构如下：

```text
用户输入 → Command（入口）→ Agent（决策层）→ Skill（执行层）
                              ↓
                         意图识别、流程路由
                              ↓
                         调用具体 Skill 执行
                              ↓
                         experience-index（经验检索）
```

来自**复合工程**的设计启示：

| 维度     | 启示                                                         |
| -------- | ------------------------------------------------------------ |
| 任务分解 | 阶段化执行（Plan → Work → Review → Compound），并行化处理，状态持久化 |
| 质量保障 | 多角度并行审查，分级处理（P1/P2/P3），持续验证（边做边测）   |
| 知识管理 | 即时文档化（趁上下文新鲜），分类存储（按问题类型），交叉引用（关联 Issue、PR） |
| 工具设计 | 工具提供能力而非行为，Prompt 定义意图和流程，让代理决定如何达成目标 |

看起来好像本能地都涉及过，就是太太太粗糙了。

极简主义设计理念（无需关心具体细节，只需关心理念）:

- **入口极简化**：只有两个命令入口，把复杂性藏到了 Agent 的智能路由里。用户只需表达意图，Agent 会判断该调用哪个 Skill。
- **Skill 而非工具堆叠**：speckit/openspec 倾向于提供更多工具、更多模板、更多约束。这里选择把能力编码为 Skill，让 Agent 在需要时自动调用，而不是让用户手动选择"现在该用哪个工具"。这个现在正在逐渐成为主流。关于 skill 可以看[这里](https://agentskills.io/home)<sup>[6]</sup>。
- **上下文自动加载**：Claude Code 团队说"人类和 AI 看同样的输出，说同样的语言，共享同一个现实"。这里把这个原则应用到上下文管理——不是让用户手动指定"加载哪些背景资料"，而是让 Agent 根据当前阶段自动加载相关的 `context/`。用户感受不到"上下文加载"这个动作，但 AI 已经具备了完整的信息。这个很有意思，**提供了一种管理 context 的方式——分门别类按约定放好**。
- **删除优先于添加**：每次迭代时，作者会问自己"有哪些东西可以删掉？"而不是"还能加什么功能？"。AGENTS.md 从最初的长篇大论，精简到现在只放通用规范和目录指针，具体流程全部下沉到 Skill 里。
- **双重用户设计**：Claude Code 为工程师和模型同时设计界面。AI 工程化也是——命令人可以手动调用，Agent 也可以在流程中自动调用子 Skill。同一套能力，两种调用方式，没有冗余。

这里面的理念我们提炼一下：

- AGENT.md 放通用规范和目录指针。
- SKILL.md 是各种能力的抽象，会有多个 SKILL。
- `context/` 下面包含各种各样的上下文信息，比如设计文档、API、重要更新日志、通用知识等。这是个项目相关知识库。

#### 工具/SKILL设计

关于工具（理解为 SKILL 也行）设计的通用理念很不错：

- 好的工具
    - 自包含：不依赖"记住"之前的对话。
    - 返回精简：只返回 token 高效的必要信息。
    - 边界清晰：用途明确，减少决策成本。
    - 发挥模型优势：利用模型擅长的能力。
- 坏的工具
    - 返回完整数据库查询结果（可能数千行）。
    - 工具描述长达数百 token。
    - 多个工具功能重叠，边界模糊。
    - 强迫模型做它不擅长的事情。

关于 SKILL，我们可以看看 [What are skills? - Agent Skills](https://agentskills.io/what-are-skills)<sup>[7]</sup> 这里的介绍：Agent Skills 是一种轻量级的开放格式，可通过专业知识和工作流程扩展 AI 代理的功能。下面是一个具体的示例：

```bash
my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```

可以去 [anthropics/skills: Public repository for Agent Skills](https://github.com/anthropics/skills)<sup>[8]</sup> 看一些具体的例子。

下面这两个网址都提供了一些编写技巧：

- [How to create custom Skills | Claude Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)<sup>[9]</sup>
- [Claude-meta-skill/create-skill-file/SKILL.md](https://github.com/YYH211/Claude-meta-skill/blob/main/create-skill-file/SKILL.md)<sup>[10]</sup>

SKILL 和 MCP 的区别是，MCP 可能更加外部化、工具化一点。如[这里](https://support.claude.com/en/articles/12512176-what-are-skills)<sup>[11]</sup>的介绍：MCP 将 Claude 连接到外部服务和数据源。SKILL 提供程序性知识——即完成特定任务或工作流程的说明。可以将两者结合使用：MCP 连接使 Claude 能够访问各种工具，而技能则教会 Claude 如何有效地使用这些工具。

SKILL 看起来好像就是特定任务的**「提示词」**，在需要时加载，更适合专业化的工作流程。

#### context设计

我们把 context 单独拿出来看。文章给出如下原则：

- 分层式信息组织。比如下面的“分层示例”。
- “即时”上下文策略。轻量维护索引，需要时加载具体信息。
- 上下文压缩与笔记系统。
    - 压缩：
        - 将接近上下文窗口限制的对话内容总结。
        - 保留：架构决策、未解决的 bug、实现细节。
        - 丢弃：冗余的工具输出或消息。
        - 用摘要重新初始化新的上下文窗口。
    - 结构化笔记：
        - 智能体定期将笔记写入上下文窗口外的持久化存储。
        - 稍后根据需要拉回上下文窗口。
        - 实现跨压缩步骤的连贯性。

分层示例：

```bash
context/
├── business/
│   └── 活动业务边界.md          ← 概要层（意图识别时加载）
├── tech/
│   └── Apollo配置规范.md       ← 技术层（方案设计时加载）
└── experience/
    ├── 商品发放历史问题.md      ← 经验层（实施前加载）
    └── 雅典娜配置注意事项.md    ← 详细层（配置时加载）
```

AI 工程化对应：

| AI 工程化设计                  | 上下文工程原理                                 |
| ------------------------------ | ---------------------------------------------- |
| `context/` 分层目录            | 分层式信息组织，按阶段按需加载                 |
| Skill 封装固定流程（`skill/`） | 稳定执行过程，避免提示词遗漏导致的上下文不完整 |
| Subagent 架构（`agent/`）      | 主 Agent 保持精简，子任务独立窗口              |
| 状态文件传递（`requirement/`） | 不依赖"记忆"，依赖结构化状态                   |
| 经验沉淀机制（`wiki/`）        | 将知识编码为可检索上下文，而非依赖人脑         |

### 整体汇总

接下来看一下整体结构，噢，我很喜欢这句：“目录结构：位置即语义”，让我想起了 [umi](https://v3.umijs.org/zh-CN/docs/convention-routing)<sup>[12]</sup> 的“文件即路由”。我稍微改了一下：

```bash
your-project/
├── MAIN.md                         # 项目入口（包含规范、目录、基本信息等）
├── agent/                          # AI下属，各司其职（让其通用化）
│   ├── phase-router.md                      # 阶段路由，意图识别
│   ├── requirement-manager.md               # 需求全生命周期管理
│   ├── design-manager.md                    # 方案全生命周期管理
│   ├── implementation-executor.md           # 开发实施执行
│   └── experience-depositor.md              # 经验沉淀（独立上下文）
├── mcp/                            # 外部工具（本来就通用的）
│   ├── TAPD MCP                             # 需求管理
│   └── iWiki MCP                            # 知识管理
├── skill/                          # 通用能力（让其通用化）
│   ├── req-create/                          # 需求创建
│   ├── design-create/                       # 方案创建
│   ├── workspace-setup/                     # 环境搭建
│   └── code-commit/                         # 代码提交
├── wiki/                           # 项目知识库（长期记忆，和项目绑定）
│   ├── business/                            # 业务领域知识
│   ├── design/                              # 设计文档
│   ├── tech/                                # 技术分析
│   ├── api/                                 # 接口文档
│   └── experience/                          # 历史经验
├── requirement/                    # 需求管理（看板或TODO，和项目绑定）
│   ├── INDEX.md                             # 需求索引
│   ├── in-progress/                         # 进行中需求
│   └── completed/                           # 已完成需求
├── reference/                      # 参考实现区，能抄就抄吧……改巴改巴的也可以
└── code/                           # 代码区
```

这里，我把 `context` 改成了 `wiki`，因为感觉 `context` 范围更广。

这是 AI 时代的项目目录，一切为了 AI 方便，同时考虑便于人工维护。我打算先按这个思路实践实践，后面看情况是否需要调整。

#### 关于知识沉淀

这部分单纯做点笔记吧，感觉很有道理。

**触发时机**

```text
不是：做完需求后专门花时间"写总结"
而是：在流程关键节点自动触发沉淀

具体触发点：
├── 需求完成时 → requirement-completer skill 自动提取可复用经验
├── 遇到问题解决后 → 用户说"记住这个坑" → experience-depositor agent 记录
├── 代码提交时 → code-commit skill 检查是否有值得记录的模式
└── 流程优化时 → /optimize-flow 命令专门用于沉淀和优化
```

**沉淀内容**

```text
# context/experience/商品发放-钱包选择问题.md

## 问题描述
商品发放时选错钱包类型，导致用户领取失败

## 触发条件
- 需求涉及商品发放
- 商品类型为虚拟商品

## 解决方案
虚拟商品必须发到虚拟钱包，实物商品发到实物钱包
具体判断逻辑见 Apollo 配置：xxx.wallet.type

## 校验方式
检查 goods_type 与 wallet_type 的匹配关系

## 关联文档
- context/tech/Apollo配置规范.md
- context/tech/services/商品服务技术总结.md
```

**加载机制**

```text
Agent 的上下文加载逻辑：

1. 意图识别阶段
   phase-router 识别意图，路由到对应 Agent
        ↓
2. 经验检索阶段
   Agent 调用 experience-index Skill，传入场景描述
   Skill 检索四类规则文件：
   ├── context-rules.md  → 匹配需加载的背景文档
   ├── risk-rules.md     → 匹配风险提示
   ├── service-rules.md  → 匹配服务依赖建议
   └── pattern-rules.md  → 匹配代码规范
        ↓
3. 返回结构化结果
   {
     "context": { "files": ["商品发放历史问题.md"] },
     "risk": { "alerts": [{"level": "high", "message": "注意钱包类型"}] },
     "service": { "suggestions": ["商品服务", "钱包服务"] },
     "pattern": { "files": ["error-handling.md"] }
   }
        ↓
4. Agent 主动提醒
   "注意：历史上商品发放有钱包选择问题，请确认..."
```

这里后续可能需要定义一下整个链路，把过程 SOP 掉，maybe 需要一个专门的文件夹。

**演进机制**

```text
阶段 1：纯文档（被动）
context/experience/xxx.md
→ AI 读取后提醒，但需要人确认

阶段 2：校验 Skill（半自动）
skill/product-distribution-validator
→ 自动校验配置，发现问题直接报错

阶段 3：完整 Command（全自动）
cmd/implement-product-distribution
→ 一个命令：加载背景 + 校验 + 生成 + 提醒 + 沉淀新经验

演进判断标准：
- 同类需求做了 5 次以上 → 考虑封装 Skill
- Skill 被调用 10 次以上 → 考虑封装 Command
- 不要过早抽象，让实践驱动演进
```

这里其实是 SKILL 的组合，文章是最后开发成工具了，所以需要变成 command 方便执行（这个命名感觉有歧义），但组装成一个大的 SKILL 也是可以的。总之，把 SKILL 当做小的 module 就行，跟写代码没有本质区别，只是换个写法而已。

#### 实践过程

这里来大致模拟一遍流程，不一定准确。

```text
1. 初始化项目，创建好统一目录。
        ↓
2. 用户初始化一个任务，可以是一句话或一段描述。
        ↓
3. 产品经理把需求细化成不同模块的细化需求，也许还可以画出 UI。用户确认。
        ↓
4. 架构师分析产品需求，并设计整体架构，形成设计文档。用户确认。
        ↓
5. 架构师根据设计文档设计接口。用户确认。
        ↓
6. 前后端根据接口和需求进行代码开发。用户确认。
        ↓
7. 需求开发完成，测试进行相关测试。用户确认。
        ↓
8. 循环执行3-7，直到完成用户任务。
```

每一次“用户确认”都是一次知识沉淀的时机，可以由用户刻意引导沉淀，比如使用某 SKILL 完成沉淀，也隐式地可以由 SKILL 自己判断是否值得沉淀。

这里没有意图判断，全流程有 AI 主导，人工仅做确认或一些信息补充和反馈。

每一步执行都自动根据目录加载相应的信息，这个可能直接固定在对应的 agent 中。

## 总结

为了让 AI 更好地干活，我感觉比写代码还累……要不是它能并行还写得快，我费这劲干啥……难怪不少人说：“让子弹再飞会儿”……也许后面很多东西就都内化到模型里面了。

其实，我最终想要的是：“一旦前期我确认了，后面全部由 AI 自动完成，它们可能会持续运行一整天，直到完成我的任务。”我给他的只是一个描述，顶多再给一个别的案例（也许我只是提个名字让他自己去搜集资料，完成调研）。

另外，我觉得这一套不仅要用在开发上，还得扩展到其他方面，比如客服、营销等等——最终形态是自动运作的全 AI 员工的虚拟组织。

