---
id: FP7wM8
title: Gridea Pro 主题开发指南（以 Phantom 为例）
createdAt: "2026-02-26 20:00:00"
updated: "2026-10-01 15:33:33"
tags:
    - 教程
    - Gridea Pro
tag_ids:
    - R2EOxf
    - BCXD1z
categories:
    - 主题开发
category_ids:
    - enrEUL
published: true
hideInList: false
feature: /post-images/cover-guide.png
isTop: false
---

Gridea Pro 支持三种模板引擎：Jinja2（Pongo2）、Go Templates、EJS。Phantom Pro 用的是 **Jinja2**——最接近大家熟悉的语法，迁移成本也低。

## 目录结构

```
gridea-pro-theme-phantom/
├── config.json          # 主题元信息 + 可视化配置声明
├── assets/              # 静态资源，构建时 assets/ 前缀会被去掉
│   ├── media/
│   └── styles/main.less
└── templates/
    ├── base.html        # 布局骨架
    ├── index.html       # 首页
    ├── post.html        # 文章页
    └── partials/        # 可复用组件
```

## 三条最容易踩的坑

1. **assets 前缀会被去掉**。写 `<link href="/styles/main.css">`，不是 `/assets/styles/main.css`。
2. **`post.date` 是 RFC3339 字符串**，Jinja2 里对它用 `|date:` 会直接报错、整页降级。展示用 `post.dateFormat`，相对时间用 `|relative`。
3. **`not x == y` 是静默陷阱**。Pongo2 会解析成 `(not x) == y`，恒为 false 且不报错。不等判断一律用 `!=`。

## 自定义配置怎么声明

`config.json` 里的 `customConfig` 决定了主题设置面板长什么样。常用的类型：

```json
{
  "name": "codeHighlight",
  "label": "代码高亮",
  "group": "主题功能",
  "type": "switch",
  "value": true
}
```

数组类型（比如 Phantom 的相册）：

```json
{
  "name": "photos",
  "label": "相册",
  "type": "array",
  "value": [],
  "arrayItems": [
    { "name": "image", "label": "图片", "type": "picture-upload" },
    { "name": "description", "label": "描述", "type": "textarea" }
  ]
}
```

模板里通过 `theme_config.photos` 取用。

## 从 EJS 迁移的对照

| EJS | Jinja2 |
| --- | --- |
| `<%= value %>` | `{{ value }}` |
| `<%- value %>` | `{{ value\|safe }}` |
| `<% if (a) { %>` | `{% if a %}` |
| `include('partials/x')` | `{% include "partials/x.html" %}` |
| `arr.length` | `arr\|length` |
| `a && b` | `a and b` |

> 迁移时先跑一遍语法校验和渲染测试，能挡掉大半低级错误。