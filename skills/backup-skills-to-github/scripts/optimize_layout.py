#!/usr/bin/env python3
"""
Optimize GitHub repo layout for WorkBuddy skills backup.
- Moves all skill dirs into skills/ subdirectory (if not already)
- Generates/updates README.md with full tables

Usage:
    python3 optimize_layout.py <owner>/<repo>
"""
import os
import sys
import json
import base64
import subprocess
import urllib.request
import urllib.error
import re


def get_gh_token():
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    return result.stdout.strip()


def make_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
    }


def api_request(url, method="GET", data=None, headers=None):
    req = urllib.request.Request(url, headers=headers, method=method)
    if data is not None:
        req.data = json.dumps(data).encode("utf-8")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read()), None
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read())
        except Exception:
            err = {"message": str(e)}
        return None, err


def list_repo_files(repo, headers, path=""):
    """Recursively list all files in repo."""
    url = f"https://api.github.com/repos/{repo}/contents"
    if path:
        url += f"/{path}"
    items, _ = api_request(url, "GET", headers=headers)
    if not items:
        return []
    files = []
    for item in items:
        if item["type"] == "file":
            files.append(item["path"])
        elif item["type"] == "dir" and item["name"] != "skills":
            files.extend(list_repo_files(repo, headers, item["path"]))
    return files


def get_skill_names_from_repo(repo, headers):
    """Get skill names by listing skills/ dir, or root dir if skills/ doesn't exist."""
    url = f"https://api.github.com/repos/{repo}/contents/skills"
    items, err = api_request(url, "GET", headers=headers)
    if err:
        # skills/ doesn't exist yet, list root
        url = f"https://api.github.com/repos/{repo}/contents"
        items, _ = api_request(url, "GET", headers=headers)
        # Filter out README.md and non-dir items
        skills = [it["name"] for it in items
                  if it["type"] == "dir" and it["name"] != "skills"]
        return skills, False  # (names, already_in_skills_dir)
    skills = [it["name"] for it in items if it["type"] == "dir"]
    return skills, True


def move_file(repo, old_path, new_path, headers):
    """Move a file by re-uploading to new path and deleting old."""
    # GET old file
    old_url = f"https://api.github.com/repos/{repo}/contents/{old_path}"
    data, err = api_request(old_url, "GET", headers=headers)
    if err:
        print(f"  SKIP (not found): {old_path}")
        return False
    sha = data["sha"]
    content_b64 = data["content"].strip()

    # PUT to new path
    new_url = f"https://api.github.com/repos/{repo}/contents/{new_path}"
    payload = {
        "message": f"Move {old_path} → {new_path}",
        "content": content_b64,
    }
    _, err = api_request(new_url, "PUT", data=payload, headers=headers)
    if err:
        print(f"  FAIL move {old_path}: {err.get('message')}")
        return False

    # DELETE old path
    del_payload = {
        "message": f"Delete old {old_path}",
        "sha": sha,
    }
    _, err = api_request(old_url, "DELETE", data=del_payload, headers=headers)
    if err:
        print(f"  WARN: could not delete old {old_path}: {err.get('message')}")
    return True


def generate_readme(skills, repo_owner, repo_name):
    """Generate a comprehensive README.md."""
    rows = []
    for s in sorted(skills):
        rows.append(f"| `{s}` | 原创 Skill | `agent_created: true` |")

    skills_table = "\n".join(rows) if rows else "（无）"

    return f"""# WorkBuddy Skills Backup

本仓库备份 WorkBuddy AI 助手的**原创 Skills**（`agent_created: true`），可直接导入使用。

## 包含的 Skills

| Skill 名称 | 类型 | 说明 |
|---|---|---|
{skills_table}

## 安装方法

将需要的 skill 目录复制到 WorkBuddy 的 skills 目录：

```bash
# 用户级安装（所有项目可用）
cp -r skills/<skill-name> ~/.workbuddy/skills/

# 项目级安装（仅当前项目）
cp -r skills/<skill-name> <project-root>/.workbuddy/skills/
```

安装后重启 WorkBuddy 即可使用。

## 仓库结构

```
scholar-forge/
├── README.md
└── skills/
    ├── <skill-name>/
    │   ├── SKILL.md          # 核心文件
    │   ├── references/       # 参考资料（可选）
    │   ├── scripts/          # 辅助脚本（可选）
    │   └── assets/           # 资源文件（可选）
    └── ...
```

## 触发示例

| 用户说 | 触发 Skill |
|---|---|
| "写一篇学术会议论文" | `academic-conference-paper-writer` |
| "帮我写论文" | `academic-paper-writer` |
| "写教学科研论文" | `edu-research-paper` |
| "降低 AIGC 检测率" | `paperyy-aigc-rewrite` |
| "备份我的 skills" | `backup-skills-to-github` |

## 关于 WorkBuddy Skills

每个 Skill 是一个独立的能力模块，包含：

- **SKILL.md** — 核心文件，定义触发词、工作流程、注意事项
- **references/** — 参考文档，供 Skill 运行时查阅
- **scripts/** — 辅助脚本，完成自动化任务
- **assets/** — 资源文件（图片、模板等）

## 相关链接

- 官网：https://www.workbuddy.ai
- Skills 文档：https://www.workbuddy.ai/docs/skills

## 贡献

欢迎提交 PR 改进这些 Skills！

---
*由 WorkBuddy 自动备份 · 最后更新：2026-05-30*
"""


def update_readme(repo, headers, skills):
    """Update README.md in repo root."""
    content = generate_readme(skills, repo.split("/")[0], repo.split("/")[1])
    content_b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    url = f"https://api.github.com/repos/{repo}/contents/README.md"
    _, err = api_request(url, "GET", headers=headers)
    if err and err.get("message", "").startswith("Not Found"):
        payload = {"message": "Add README.md", "content": content_b64}
    else:
        existing, _ = api_request(url, "GET", headers=headers)
        payload = {"message": "Update README.md", "content": content_b64, "sha": existing.get("sha", "")}

    _, err = api_request(url, "PUT", data=payload, headers=headers)
    if err:
        print(f"  README update FAIL: {err.get('message')}")
        return False
    print("  README.md updated")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 optimize_layout.py <owner>/<repo>")
        sys.exit(1)

    repo = sys.argv[1]
    token = get_gh_token()
    if not token:
        print("ERROR: Not logged in. Run: gh auth login")
        sys.exit(1)
    headers = make_headers(token)

    print(f"Optimizing {repo} ...")
    print()

    # Step 1: Check current layout
    skills, already_in_subdir = get_skill_names_from_repo(repo, headers)
    print(f"Found skills: {', '.join(skills) if skills else '(none)'}")
    print(f"Already in skills/ subdir: {already_in_subdir}")
    print()

    if not already_in_subdir and skills:
        # Step 2: Move each skill into skills/ subdir
        print("Moving skills into skills/ subdir...")
        moved = 0
        for skill_name in skills:
            # List all files under this skill
            files = list_repo_files(repo, headers, skill_name)
            ok = True
            for fpath in files:
                new_path = f"skills/{fpath}"
                if move_file(repo, fpath, new_path, headers):
                    moved += 1
                else:
                    ok = False
            if ok:
                print(f"  Moved: {skill_name}")
        print(f"  Total files moved: {moved}")
        print()

    # Step 3: Update README.md
    print("Updating README.md...")
    # Re-fetch skill names after move
    skills, _ = get_skill_names_from_repo(repo, headers)
    update_readme(repo, headers, skills)

    print()
    print(f"Done! Repo: https://github.com/{repo}")


if __name__ == "__main__":
    main()
