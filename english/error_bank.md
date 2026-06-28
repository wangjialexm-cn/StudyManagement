# 英语错题库｜Error Bank

## 文件用途

本文件统一整理茄子的英语真实错题，并为后续 Lexical Radar 复现训练提供来源。

记录原则：

- 只把真实课堂、练习、批改中发生过的错误写入“真实错题”。
- 教材中的仿写、改错、训练题不自动视为学生错题。
- 重复错误合并为同一类问题，保留来源。
- 每个错题必须能追溯来源。

## 错题分类

| 分类 | 含义 |
|---|---|
| `vocabulary_issue` | 词汇身份、词义、词性、搭配导致的错误 |
| `grammar_issue` | 语法结构掌握不稳导致的错误 |
| `output_issue` | 会认但主动输出不稳 |
| `spelling_issue` | 拼写错误 |
| `collocation_issue` | 固定搭配错误 |

## 真实错题

| 编号 | 日期 | 原题/情境 | 学生答案 | 正确答案 | 错因 | Root Cause | 知识点标签 | 是否已掌握 | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| E-2026-06-26-01 | 2026-06-26 | 用 `depend on` 表达“成功取决于……” | `Success depend on...` | `Success depends on...` | 第三人称单数主语后动词未加 `-s`；主动输出时动词形式不稳 | 词汇主动输出和动词形式联动不稳，能理解 `depend on`，但主动造句时没有稳定匹配主语和动词形式。 | `subject_verb_agreement`、`verb_form_error`、`depend on` | 否，需复现 | `茄子学习档案/mistakes.md`；Day3 英语副课 |
| E-2026-06-27-01 | 2026-06-27 | The number is increase. | `is increase` | `is increasing` | 表面是现在进行时错误，根因是未稳定识别 `increase` 可作动词 | 不知道 `increase` 本身是动词，不是不会 `be doing`。 | `vocabulary_issue`、`verb_identity_confusion`、`increase` | 否，当前重点复现 | `mistakes/day4.json` |
| E-2026-06-27-02 | 2026-06-27 | The price is decrease. | `is decrease` | `is decreasing` | 表面是现在进行时错误，根因是未稳定识别 `decrease` 可作动词 | 不知道 `decrease` 本身是动词，不是不会 `be doing`。 | `vocabulary_issue`、`verb_identity_confusion`、`decrease` | 否，当前重点复现 | `mistakes/day4.json` |
| E-2026-06-27-03 | 2026-06-27 | The students is learning. | `is learning` | `The students are learning.` | 复数主语 `students` 后 be 动词应为 `are` | 主动输出时主语单复数与 be 动词形式匹配不稳。 | `subject_verb_agreement`、`be_verb`、`present_continuous` | 否，需复现 | `mistakes/day4.json` |

## 重复问题归类

### Day5 批改后的重新判断

ChatGPT 根据 Day5 批改结果重新判断：学生已经基本掌握 `be doing`。`be increase / be decrease` 的根因不是现在进行时语法不会，而是 `increase / decrease` 没有进入主动输出阶段，学生没有稳定识别其动词身份。

后续处理：降低 `be doing` 重复练习比例，提高词性判断、动词变形、常见搭配和主动造句训练比例。

### 1. 词汇身份不清：`vocabulary_issue / verb_identity_confusion`

当前代表词：

- `increase`
- `decrease`

复现要求：

- 每次出现时先判断词性；
- 再判断是否需要 `be + doing`；
- 最后完成自主造句。

### 2. 动词形式变化不稳：`verb_form_error`

当前代表错误：

- `Success depend on...` → `Success depends on...`

复现要求：

- 主语替换：`I / he / success / students`；
- 动词形式替换：原形、三单、现在分词；
- 汉译英输出。

### 3. 主谓一致不稳：`subject_verb_agreement`

当前代表错误：

- `The students is learning.` → `The students are learning.`

复现要求：

- 先找主语；
- 判断单复数；
- 再选择 be 动词或实义动词形式。

## 教材复现题说明

Day5 英语教材中已经围绕 `increase / decrease / depend on / discover / especially` 设计了改错、造句、翻译和写作训练。

这些题目属于“复现训练材料”，不是新的学生错题。只有学生实际作答并批改后，才写入上方“真实错题”表。

## 后续维护规则

- 新错题进入本文件后，同步更新 `english/lexical_radar.md` 和 `english/word_bank.md`。
- 若同类错误再次出现，只追加来源和复现记录，不重复建同类问题。
- 连续两次真实输出正确后，才可将“是否已掌握”改为“是，转入低频抽查”。
- Day6 以后英语教材每天至少从本文件抽取 1 个真实错题做变式复现。
