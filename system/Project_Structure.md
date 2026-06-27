# 茄子学习系统 v2.0｜Project Structure

> 架构状态：v2.0 已于 2026-06-25 冻结。除重大问题外，不再调整目录和核心规范；后续优化统一记录到 `Teaching_Log.md`。

## 顶层目录

```text
家庭教师/
├── system/
├── templates/
├── materials/
├── daily/
├── archive/
└── 茄子学习档案/
```

## system/

保存项目最高规范。

- `Master_Prompt.md`：项目总规范
- `Teaching_System.md`：教学、课堂、批改、互动规则
- `Material_Standard.md`：教材与练习材料标准
- `Ability_Framework.md`：L1~L10 能力体系
- `Project_Structure.md`：项目目录规范
- `Curriculum.md`：初升高到高考三年课程地图

## templates/

保存统一模板。

- `Student_Book_Template.docx`
- `Class_Practice_Template.docx`
- `Homework_Template.docx`
- `Teacher_Guide_Template.docx`
- `Learning_Record_Template.md`

## materials/

保存正式教材与训练材料。

建议结构：

```text
materials/
└── bridge/
    ├── day01/
    ├── day02/
    └── dayXX/
```

每一天固定包含：

- 学生教材
- 课堂练习
- 课后训练卷
- 教师答案

## daily/

保存每日真实课堂归档。

建议结构：

```text
daily/
└── YYYY-MM-DD/
    ├── 课堂记录.md
    ├── 教材/
    ├── 训练卷/
    ├── 批改/
    └── 学习总结.md
```

## 茄子学习档案/

保存长期核心档案。

- `student_profile.md`
- `ability_profile.md`
- `learning_record.md`
- `mistakes.md`
- `weekly_plan.md`
- `exam_records.md`
- `handover_report.md`

## archive/

保存历史备份，不删除旧文件。

- `v1_legacy/`：v1.0 编号档案历史备份
