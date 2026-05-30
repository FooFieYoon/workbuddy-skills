# 在主流 AI 工具中使用这些 Skills

> **Author: Yin**  
> 本指南介绍如何将仓库中的 WorkBuddy Skills 迁移或适配到 Cursor、VS Code + Continue、Claude Desktop、Cherry Studio、Open WebUI 等主流 AI 工具中使用。

---

## 目录

- [前置说明](#前置说明)
- [WorkBuddy（原生）](#workbuddy原生)
- [Cursor — Rules & Prompt Files](#cursor--rules--prompt-files)
- [VS Code + Continue](#vs-code--continue)
- [Claude Desktop — Custom Instructions](#claude-desktop--custom-instructions)
- [Cherry Studio — System Prompts](#cherry-studio--system-prompts)
- [Open WebUI — Modelfiles / System Prompts](#open-webui--modelfiles--system-prompts)
- [通用适配原则](#通用适配原则)
- [快速对照表](#快速对照表)

---

## 前置说明

本仓库中的 Skills 原生格式为 WorkBuddy `SKILL.md`，核心包含：

1. **YAML Frontmatter** — 元数据（名称、描述、触发条件）
2. **Workflow 正文** — 分步工作流程（Markdown）
3. **References** — 可引用的辅助文档

迁移到其他工具时，**核心内容（工作流程正文）可直接复用**，只需按各工具格式调整封装方式。

---

## WorkBuddy（原生）

> 零配置，直接安装即用。

```bash
# 克隆整个仓库
git clone https://github.com/FooFieYoon/workbuddy-skills.git

# 安装某个 Skill（用户级，所有项目可用）
cp -r workbuddy-skills/skills/<skill-name> ~/.workbuddy/skills/

# 安装到当前项目（项目级）
cp -r workbuddy-skills/skills/<skill-name> .workbuddy/skills/
```

重启 WorkBuddy 后，直接用自然语言触发，例如：
- `"写一篇学术年会论文"`
- `"降低这篇论文的 AIGC 检测率"`

---

## Cursor — Rules & Prompt Files

Cursor 使用 `.cursorrules`（全局规则）或 `.cursor/rules/*.mdc`（项目级规则）来注入系统提示。

### 步骤

**1. 提取 Skill 的工作流程内容**

打开对应 `SKILL.md`，复制 YAML frontmatter 以下的正文部分（即 `---` 之后的 Markdown 内容）。

**2. 创建 Cursor Rules 文件**

```bash
# 项目级（推荐）
mkdir -p .cursor/rules
```

新建文件 `.cursor/rules/<skill-name>.mdc`，内容格式：

```markdown
---
description: 学术年会论文全流程写作助手
globs: ["**/*.md", "**/*.tex", "**/*.docx"]
alwaysApply: false
---

# 学术年会论文写作助手

当用户请求写学术年会论文时，按以下流程执行：

[在此粘贴 SKILL.md 的正文内容]
```

**3. 触发方式**

在 Cursor Chat 中按 `@Rules` 引用，或在 `alwaysApply: true` 时自动加载。

### 示例 — academic-paper-writer

```bash
# 将 SKILL.md 正文转为 Cursor Rule
cat skills/academic-paper-writer/SKILL.md | sed '1,/^---$/d; 1,/^---$/d'
```

复制输出，粘贴到 `.cursor/rules/academic-paper-writer.mdc`。

---

## VS Code + Continue

[Continue](https://continue.dev) 是 VS Code 的 AI 编程助手插件，支持自定义 Prompt Slash Commands。

### 步骤

**1. 打开 Continue 配置文件**

```
~/.continue/config.json
```

**2. 添加 Slash Commands**

```json
{
  "slashCommands": [
    {
      "name": "write-paper",
      "description": "学术论文全流程写作助手",
      "prompt": "[在此粘贴 SKILL.md 工作流正文]"
    },
    {
      "name": "reduce-aigc",
      "description": "降低 AIGC 检测率 / 论文人工化改写",
      "prompt": "[在此粘贴 paperyy-aigc-rewrite SKILL.md 正文]"
    }
  ]
}
```

**3. 触发方式**

在 Continue Chat 中输入 `/write-paper` 或 `/reduce-aigc` 即可触发。

### 备注

- Continue 也支持 `.prompt` 文件（存放在 `~/.continue/prompts/`），格式更灵活，可引用本地文件。
- 参考：https://docs.continue.dev/customization/slash-commands

---

## Claude Desktop — Custom Instructions

Claude Desktop 支持通过 **Custom Instructions（自定义指令）** 注入持久化系统提示。

### 步骤

**1. 打开设置**

`Claude Desktop → Settings → Custom Instructions`

**2. 粘贴 Skill 内容**

将 `SKILL.md` 的工作流正文（去掉 YAML frontmatter）粘贴到 Custom Instructions 文本框中。

建议格式：

```
## 学术论文写作模式

当我请求写论文时，请严格按以下流程执行：

[SKILL.md 正文内容]

---

## AIGC 检测降重模式

当我请求降低 AIGC 检测率时：

[paperyy-aigc-rewrite SKILL.md 正文内容]
```

**3. 触发方式**

在对话中直接说 `"帮我写一篇关于XXX的学术论文"` 即可。

### 备注

- Custom Instructions 字数有限制（约 1500 词），建议只保留最常用的 1-2 个 Skill。
- 可以用 Projects 功能为不同项目分别配置不同的 Skill 指令。

---

## Cherry Studio — System Prompts

[Cherry Studio](https://cherry-ai.com) 是国内主流 AI 桌面客户端，支持为每个对话或助手配置 System Prompt。

### 步骤

**1. 创建新助手**

`Cherry Studio → 助手 → 新建助手 → 配置 System Prompt`

**2. 粘贴 Skill 内容**

```
你是一个学术论文写作助手。

[粘贴 academic-paper-writer SKILL.md 正文]
```

**3. 触发方式**

选中该助手后，直接输入写作需求即可。

### 推荐配置方案

为每个 Skill 创建一个专属助手：

| 助手名称 | 对应 Skill |
|---|---|
| 学术论文助手 | `academic-paper-writer` |
| 年会论文助手 | `academic-conference-paper-writer` |
| 教学科研论文助手 | `edu-research-paper` |
| AIGC 降重助手 | `paperyy-aigc-rewrite` |

---

## Open WebUI — Modelfiles / System Prompts

[Open WebUI](https://openwebui.com) 支持通过 **Models**（自定义模型配置）注入 System Prompt。

### 方式一：通过界面配置

1. `Open WebUI → 管理后台 → 模型 → 新建模型`
2. 填写名称（如 `academic-paper-assistant`）
3. 在 **System Prompt** 字段中粘贴 SKILL.md 正文
4. 保存后选用该模型即可

### 方式二：Modelfile（Ollama 模型）

如果使用 Ollama 本地模型，可通过 Modelfile 注入：

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

## 通用适配原则

无论哪个工具，适配步骤都遵循相同逻辑：

```
SKILL.md 正文
    ↓
去掉 YAML frontmatter（--- 到 --- 之间的部分）
    ↓
保留 Markdown 工作流正文
    ↓
按目标工具格式封装（Rules / Slash Command / System Prompt）
    ↓
配置触发条件（关键词 / 命令 / 按需选择）
```

### 提取 SKILL.md 正文的快捷方式

```bash
# Linux / macOS / Git Bash
skill="academic-paper-writer"
awk '/^---$/{n++;next} n>=2' skills/$skill/SKILL.md

# PowerShell
$skill = "academic-paper-writer"
$content = Get-Content "skills/$skill/SKILL.md" -Raw
$content -replace '^---[\s\S]*?---\n', ''
```

---

## 快速对照表

| 工具 | 配置文件/位置 | 格式 | 自动触发 | 备注 |
|---|---|---|---|---|
| **WorkBuddy** | `~/.workbuddy/skills/` | `SKILL.md` | ✅ 自然语言触发 | 原生格式，零配置 |
| **Cursor** | `.cursor/rules/*.mdc` | MDC + Markdown | ⚠️ 需 `@Rules` 引用或设 `alwaysApply` | 支持 glob 过滤 |
| **VS Code + Continue** | `~/.continue/config.json` | JSON Slash Command | ✅ `/命令名` 触发 | 支持 `.prompt` 文件 |
| **Claude Desktop** | Settings → Custom Instructions | 纯文本 Markdown | ✅ 对话中自然触发 | 字数有限制 |
| **Cherry Studio** | 助手 → System Prompt | 纯文本 Markdown | ✅ 选择助手后自动 | 支持多助手切换 |
| **Open WebUI** | 模型 → System Prompt | 纯文本 Markdown | ✅ 选择模型后自动 | 支持 Modelfile |

---

## 参考资料

- [WorkBuddy Skills 文档](https://www.workbuddy.ai/docs/skills)
- [Cursor Rules 文档](https://docs.cursor.com/context/rules-for-ai)
- [Continue Slash Commands 文档](https://docs.continue.dev/customization/slash-commands)
- [Open WebUI 文档](https://docs.openwebui.com)
- [Cherry Studio 官网](https://cherry-ai.com)

---

*By Yin · Updated: 2026-05-30*
