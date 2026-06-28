# Lexical Radar v1.0｜英语词汇雷达系统

## 文件用途

本文件用于统一记录茄子英语学习中的“词汇进入句子系统”问题。

当前判断不是简单的“不认识单词”，而是：

- 有些词知道中文意思，但不能稳定判断词性；
- 有些词会认，但不能稳定造句；
- 有些词会背，但搭配、动词形式、句中位置不稳定；
- 有些错误表面像语法错误，根因其实是词汇身份不清。

后续 Day6 以后英语教材必须每天从本文件和 `english/error_bank.md` 中抽取内容进行复现训练。

## 资料来源

| 来源 | 内容 | 处理方式 |
|---|---|---|
| `英语学情诊断与假期补漏清单.md` | 214 个词汇/短语复习记录、A/B/C 分层词、易混词、句型与写作问题 | 合并进 `word_bank.md` 和本文件的雷达分类 |
| `茄子学习档案/learning_record.md` | Day3 英语副课记录 | 作为 `increase / decrease / discover / depend on / especially` 的学习来源 |
| `茄子学习档案/mistakes.md` | Day3 英语输出错误 | 写入 `error_bank.md` |
| `mistakes/day4.json` | Day4 英语真实错题 | 写入 `error_bank.md`，并标记 `increase / decrease` 为当前重点词 |
| `daily/Day05/english/` | Day5 英语教材与训练设计 | 只作为复现训练来源，不直接记为真实错题 |

## 当前核心发现

### 0. Day5 批改后的重新判断

根据 Day5 批改结果，ChatGPT 重新判断：

- 学生已经基本掌握 `be doing`。
- Day5 已正确完成：`The number is increasing.`、`The price is decreasing.`
- Day4 的 `be increase / be decrease` 不应继续按“现在进行时语法漏洞”处理。
- 真正原因是 `increase / decrease` 没有进入主动输出阶段，学生没有稳定意识到这两个词本身可以作动词。

因此，从 Day6 开始，英语训练重心调整为 Lexical Radar：

1. 单词词性；
2. 动词变形；
3. 常见搭配；
4. 主动造句。

`be doing` 只保留少量复现，不再高比例重复训练。

### Today's Discovery（Day5）

学生认识 `increase / decrease` 的中文意思。

但不知道：

- `increase` 本身就是动词；
- `decrease` 本身就是动词。

因此，错误分类正式修正：

| 原分类 | 修正后分类 | 子类型 |
|---|---|---|
| `grammar_error` | `vocabulary_issue` | `verb_identity_confusion` |

教学含义：

以后遇到类似错误，不能只看表面结构是否像语法错误，要先判断学生是否真正知道词汇身份。

### 1. increase / decrease 问题

- `increase / decrease` 中文意思知道。
- 词性识别不稳，不能稳定判断它们本身可以作动词。
- 曾误写为 `be increase / be decrease`。
- 根因不是单纯不会 `be doing`，而是没有把 `increase / decrease` 真正纳入“动词句子系统”。
- 归类：`vocabulary_issue / verb_identity_confusion`。

### 2. depend on 问题

- 能理解 `depend on` 的意思。
- 主动输出时出现 `Success depend on...`。
- 归类：`verb_form_error` + `subject_verb_agreement`。

### 3. 词汇整体问题

- 看英文认中文明显好于“看中文主动拼出英文”。
- 旧记录显示第 33—35 轮主动拼写首答正确率约 42%。
- 需要从“背词义”和“重复单一语法结构”升级到：

词性判断 → 常见搭配 → 句型位置 → 动词形式 → 主动输出。

## 错误类型定义

| 错误类型 | 含义 | 当前例子 |
|---|---|---|
| `verb_identity_confusion` | 不能判断某词是否为动词 | `be increase / be decrease` |
| `verb_form_error` | 动词形式变化不熟 | `Success depend on...` |
| `collocation_error` | 固定搭配错误 | `depend on`、`keep/enjoy + doing` 待复现 |
| `output_instability` | 会认词但不会稳定造句 | 词义知道但造句不稳 |
| `spelling_instability` | 中文到英文主动拼写不稳 | `achieve → acheive`、`government → gavermant` |
| `confusing_words` | 易混词辨析不稳 | `properly / probably`、`receive / accept` |

