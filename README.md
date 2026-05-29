# WorkBuddy Skills Backup

本仓库备份 WorkBuddy AI 助手的**原创 Skills**（`agent_created: true`），可直接导入使用。

## 包含的 Skills

| Skill 名称 | 功能说明 | 适用场景 |
|---|---|---|
| `academic-conference-paper-writer` | 学术年会论文全流程写作助手 | 年会报告、会议论文 |
| `academic-paper-writer` | 通用学术论文全流程写作助手 | 期刊论文、学位论文 |
| `edu-research-paper` | 教学科研论文撰写辅助 | 教育科研论文、结题报告 |
| `paperyy-aigc-rewrite` | PaperYY AIGC 检测降重改写工具 | AIGC 率降低、论文人工化改写 |

## 安装方法

将需要的 skill 目录复制到 WorkBuddy 的 skills 目录：

```bash
# 用户级安装（所有项目可用）
cp -r skills/<skill-name> ~/.workbuddy/skills/

# 项目级安装（仅当前项目）
cp -r skills/<skill-name> <project-root>/.workbuddy/skills/
```

安装后重启 WorkBuddy 即可使用。

## 每个 Skill 的结构

```
skills/
└── <skill-name>/
    ├── SKILL.md          # 核心文件，定义 skill 的触发词、工作流程
    ├── references/       # 参考资料（可选）
    ├── scripts/          # 辅助脚本（可选）
    └── assets/           # 资源文件（可选）
```

## 触发示例

| 用户说 | 触发 Skill |
|---|---|
| "写一篇学术会议论文" | `academic-conference-paper-writer` |
| "帮我写论文" | `academic-paper-writer` |
| "写教学科研论文" | `edu-research-paper` |
| "降低 AIGC 检测率" | `paperyy-aigc-rewrite` |

## 关于 WorkBuddy

WorkBuddy 是一个强大的 AI 编程助手，支持通过 Skills 扩展能力。每个 Skill 是一个独立的能力模块，包含触发条件、工作流程和参考资料。

- 官网：https://www.workbuddy.ai
- Skills 文档：https://www.workbuddy.ai/docs/skills

## 贡献

这些是原创 Skill，如果你有改进建议，欢迎提 Issue 或 PR。

---
*由 WorkBuddy 自动备份 · 最后更新：2026-05-30*
