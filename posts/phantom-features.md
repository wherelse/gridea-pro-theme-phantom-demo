---
id: emtbol
title: Phantom 主题功能一览
createdAt: "2026-03-03 14:30:00"
updated: "2026-10-01 15:33:33"
tags:
    - Phantom
    - 主题
tag_ids:
    - xGrxRd
    - azGnmO
categories:
    - 主题开发
category_ids:
    - enrEUL
published: true
hideInList: false
feature: /post-images/cover-features.png
isTop: false
---

这篇把 Phantom Pro 的主要能力列一遍，按「表面上能看到的」和「设置里能调的」分开说。

## 页面上有的

| 页面 | 路径 | 说明 |
| --- | --- | --- |
| 首页 | `/` | 磁贴式文章列表，自动分页 |
| 博客 | `/blog/` | 与首页同款的独立列表页 |
| 文章 | `/post/<slug>/` | 正文 + 右侧目录，窄屏自动隐藏 |
| 归档 | `/archives/` | 按年份分组 |
| 标签 | `/tags/` 与 `/tag/<slug>/` | 标签云 + 单标签列表 |
| 分类 | `/category/<slug>/` | 复用标签页模板渲染 |
| 相册 | `/post/gallery/` | 主题配置里的照片，瀑布式磁贴 |
| 日常 | `/memos/` | Gridea Pro 原生闪念 |
| 友链 | `/links/` | Gridea Pro 原生友链 |
| 关于 | `/post/about/` | 由 `about` 页面渲染 |

## 设置里能调的

- **社交**：GitHub、Twitter、微博、知乎、bilibili、Facebook、500px、Dribbble、Instagram，填了才会出现在页脚。
- **代码高亮**：开关 Prism 高亮与样式。
- **备案信息**：填了会显示在页脚版权行。
- **自定义 CSS**：追加到页头，用来做一点「只有我会用」的微调。
- **相册**：一个可增删的数组，每张照片填图片与描述。
- **页面标题**：相册、友链、日常三个页面的标题都可以改。

## 一点设计说明

Phantom 的首页没有侧边栏，文章以「图 + 标题 + 摘要」的卡片铺开，因此**封面图规格统一**时观感最好。建议用 16:10 左右的横图。

```css
/* 想让磁贴更紧凑，可以在「自定义 CSS」里试试 */
.tiles article {
  width: calc(50% - 2.5em);
}
```

> 小提示：相册页和首页共用 `.tiles` 布局，两者风格天然一致。