## 雷达分类

### A. 当前重点复现词

| 词/短语 | 词性 | 当前问题 | 复现优先级 | 来源 |
|---|---|---|---|---|
| increase | v./n. | 中文意思知道，但动词身份识别不稳；误写 `be increase` | 最高 | Day4 真实错题 |
| decrease | v./n. | 中文意思知道，但动词身份识别不稳；误写 `be decrease` | 最高 | Day4 真实错题 |
| depend on | phr. v. | 主谓一致和三单形式不稳 | 高 | Day3 真实错题 |
| discover | v. | 已学习，需进入造句系统 | 中 | Day3 英语副课 |
| especially | adv. | 已学习，需进入句子位置训练 | 中 | Day3 英语副课 |

### B. 不熟词：优先回炉

来自旧英语资料 A 级词。状态为“历史反复出错”，不是新近课堂错题。

`reduce`、`remain`、`properly`、`purpose`、`image`、`realize`、`replace`、`compare`、`refuse`、`mental`、`shock`、`condition`、`amusement`、`available`、`research`、`destroy`、`defeat`、`performance`、`preparations`、`excitement`

### C. 词性不清的词

| 词 | 当前判断 | 处理方式 |
|---|---|---|
| increase | 动词身份识别不稳 | 每次复现必须判断词性并造句 |
| decrease | 动词身份识别不稳 | 每次复现必须判断词性并造句 |
| produce / product | 动词与名词易混 | 成对辨析 |
| record | 名词/动词均可，需看句子位置 | 放入句中判断 |
| support | 可作动词/名词，需看句子位置 | 放入句中判断 |
| research | 可作名词/动词，需看句子位置 | 放入句中判断 |

### D. 会认不会用的词

| 词/短语 | 问题 | 训练方式 |
|---|---|---|
| depend on | 会认，但三单输出不稳 | 主语替换造句 |
| discover | 会认，需主动造句 | 过去式、一般现在时造句 |
| especially | 会认，需掌握句中位置 | 句子扩写 |
| available | 会认，拼写和语境不稳 | 情景造句 |
| purpose | 会认，主动回忆不稳 | 固定句型 `The purpose of... is...` |

### E. 搭配不熟的词/结构

| 搭配 | 当前依据 | 训练方式 |
|---|---|---|
| depend on | Day3 真实错题 | 主谓一致 + 完整句输出 |
| keep/enjoy + doing | 旧资料语法薄弱点 | 改错 + 造句 |
| be interested in doing | 旧资料语法薄弱点 | 句型替换 |
| spend money/time doing | 旧资料语法薄弱点 | 汉译英 |
| Thank you for doing | 旧资料句型薄弱点 | 情景表达 |

### F. 需要复现的易混词

`receive / accept`、`accept / except`、`properly / probably`、`reduce / record`、`condition / confidence`、`product / produce`、`correct / continue`、`invitation / invention`、`course / of course`、`remove / replace`、`satisfaction / situation`、`purpose / certainly`、`rapid / repair`、`record / repeat`、`brave / courage / encourage`

## 每个雷达词的训练四件套

每个重点词必须训练：

1. 词性：它在句子中是什么身份？
2. 中文意思：这个意思是否适合当前语境？
3. 常见句型/搭配：它通常和哪些词一起出现？
4. 自主造句：能不能脱离提示写出正确句子？

## Day6 以后英语教材固定要求

每天至少安排一个 Lexical Radar 小栏目。

栏目内容必须包含：

- 今日雷达词 3～5 个；
- 判断词性；
- 造句；
- 改错；
- 汉译英；
- 至少 1 题来自 `english/error_bank.md` 的真实错题变式；
- 至少 1 题来自 `english/word_bank.md` 的旧词复现。

## 当前教学判断

茄子的英语问题不能只按“语法点没学会”处理。

更准确的教学路径是：

词汇身份识别 → 句子结构判断 → 动词形式变化 → 主动输出稳定。

因此，英语课从 Day6 开始应把词汇、语法、阅读、翻译和写作合并训练，而不是孤立背单词。
