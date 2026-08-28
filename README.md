# skill-test

技能测试项目，用于验证自定义 Skill 的编写与加载流程。

## 目录结构

```
skill-test/
├── readme.md              # 项目说明
└── skills/
    └── hello/             # 示例技能
        └── SKILL.md       # 技能定义文件
```

## 技能规范

一个有效的 Skill 包含：

- 一个目录：`skills/<skill-name>/`
- 一个文件：`SKILL.md`

`SKILL.md` 使用如下格式：

```markdown
---
name: "<skill-name>"
description: "<做什么 + 何时触发，200 字符以内>"
---

# 技能标题

详细说明与使用指南。
```

## 现有技能

| 技能名 | 说明 |
| ------ | ---- |
| hello  | 简单问候示例技能 |
