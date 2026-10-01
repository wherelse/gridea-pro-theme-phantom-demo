---
id: 9UnfQr
title: 你好，Phantom —— 从旧版 Gridea 来到 Gridea Pro
createdAt: "2026-03-05 10:00:00"
updated: "2026-10-01 15:33:33"
tags:
    - Phantom
    - Gridea Pro
tag_ids:
    - xGrxRd
    - BCXD1z
categories:
    - 主题开发
category_ids:
    - enrEUL
published: true
hideInList: false
feature: /post-images/cover-hello.png
isTop: true
---

第一次打开 Phantom，像推开一扇很大的落地窗：整屏的磁贴，右侧滑出的菜单，字与图都铺得很开。

这个主题最早是 [HTML5UP 的 Phantom](https://html5up.net/phantom)，后来被移植成旧版 Gridea 主题 `gridea-theme-phantom`。现在，它来到了 **Gridea Pro**。

<!-- more -->

## 变的是什么

旧版主题用 EJS 模板，配置项是一堆 `switch`、`array`。迁到 Gridea Pro 之后，很多能力变成了**站点原生功能**：

- **友链**不再塞在主题配置里，而是 Gridea Pro 的「友链」模块，主题直接渲染 `links`。
- **闪念**使用原生 `memos` 数据，不用再挂外部哔哔脚本。
- **评论**由站点级「评论」统一配置，支持 Twikoo / Waline / Valine / Gitalk / Giscus / Disqus / Cusdis。
- **KaTeX 公式**由引擎在含公式的页面自动注入样式。

## 没变的是什么

磁贴式的首页、`Menu` 侧滑导航、页脚的 Follow 图标墙、相册的大图网格——这些属于 Phantom 的「味道」，一个都没丢。

> 换引擎，不换气质。

主题的模板从 EJS 改写为 Jinja2（Pongo2），样式依旧是那套 LESS，静态资源原样保留。

## 接下来

- 想看看它都能做什么，翻翻[《Phantom 主题功能一览》](/post/phantom-features/)；
- 想自己动手改，读读[《Gridea Pro 主题开发指南》](/post/gridea-pro-theme-guide/)。