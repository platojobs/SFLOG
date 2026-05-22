#!/usr/bin/env python3
"""Update daily repo pulse for platojobs/SFLog (Gitblog backup)."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT / "BACKUP"
DATA = ROOT / "data"
PULSE_PATH = DATA / "repo-pulse.json"
QUOTES_PATH = DATA / "daily-quotes.json"
ACTIVITY_PATH = ROOT / "ACTIVITY.md"


def load_backup_posts() -> list[dict[str, str]]:
    posts: list[dict[str, str]] = []
    for md in sorted(BACKUP.glob("*.md")):
        title = md.stem
        if "_" in title:
            title = title.split("_", 1)[1]
        posts.append({"title": title or md.name, "file": md.name})
    return posts


def pick_spotlight(posts: list[dict[str, str]], day: int) -> dict[str, str]:
    if not posts:
        return {"title": "暂无备份文章", "file": ""}
    item = posts[day % len(posts)]
    return item


def write_activity_page(pulse: dict) -> None:
    spot = pulse["spotlight"]
    file_line = (
        f"`BACKUP/{spot['file']}`"
        if spot.get("file")
        else "（无）"
    )
    body = f"""# SFLog 每日脉动

本页由 GitHub Actions 自动更新，用于保持仓库轻量维护节奏（非 Issues 同步）。

| 字段 | 值 |
|------|-----|
| UTC 时间 | {pulse["last_updated_utc"]} |
| 本地日期 | {pulse["last_updated_local"]} |
| BACKUP 文章数 | {pulse["posts_total"]} |
| 脉动序号 | {pulse["pulse_count"]} |

## 今日一句

> {pulse["daily_quote"]}

## 今日随机备份

- **标题**：{spot["title"]}
- **文件**：{file_line}

---

[返回 README](/README.md)
"""
    ACTIVITY_PATH.write_text(body, encoding="utf-8")


def main() -> None:
    now = datetime.now(timezone.utc)
    local = datetime.now()
    day = local.timetuple().tm_yday

    quotes = json.loads(QUOTES_PATH.read_text(encoding="utf-8"))
    quote = quotes[day % len(quotes)]

    posts = load_backup_posts()
    spotlight = pick_spotlight(posts, day)

    prev: dict = {}
    if PULSE_PATH.exists():
        prev = json.loads(PULSE_PATH.read_text(encoding="utf-8"))

    pulse = {
        "pulse_count": int(prev.get("pulse_count", 0)) + 1,
        "last_updated_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_updated_local": local.strftime("%Y-%m-%d"),
        "posts_total": len(posts),
        "day_of_year": day,
        "daily_quote": quote,
        "spotlight": spotlight,
    }

    PULSE_PATH.write_text(
        json.dumps(pulse, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_activity_page(pulse)
    print(json.dumps(pulse, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
