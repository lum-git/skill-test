#!/usr/bin/env python3
"""hello 技能的问候脚本。

用法:
    python3 scripts/hello.py "用户的请求内容"
    python3 scripts/hello.py --name 小明 "帮我看看代码"
"""

import argparse
import sys
from datetime import datetime


def greet(name: str, request: str) -> str:
    """生成问候内容：问候 + 复述请求 + 建议下一步。"""
    hour = datetime.now().hour
    if hour < 6:
        period = "凌晨好"
    elif hour < 12:
        period = "早上好"
    elif hour < 18:
        period = "下午好"
    else:
        period = "晚上好"

    lines = [f"{period}，{name}！"]
    if request:
        lines.append(f"你刚才的请求是：「{request}」")
        lines.append("建议下一步：补充更多细节，或让我直接开始处理。")
    else:
        lines.append("你还没有提出具体请求，可以告诉我你想做什么。")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="生成问候语并复述用户请求")
    parser.add_argument("request", nargs="*", help="用户的请求内容")
    parser.add_argument("--name", default="用户", help="用户称呼，默认「用户」")
    args = parser.parse_args()

    request = " ".join(args.request).strip()
    print(greet(args.name, request))
    return 0


if __name__ == "__main__":
    sys.exit(main())
