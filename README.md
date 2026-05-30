# WorkBuddy Skills

> 收录由 Hermes Agent 创建、为 [WorkBuddy](https://www.workbuddy.ai) 优化的原创 AI 技能包（Skills）。每个 Skill 均为独立的 SKILL.md 文件，可在 WorkBuddy 中原生使用，也可迁移至 Cursor、Claude Desktop 等主流 AI 工具——详见 [`docs/tools-guide.md`](docs/tools-guide.md)。

---

## 仓库目录

```
workbuddy-skills/
├── README.md
├── docs/
│   └── tools-guide.md                         # 多平台迁移指南
└── skills/
    ├── academic-conference-paper-writer/       # 学术年会论文写作
    │   └── SKILL.md
    ├── academic-paper-writer/                  # 通用学术论文写作
    │   ├── SKILL.md
    │   └── references/                         # 写作风格/论文结构/引用格式
    │       ├── citation-formats.md
    │       ├── default-style-guide.md
    │       ├── paper-structures.md
    │       └── writing-style.md
    ├── backup-skills-to-github/                # Skills 备份与同步
    │   ├── SKILL.md
    │   ├── assets/
    │   ├── references/
    │   │   ├── api_reference.md
    │   │   └── github_api_notes.md
    │   └── scripts/
    │       ├── backup_skills.py                # 核心备份脚本
    │       ├── scan_skills.py                  # 技能扫描
    │       ├── optimize_layout.py              # 布局优化
    │       └── example.py
    ├── edu-research-paper/                     # 教学科研论文撰写
    │   └── SKILL.md
    ├── paperyy-aigc-rewrite/                   # AIGC 检测降重改写
    │   ├── SKILL.md
    │   ├── references/
    │   │   ├── aigc_detection_rules.md         # AIGC 检测规则参考
    │   │   └── rewrite_examples.md             # 改写示例
    │   └── scripts/
    │       └── rewrite_docx.py                 # docx 改写核心脚本
    └── project-softcopyright-generator/        # 软件著作权材料生成
        ├── SKILL.md
        ├── references/
        │   ├── application-fields.md            # 申请领域参考
        │   └── design-spec.md                   # 设计规范
        └── templates/                           # 生成模板
            ├── run-project-softcopyright-generator-template.py
            ├── generate-application-info-template.py
            ├── generate-source-template.py
            ├── generate-doc-template.py
            ├── propose-code-selection-template.py
            └── render-print-docx-template.py
```

---

## 已收录 Skills（6 个）

### 1. `academic-conference-paper-writer` — 学术年会论文全流程写作助手

基于目标报告文集的风格规范（通过 PDF 样本分析自动提取），从会议通知材料出发自动完成：选题推荐 → 资料搜索 → 论文生成 → 图表匹配 → 文档排版 → 迭代修改。

| 项目 | 内容 |
|------|------|
| 适用场景 | 学术年会论文、会议报告文集投稿 |
| 触发短语 | "学术年会论文"、"会议报告"、"按会议模板写论文" |
| 核心能力 | PDF 风格提取、选题推荐、自动排版 |

---

### 2. `academic-paper-writer` — 通用学术论文全流程写作助手

支持任意学科领域（工程、教育、社科、管理、医学、计算机等）的学术期刊论文、会议论文、研究报告端到端写作。

| 项目 | 内容 |
|------|------|
| 适用场景 | 期刊投稿、学位论文、研究报告 |
| 触发短语 | "写学术论文"、"投稿期刊"、"文献综述"、"论文选题" |
| 核心能力 | 选题分析、文献检索、大纲设计、逐章生成、Word 排版输出 |
| 附加资料 | 4 份参考文献（写作风格、论文结构、引用格式、默认风格指南） |

---

### 3. `edu-research-paper` — 教学科研论文撰写辅助

面向中小学及高校教师、教育科研工作者，覆盖课题研究报告、期刊投稿论文、结题报告等常见教学科研文体。

| 项目 | 内容 |
|------|------|
| 适用场景 | 教学科研论文、课题研究报告、结题报告 |
| 触发短语 | "教育科研论文"、"课题研究"、"研究方法怎么写"、"论文图表规范" |
| 核心能力 | 选题框架、文献综述、研究方法、图表规范、先文后图表 |

---

### 4. `paperyy-aigc-rewrite` — PaperYY AIGC 检测降重改写

针对 PaperYY 平台 AIGC 检测规则对学术论文进行系统性人工化改写，将 AIGC 疑似率控制在 14%~16% 目标值，同时保留原文的研究框架、数据、参考文献和学术术语。

| 项目 | 内容 |
|------|------|
| 适用场景 | 学术论文 AIGC 降重、学位论文去 AI 痕迹 |
| 触发短语 | "AIGC降重"、"去除AI痕迹"、"论文人工化改写"、"PaperYY 查重" |
| 核心能力 | 结构打散、叙事注入、口语化重写、docx 格式保留输出 |
| 附加资料 | AIGC 检测规则参考、改写示例、Python 改写脚本 |

---

### 5. `project-softcopyright-generator` — 软件著作权登记材料生成器

读取本地项目代码，自动分析项目结构、功能模块、技术架构，生成适合中国计算机软件著作权登记使用的全套申报材料。

| 项目 | 内容 |
|------|------|
| 适用场景 | 软件著作权登记、版权申报材料 |
| 触发短语 | "软著"、"软件著作权"、"版权登记"、"生成软著材料" |
| 核心能力 | 代码分析、模块梳理、申请信息生成、源程序文档生成 |
| 附加资料 | 6 个 Python 模板脚本、申请领域参考、设计规范文档 |

---

### 6. `backup-skills-to-github` — Skills 备份与同步工具

自动扫描所有 `agent_created: true` 的原创 Skills，通过 GitHub API 一键备份到远程仓库，支持增量更新与文件级同步。

| 项目 | 内容 |
|------|------|
| 适用场景 | Skills 版本管理、跨设备同步、开源分享 |
| 触发短语 | "备份我的 skills"、"同步 skills 到 GitHub" |
| 核心能力 | 自动扫描、GitHub API 上传、增量更新 |
| 附加资料 | 3 个 Python 脚本、GitHub API 参考文档 |

---

## 快速开始

### 原生安装（WorkBuddy）

```bash
# 克隆仓库
git clone https://github.com/FooFieYoon/workbuddy-skills.git

# 安装到用户级（所有项目可用）
cp -r workbuddy-skills/skills/<skill-name> ~/.workbuddy/skills/

# 安装到项目级（仅当前项目）
cp -r workbuddy-skills/skills/<skill-name> .workbuddy/skills/
```

重启 WorkBuddy 后，直接用自然语言触发。

### 迁移到其他 AI 工具

详见 [`docs/tools-guide.md`](docs/tools-guide.md) — 涵盖 Cursor、VS Code + Continue、Claude Desktop、Cherry Studio、Open WebUI 等工具的具体迁移方法。

---

## 贡献

本仓库由 Hermes Agent 自动维护。欢迎通过 Issue / Pull Request 贡献新的 Skill 或提出改进建议：

1. Fork 本仓库
2. 在 `skills/` 下创建新的 Skill 目录（包含 `SKILL.md`）
3. `SKILL.md` 中需包含 `agent_created: true` 标记
4. 提交 Pull Request

---

## 许可证

MIT License

---

## 关于

- **仓库地址**: [github.com/FooFieYoon/workbuddy-skills](https://github.com/FooFieYoon/workbuddy-skills)
- **维护者**: Hermes Agent
- **所属项目**: [WorkBuddy AI 助手](https://www.workbuddy.ai)
