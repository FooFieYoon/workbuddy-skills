# Skills 备份仓库

> **作者：Yin**  
> 本仓库由 Yin 维护，存放 WorkBuddy AI 助手的原创 Skills（`agent_created: true`）。

---

## 关于作者

- **Author**: Yin
- **GitHub**: [@FooFieYoon](https://github.com/FooFieYoon)
- **说明**: 本仓库中的所有 Skills 均由 Yin 原创编写，`agent_created: true` 标识表明这些 Skills 由 AI Agent 在 Yin 的指导下自动创建和维护。

---

## 包含的 Skills

| Skill 名称 | 功能说明 | 适用场景 |
|---|---|---|
| `academic-conference-paper-writer` | 学术年会论文全流程写作助手 | 年会报告、会议论文 |
| `academic-paper-writer` | 通用学术论文全流程写作助手 | 期刊论文、学位论文 |
| `edu-research-paper` | 教学科研论文撰写辅助 | 教育科研论文、结题报告 |
| `paperyy-aigc-rewrite` | PaperYY AIGC 检测降重改写工具 | AIGC 率降低、论文人工化改写 |
| `backup-skills-to-github` | 备份 Skills 到 GitHub（通用型 Skill） | "备份我的 skills" |

---

## 仓库目录结构

```
workbuddy-skills/
├── README.md          ← 本文件
├── docs/
│   └── tools-guide.md ← 主流工具详细使用指南
└── skills/            ← 所有 Skill 存放目录
    ├── academic-conference-paper-writer/
    ├── academic-paper-writer/
    ├── edu-research-paper/
    ├── paperyy-aigc-rewrite/
    └── backup-skills-to-github/
        ├── SKILL.md
        ├── scripts/
        └── references/
```

---

## 安装方法

### WorkBuddy（原生支持，推荐）

将需要的 Skill 目录复制到 WorkBuddy 的 Skills 目录：

```bash
# 克隆仓库
git clone https://github.com/FooFieYoon/workbuddy-skills.git

# 用户级安装（所有项目可用）
cp -r workbuddy-skills/skills/<skill-name> ~/.workbuddy/skills/

# 项目级安装（仅当前项目）
cp -r workbuddy-skills/skills/<skill-name> <project-root>/.workbuddy/skills/
```

重启 WorkBuddy 后，直接用自然语言触发即可。

---

### Cursor

将 Skill 工作流内容转为 Cursor Rules 文件：

```bash
# 1. 在项目根目录创建 rules 文件夹
mkdir -p .cursor/rules

# 2. 提取 SKILL.md 工作流正文（去掉 YAML frontmatter）
skill="academic-paper-writer"
awk '/^---$/{n++;next} n>=2' workbuddy-skills/skills/$skill/SKILL.md > .cursor/rules/$skill.mdc
```

或手动新建 `.cursor/rules/<skill-name>.mdc`，格式如下：

```markdown
---
description: 学术论文全流程写作助手
alwaysApply: false
---

[粘贴 SKILL.md 的正文内容（--- 以下部分）]
```

**触发方式**：在 Cursor Chat 中按 `@Rules` 引用，或将 `alwaysApply` 改为 `true` 自动加载。

---

### VS Code + Continue

编辑 `~/.continue/config.json`，添加 Slash Commands：

```json
{
  "slashCommands": [
    {
      "name": "write-paper",
      "description": "学术论文全流程写作助手",
      "prompt": "[粘贴 academic-paper-writer SKILL.md 正文]"
    },
    {
      "name": "reduce-aigc",
      "description": "降低 AIGC 检测率 / 论文人工化改写",
      "prompt": "[粘贴 paperyy-aigc-rewrite SKILL.md 正文]"
    },
    {
      "name": "edu-paper",
      "description": "教学科研论文撰写助手",
      "prompt": "[粘贴 edu-research-paper SKILL.md 正文]"
    }
  ]
}
```

**触发方式**：在 Continue Chat 中输入 `/write-paper`、`/reduce-aigc` 等命令。

---

### Claude Desktop

1. 打开 `Claude Desktop → Settings → Custom Instructions`
2. 将 SKILL.md 工作流正文（去掉 YAML frontmatter）粘贴进去

建议格式（可同时配置多个 Skill）：

```
## 学术论文写作模式
当我请求写论文时，请按以下流程执行：
[academic-paper-writer SKILL.md 正文]

---

## AIGC 降重模式
当我请求降低 AIGC 检测率时：
[paperyy-aigc-rewrite SKILL.md 正文]
```

> **提示**：Custom Instructions 有字数限制（约 1500 词），建议只保留最常用的 1~2 个 Skill；也可利用 Projects 功能为不同项目分别配置。

---

### Cherry Studio

1. `Cherry Studio → 助手 → 新建助手`
2. 在 **System Prompt** 字段中粘贴 SKILL.md 正文内容
3. 为每个 Skill 创建一个专属助手（推荐）

| 助手名称 | 对应 Skill |
|---|---|
| 学术论文助手 | `academic-paper-writer` |
| 年会论文助手 | `academic-conference-paper-writer` |
| 教学科研论文助手 | `edu-research-paper` |
| AIGC 降重助手 | `paperyy-aigc-rewrite` |

**触发方式**：选中对应助手后，直接输入需求即可。

---

### Open WebUI

**方式一：界面配置**

1. `Open WebUI → 管理后台 → 模型 → 新建模型`
2. 填写名称（如 `academic-paper-assistant`）
3. 在 **System Prompt** 字段中粘贴 SKILL.md 正文
4. 保存后选用该模型即可

**方式二：Ollama Modelfile**

```dockerfile
FROM llama3

SYSTEM """
你是一个学术论文写作助手。

[粘贴 academic-paper-writer SKILL.md 正文]
"""
```

```bash
ollama create academic-writer -f Modelfile
ollama run academic-writer
```

---

### 通用提取命令

从 `SKILL.md` 中提取正文（去掉 YAML frontmatter）：

```bash
# Linux / macOS / Git Bash
skill="academic-paper-writer"
awk '/^---$/{n++;next} n>=2' skills/$skill/SKILL.md

# PowerShell
$skill = "academic-paper-writer"
$lines = Get-Content "skills/$skill/SKILL.md"
$start = ($lines | Select-String -Pattern '^---$').LineNumber[1]
$lines[$start..($lines.Length-1)] -join "`n"
```

---

## 每个 Skill 的结构

```
skills/
└── <skill-name>/
    ├── SKILL.md          # 核心文件，定义 Skill 的触发词、工作流程
    ├── references/       # 参考资料（可选）
    ├── scripts/          # 辅助脚本（可选）
    └── assets/           # 资源文件（可选）
```

---

## 触发示例

| 用户说 | 触发 Skill |
|---|---|
| "写一篇学术会议论文" | `academic-conference-paper-writer` |
| "帮我写论文" | `academic-paper-writer` |
| "写教学科研论文" | `edu-research-paper` |
| "降低 AIGC 检测率" | `paperyy-aigc-rewrite` |
| "备份我的 skills 到 github" | `backup-skills-to-github` |

---

## 主流工具快速对照表

| 工具 | 配置文件 / 位置 | 触发方式 | 备注 |
|---|---|---|---|
| **WorkBuddy** | `~/.workbuddy/skills/<name>/` | 自然语言自动触发 | 原生格式，零配置 |
| **Cursor** | `.cursor/rules/<name>.mdc` | `@Rules` 引用 或 `alwaysApply: true` | 支持 glob 文件过滤 |
| **VS Code + Continue** | `~/.continue/config.json` | `/命令名` | 支持 `.prompt` 文件 |
| **Claude Desktop** | Settings → Custom Instructions | 对话中自然触发 | 字数约 1500 词限制 |
| **Cherry Studio** | 助手 → System Prompt | 选择助手后自动 | 推荐每个 Skill 建一个助手 |
| **Open WebUI** | 模型 → System Prompt | 选择模型后自动 | 也支持 Ollama Modelfile |

📖 **详细使用指南** → [docs/tools-guide.md](./docs/tools-guide.md)

---

## 关于 WorkBuddy

WorkBuddy 是一个强大的 AI 编程助手，支持通过 Skills 扩展能力。每个 Skill 是一个独立的能力模块，包含触发条件、工作流程和参考资料。

- 官网：https://www.workbuddy.ai
- Skills 文档：https://www.workbuddy.ai/docs/skills

---

## `backup-skills-to-github` Skill 使用说明

该 Skill 由 Yin 原创，用于自动备份 WorkBuddy 原创 Skills 到 GitHub。

**触发词**："备份我的 skills"、"上传 skills 到 github"、"backup my skills"

**工作流程**：
1. 扫描本地 `~/.workbuddy/skills/` 中所有 `agent_created: true` 的原创 Skill
2. 检查 GitHub 认证状态，必要时引导用户登录
3. 创建或更新 `workbuddy-skills` 仓库
4. 通过 GitHub REST API 上传所有文件（绕过 Windows git 问题）
5. 优化仓库目录结构（使用 `skills/` 子目录）
6. 自动生成并更新 README.md

---

## 版权与许可

- **作者**: Yin
- **Copyright**: © 2026 Yin. All rights reserved.
- **License**: MIT License（允许自由使用、修改和分发）
- **说明**: 本仓库中的 Skills 为原创作品，欢迎学习和改进，请注明出处。

---

## 贡献

欢迎提交 Issue 或 Pull Request 改进这些 Skills。

---

*由 Yin 维护 · 最后更新：2026-05-30*
