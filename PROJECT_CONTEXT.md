# PROJECT_CONTEXT｜茄子学习系统项目大脑

## 项目目标

本项目用于管理茄子的初升高学习衔接。目标不是临时补题，而是建立一个能长期追踪、持续校正、可复现的学习系统。

核心目标：

- 建立数学、英语、物理、化学的长期能力画像。
- 用真实课堂、批改和复测证据更新能力状态。
- 将错题转化为 Root Cause，再转化为教材设计和复习计划。
- 按高中节奏推进新知识，同时保留必要自动复习。
- 让任何新会话都能快速接续当前教学状态。

## 教学原则

当前系统采用“原因驱动教学”：

`错题 -> Root Cause -> 能力模型 -> 复习计划 -> 教材生成`

执行原则：

- 不把表面错误直接等同于真实能力缺陷。
- 不根据单道错题判断学生不会整个知识点。
- 教材优先针对能力根因，而不是机械重复原题。
- 不编造未发生的课堂结果。
- 学生是否掌握，必须等待真实课堂、批改或复测证据。

## 当前教学模式

从 Day6R 起采用“重点高中实验班节奏”：

- 70% 新知识
- 20% 应用
- 10% 自动复习

课堂主线用于推进完整知识块。复习由 Review Scheduler、Root Cause Library、Lexical Radar 和错题复现承担。

推荐课堂风格：

- 高中名师 + 家庭教师。
- 连续讲授完整知识块约 5-10 分钟，再设置关键互动。
- 不为了凑时长降低知识密度。
- 不频繁停顿确认“继续吗”。

## 当前课程进度

当前正式课程包：Day6R Rebuild。

原 Day6 已废止，最新正式材料位于 `daily/Day06R/`。

Day6R 四科主题：

- 数学：函数第一课，覆盖函数定义、三要素、定义域、值域、三种表示法、函数判断和综合题。
- 英语：Today's Lexical Radar + Reading + Writing，重点词为 `increase`、`decrease`、`discover`、`depend on`、`especially`。
- 物理：运动图像，覆盖 `s-t` 图像、`v-t` 图像、斜率、面积和运动过程描述。
- 化学：物质的量基础，覆盖 mol、摩尔质量、阿伏伽德罗常数、粒子数和 `m -> n -> N` 公式链。

## 当前学生能力模型

### 数学

基础较扎实，集合（二）Day4 无错题。当前已从集合过渡到函数。需要继续观察函数迁移能力，并保持证明意识、条件检索和表达完整性训练。

重点 Root Cause：

- RC-MATH-001：证明意识不足。
- RC-MATH-002：条件检索不完整。
- RC-MATH-003：表达完整性不足。

### 英语

时态基础较好，`be doing` 已基础掌握。当前主要矛盾是词汇没有稳定进入主动输出系统。

重点能力：

- 词性识别。
- 动词形式变化。
- 固定搭配。
- 主动造句。
- Vocabulary Output / Vocabulary Depth。

重点 Root Cause：

- RC-ENG-001：词性识别不足。
- RC-ENG-002：词汇主动输出不足。
- RC-ENG-003：主谓与动词形式在主动输出中不稳定。

### 物理

公式应用和计算能力较稳定。薄弱点是概念表达、物理意义解释和图像语言转物理语言。

重点 Root Cause：

- RC-PHY-001：概念表达能力不足。
- RC-PHY-002：物理意义与计算公式连接不足。

### 化学

四科中基础相对稳定。摩尔质量已基本掌握，当前进入物质的量基础框架。

重点 Root Cause：

- RC-CHEM-001：概念理解不足，尤其是化学式下标含义和“先乘后加”。

## 当前重点突破

1. 数学：从集合迁移到函数，建立“定义域中的每一个 x 唯一确定一个 y”的函数意识。
2. 英语：把重点词从“会认中文”推进到“会判断词性、会变形、会搭配、会入句”。
3. 物理：从平均速度公式应用推进到运动图像理解和过程表达。
4. 化学：建立 mol、M、NA、N、m、n 的关系链，打通微观粒子和宏观质量。

## ChatGPT 职责

- 进行课堂讲授和互动。
- 根据学生真实回答判断掌握情况。
- 审核教材是否适合当前能力模型。
- 给出下一步教学任务。
- 判断错题背后的 Root Cause。
- 确认教材是否可以生成最终版。

## Codex 职责

- 每次新会话优先读取 `PROJECT_CONTEXT.md`，再读取 `WORKING_STATUS.md`。
- 按 ChatGPT 确认的任务生成教材、练习、作业、教师讲义和答案。
- 维护 daily 目录、system 规则文件、英语雷达系统和长期档案。
- 不编造学习结果。
- 不在审核通过前生成最终打印版。
- 完成明确文件任务后提交 Git。

## 每日工作流

1. 读取 `PROJECT_CONTEXT.md` 和 `WORKING_STATUS.md`。
2. 读取 `system/Teaching_Standard.md`、`system/root_cause_library.md` 和 `茄子学习档案/ability_profile.md`。
3. 根据当前任务读取对应学科材料和最近 daily 记录。
4. 生成或使用当日课程包。
5. 上课后记录真实课堂反馈。
6. 批改 Class Practice 和 Homework。
7. 将错题归入表面错误和 Root Cause。
8. 更新 ability_profile、Root Cause Library、英语 error_bank / review_plan。
9. 更新 `WORKING_STATUS.md`。
10. 提交 Git，并在可用时推送到 GitHub。

## 新会话读取顺序

以后任何新开的 Codex 会话，优先读取：

1. `PROJECT_CONTEXT.md`
2. `WORKING_STATUS.md`
3. `system/Teaching_System.md`
4. `system/Teaching_Standard.md`
5. `system/root_cause_library.md`
6. `茄子学习档案/ability_profile.md`
7. 当前 latest `daily/` 目录

