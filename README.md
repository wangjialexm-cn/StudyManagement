# 茄子学习系统

## 系统简介

茄子学习系统是一个面向初升高阶段的个人学习管理项目，用于持续记录学生能力画像、真实课堂反馈、错题根因、复习计划和每日课程材料。

系统当前处于 v2.0 阶段，核心方法是“原因驱动教学”：先判断学生当前能力状态和 Root Cause，再生成教材、练习、作业和教师指导，而不是简单围绕错题重复刷题。

## 项目目标

1. 建立长期可追踪的学生能力模型。
2. 让数学、英语、物理、化学课程按高中衔接节奏系统推进。
3. 通过真实课堂、批改和复测不断校正 Root Cause。
4. 形成可复用的每日课程包：Student Book、Class Practice、Homework、Teacher Guide、Answer。
5. 保持项目资料可在新电脑、新会话中快速恢复上下文。

## ChatGPT 与 Codex 分工

### ChatGPT

- 负责教学判断、课堂讲授、教研审核和学习结果判断。
- 根据真实课堂表现、批改结果和学生回答更新能力判断。
- 审核 Codex 生成的教材是否符合教学节奏和学生当前能力。
- 决定下一步教学任务，并确认是否允许生成最终版材料。

### Codex

- 负责读取项目上下文、整理文件、生成教材草稿和维护项目结构。
- 根据 ChatGPT 确认的任务生成 Markdown 审核稿。
- 在审核通过后生成正式课程包和归档材料。
- 维护 Git 提交，确保项目可以持续同步和恢复。

## Git 工作流程

1. 每次开始工作前先读取 `PROJECT_CONTEXT.md` 和 `WORKING_STATUS.md`。
2. 修改前确认当前任务范围，不改动无关文件。
3. 教材生成遵循 `system/Teaching_Standard.md`。
4. 未经 ChatGPT 审核通过，不生成最终 PDF 或打印版。
5. 每次完成一个明确任务后提交 Git。
6. Commit message 使用简短英文，说明本次变更目的。
7. 推送到 GitHub 后，项目在其他电脑可通过拉取仓库恢复。

## 新电脑如何恢复项目

1. 安装 Git。
2. 克隆 GitHub 仓库到本地。
3. 进入项目目录。
4. 优先阅读：
   - `PROJECT_CONTEXT.md`
   - `WORKING_STATUS.md`
   - `system/Teaching_System.md`
   - `system/Teaching_Standard.md`
   - `茄子学习档案/ability_profile.md`
5. 确认 `daily/` 中最新 Day 目录。
6. 根据 `WORKING_STATUS.md` 接续下一步任务。

