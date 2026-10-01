#!/usr/bin/env python3
"""把构建产物里的站内绝对路径（以 / 开头）加上子路径前缀。

Gridea Pro 渲染出的 HTML/CSS 使用站点根绝对路径（如 /styles/main.css、
/post-images/x.png、/post/xxx/）。GitHub 项目 Pages 部署在
https://<user>.github.io/<repo>/ 这样的子路径下，根绝对路径会 404，
因此这里统一补上前缀。

用法：
    python3 prefix_paths.py <输出目录> <前缀>     # 前缀形如 /my-repo
"""
import os
import re
import sys

# HTML / XML：这些属性里的 "/xxx" 需要加前缀
ATTR_RE = re.compile(
    r'(\b(?:href|src|data-src|poster|action|formaction)=")/(?!/)'
)
# HTML / XML：JSON-LD 等内联 JSON 里的 "key":"/xxx"
JSONLIKE_RE = re.compile(r'("(?:\w+)"\s*:\s*")/(?!/)')
# CSS：url(/xxx)
CSS_URL_RE = re.compile(r'(url\(\s*["\']?)/(?!/)')
# JSON 文件：任意 "key":"/xxx"
JSON_RE = re.compile(r'(":\s*")/(?!/)')


def rewrite(path, patterns):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    out = text
    for rx, repl in patterns:
        out = rx.sub(repl, out)
    if out != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        return True
    return False


def main():
    if len(sys.argv) < 3:
        print("usage: prefix_paths.py <dir> <prefix>")
        sys.exit(2)
    out_dir = sys.argv[1]
    prefix = "/" + sys.argv[2].strip("/")
    sub = prefix + "/"

    changed = 0
    for root, _dirs, files in os.walk(out_dir):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            path = os.path.join(root, name)
            if ext in (".html", ".htm", ".xml"):
                pats = [
                    (ATTR_RE, r"\g<1>" + sub),
                    (JSONLIKE_RE, r"\g<1>" + sub),
                ]
            elif ext == ".css":
                pats = [(CSS_URL_RE, r"\g<1>" + sub)]
            elif ext in (".json", ".webmanifest"):
                pats = [(JSON_RE, r"\g<1>" + sub)]
            else:
                continue
            if rewrite(path, pats):
                changed += 1

    print(f"prefix '{prefix}' applied, rewritten files: {changed}")


if __name__ == "__main__":
    main()
