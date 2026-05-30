# WorkBuddy Skills 仓库

本仓库收录由 Hermes Agent 创建、适用于 [WorkBuddy](https://www.workbuddy.ai) 的原创 AI 技能包（Skills）。

WorkBuddy 是一个强大的 AI 编程助手，支持通过 SKILL.md 格式扩展能力。本仓库中的所有 Skills 均标记了 `agent_created: true`，由 AI 自主创建并持续迭代维护。

---

## 仓库结构

```
workbuddy-skills/
├── skills/                                # 技能包目录
│   ├── academic-conference-paper-writer/  # 学术年会论文写作助手
│   ├── academic-paper-writer/             # 通用学术论文写作助手
│   ├── backup-skills-to-github/           # Skills 备份工具
│   ├── edu-research-paper/                # 教学科研论文写作辅助
│   ├── paperyy-aigc-rewrite/              # PaperYY AIGC 降重改写
│   └── project-softcopyright-generator/   # 软件著作权材料生成
└── docs/                                  # 文档目录
```

---

## 已收录 Skills

| Skill 名称 | 说明 | 触发关键词 |
|-----------|------|-----------|
| **academic-conference-paper-writer** | 学术年会论文全流程写作助手。基于目标报告文集风格规范自动完成选题→资料搜索→论文生成→图表匹配→文档排版→迭代修改 | 学术年会、会议论文、报告文集 |
| **academic-paper-writer** | 通用学术论文全流程写作助手。支持工程/教育/社科/管理/医学/计算机等学科，覆盖选题分析、文献检索、大纲设计、逐章生成、Word 排版输出 | 学术论文、期刊投稿、研究报告、选题推荐 |
| **backup-skills-to-github** | 自动扫描并备份 `agent_created: true` 的原创 Skills 到 GitHub 仓库，通过 GitHub API 上传所有文件 | 备份 skills、上传到 github、sync skills |
| **edu-research-paper** | 教学科研论文撰写辅助。面向中小学教师及高校教师，覆盖课题研究报告、期刊投稿论文、结题报告等常见类型 | 教学科研论文、教育科研、选题怎么定、文献综述 |
| **paperyy-aigc-rewrite** | PaperYY 平台 AIGC 检测降重改写工具。系统性人工化改写，将 AIGC 疑似率控制在 14%~16%，保留研究框架与学术术语 | AIGC降重、去AI痕迹、PaperYY、论文改写 |
| **project-softcopyright-generator** | 软件著作权登记材料生成器。读取本地项目代码，自动分析项目结构、功能模块、技术架构，生成软著申请所需的说明资料与源代码文档 | 软著、软件著作权、著作权登记、版权登记 |

---

## 使用方法

### 安装 Skill 到 WorkBuddy

1. 打开 WorkBuddy 设置 → Skills 管理
2. 选择「从文件夹安装」
3. 选择本仓库中对应 skill 的子目录（如 `skills/academic-paper-writer/`）
4. 确认安装

### 直接从本仓库安装（推荐）

```bash
# 克隆仓库到 WorkBuddy skills 目录
git clone https://github.com/FooFieYoon/workbuddy-skills.git ~/.workbuddy/skills/
```

---

## 技术要求

- WorkBuddy 版本：最新版
- 运行环境：支持 Python 3.x（部分 Skills 需要）
- 适用语言：中文（简体）

---

## 贡献

本仓库由 Hermes Agent 自动维护。如需贡献新的 Skill，请：

1. Fork 本仓库
2. 在 `skills/` 目录下创建新的 Skill 文件夹
3. 确保 SKILL.md 中包含 `agent_created: true` 标记
4. 提交 Pull Request

---

## 许可证

本仓库中的 Skills 采用 [MIT 许可证](LICENSE) 开源。

---

## 关于

- **维护者**：Hermes Agent
- **所属项目**：WorkBuddy AI 助手
- **仓库地址**：[github.com/FooFieYoon/workbuddy-skills](https://github.com/FooFieYoon/workbuddy-skills)
- **问题反馈**：请在 GitHub Issues 中提交

---

*由 Hermes Agent 自动生成并维护 🤖*
