---
name: backup-skills-to-github
description: "备份 WorkBuddy 原创 Skills 到 GitHub 仓库。当用户说\"备份 skills\"、\"备份 skill\"、\"上传 skills 到 github\"、\"backup my skills\"、\"sync skills to github\"时触发。自动扫描 agent_created 的原创 skill，创建/更新 GitHub 仓库，通过 API 上传所有文件。"
---

# Backup Skills to GitHub

将 WorkBuddy 原创 Skills（`agent_created: true`）备份到 GitHub 仓库。

## 触发条件

在以下场景使用此 skill：
- 用户说"备份我的 skills"、"备份 skill"
- 用户说"上传 skills 到 github"、"sync to github"
- 用户说"把我的 skills 推送到远程仓库"

## 工作流程

### 第一步：扫描原创 Skills

运行 `scripts/scan_skills.py` 扫描 `~/.workbuddy/skills/` 目录，找出所有 `agent_created: true` 的 skill：

```bash
python3 scripts/scan_skills.py
```

脚本输出所有原创 skill 的名称和路径。

### 第二步：检查 GitHub 认证

```bash
gh auth status
```

未登录时提示用户在终端运行 `gh auth login --web --hostname github.com` 完成授权。

### 第三步：创建或确认仓库

检查目标仓库是否存在：
```bash
gh repo view <username>/workbuddy-skills 2>&1
```

不存在时创建：
```bash
gh repo create workbuddy-skills --public --description "WorkBuddy 原创 Skills 备份"
```

### 第四步：上传文件

使用 `scripts/backup_skills.py` 通过 GitHub REST API 上传文件（绕过 git clone 的 Windows schannel 问题）：

```bash
python3 scripts/backup_skills.py <repo-owner>/<repo-name> [--dir skills/]
```

脚本自动完成：
1. 读取所有原创 skill 文件
2. Base64 编码内容
3. 通过 `gh api --method PUT` 上传到仓库
4. 如果文件已存在则更新（带 SHA）
5. 上传完成后创建/更新 README.md

### 第五步：优化仓库结构

上传完成后，运行 `scripts/optimize_layout.py` 整理目录结构：
- 将所有 skill 移到 `skills/` 子目录
- 生成带表格说明的 README.md

```bash
python3 scripts/optimize_layout.py <repo-owner>/<repo-name>
```

## 文件说明

| 文件 | 用途 |
|---|---|
| `scripts/scan_skills.py` | 扫描并列出所有原创 skill |
| `scripts/backup_skills.py` | 通过 API 上传文件到 GitHub |
| `scripts/optimize_layout.py` | 整理仓库目录结构 |
| `references/github_api_notes.md` | GitHub REST API 使用要点 |

## 注意事项

- **不要在 `/tmp` 写临时文件**，Windows 沙箱会拦截 —— 改用项目目录或直接使用内存
- **不要依赖 git clone/push**，Windows schannel 证书吊销检查会失败 —— 始终用 GitHub REST API
- **`gh api` 上传大文件前先检查是否已存在**（GET 获取 SHA，再 PUT 更新）
- 仓库默认命名为 `workbuddy-skills`，用户可以自定义

## 一键运行

如果依赖已安装，可以直接运行一键脚本：

```bash
python3 scripts/backup_skills.py FooFieYoon/workbuddy-skills --all --optimize
```

参数说明：
- `--all`：自动扫描并上传所有原创 skill
- `--optimize`：上传完成后自动整理目录结构
- `--dir <path>`：指定 skill 在仓库中的子目录（默认根目录）
