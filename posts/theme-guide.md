---
id: AUuip6
title: Phantom 主题使用指南
createdAt: "2026-03-07 10:00:00"
updated: "2026-10-01 15:50:37"
tags:
    - 教程
    - Phantom
tag_ids:
    - R2EOxf
    - xGrxRd
categories:
    - 主题开发
category_ids:
    - enrEUL
published: true
hideInList: false
feature: ""
isTop: false
---

这份指南面面俱到地说明 `gridea-pro-theme-phantom` 的安装、设置、每个页面的来源，
以及常见的坑与自定义方法。第一次使用建议从头读一遍。

> 本指南本身就是这个演示站里的一篇文章——它既能当文档读，也顺便展示了主题的正文排版。

## 目录

1. [安装与启用](#安装与启用)
2. [页面一览](#页面一览)
3. [主题设置项](#主题设置项)
4. [相册怎么用](#相册怎么用)
5. [日常（闪念）](#日常闪念)
6. [友链](#友链)
7. [评论](#评论)
8. [特殊页面机制](#特殊页面机制)
9. [自定义样式与布局](#自定义样式与布局)
10. [从旧版 Phantom 迁移的差异](#从旧版-phantom-迁移的差异)
11. [常见问题](#常见问题)

---

## 安装与启用

1. 把主题目录 `gridea-pro-theme-phantom` 复制到你的 Gridea Pro 站点目录下的 `themes/` 中
   （默认站点目录是 `~/Documents/Gridea Pro/`，以应用里显示的路径为准）。
2. 重启 Gridea Pro，在「主题」中切换到 **Phantom**。
3. 主题设置面板里按需填写，保存后渲染即可看到效果。

> **重要**：Gridea Pro 对主题 `config.json` 的 `customConfig` 声明有**进程级缓存**。
> 如果你修改了主题的 `config.json`（比如新增了配置项），必须**重启应用**才会生效；
> 但改动 `templates/`、`assets/` 里的模板与样式是不需要重启的。

## 页面一览

主题的文件名是固定约定，引擎据此渲染各个路由：

| 页面 | 模板文件 | 输出路径 | 说明 |
| --- | --- | --- | --- |
| 首页 | `index.html` | `/` 及 `/page/2/` … | 磁贴式文章列表，自动分页 |
| 博客列表 | `blog.html` | `/{postPath}/`（默认 `/post/`） | 与首页同款列表页 |
| 文章详情 | `post.html` | `/post/<slug>/` | 正文 + 右侧目录（窄屏隐藏） |
| 归档 | `archives.html` | `/archives/` | 按年份分组 |
| 标签汇总 | `tags.html` | `/tags/` | 标签云 |
| 单个标签 | `tag.html` | `/tag/<slug>/` | 该标签下的文章 |
| 分类汇总 | `categories.html` | `/categories/` | 分类云 |
| 单个分类 | `category.html` | `/category/<slug>/` | 该分类下的文章 |
| 闪念 | `memos.html` | `/memos/` | Gridea Pro 原生 memos |
| 友链 | `links.html` | `/links/` | Gridea Pro 原生友链 |
| 关于 | `about.html` | `/post/about/` | 由 `about` 页面渲染（见下） |
| 相册 | `gallery.html` | `/post/gallery/` | 由 `gallery` 页面渲染（见下） |
| 404 | `404.html` | `/404.html` | 找不到页面时展示 |

> **博客菜单为什么指向 `/post/` 而不是 `/blog/`？** 引擎把 `blog.html` 渲染到配置的
> `postPath`（默认 `post`）下，所以博客列表页的地址是 `/post/`，不是 `/blog/`。
> 添加菜单时请链接到 `/post`。

## 主题设置项

设置项分组与含义：

### 社交

`Github / Twitter / 微博 / 知乎 / bilibili / Facebook / 500px / Dribbble / Instagram`
——填了链接才会在页脚出现对应图标，留空即隐藏。

### 主题功能

| 配置项 | 类型 | 说明 |
| --- | --- | --- |
| 代码高亮主题 | 开关 | 开启后在文章页加载 Prism 高亮与样式 |
| 无封面时显示自动封面 | 开关 | 默认开启：无特色图的文章自动生成渐变封面；关闭后则不显示封面 |
| 备案信息 | 输入 | 填写后显示在页脚版权行 |
| 自定义 CSS | 多行 | 追加到 `</head>` 前，用于覆盖主题样式 |

### 相册

| 配置项 | 说明 |
| --- | --- |
| 相册页面标题 | 相册页的标题文字 |
| 相册 | 可增删的图片列表，每项含「图片」与「描述」 |

### 友链 / 日常

- **友链页面标题**：友链页标题（条目在 Gridea Pro 的「友链」模块里管理）。
- **日常页面标题**：闪念页标题（内容在 Gridea Pro 的「闪念」模块里管理）。

### 评论

- **Twikoo 前端版本**：仅在使用 Twikoo 时生效，需与服务端大版本一致。

> 评论平台（Twikoo / Waline / Valine / Gitalk / Giscus / Disqus / Cusdis）在
> Gridea Pro 的**站点级「评论」设置**里配置，主题会自动按所选平台渲染，无需主题里再开关。

## 相册怎么用

相册图片通过主题设置里的「相册」数组维护。按 Gridea Pro 的约定，通过设置面板
上传的图片会被保存到站点的 `images/theme/` 目录，路径形如 `/images/theme/xxx.png`。

- 在设置面板点图片框即可上传，也可以直接在输入框里填写**图床外链**。
- `description` 会作为图片下方的小字说明。
- 相册页使用与首页相同的磁贴布局，**建议使用规格统一的横图**（例如 3:2）。

## 日常（闪念）

闪念内容在 Gridea Pro 的「闪念」模块里写，主题只负责渲染成时间线样式。
每条闪念支持正文（Markdown）与标签。

## 友链

友链条目在 Gridea Pro 的「友链」模块里管理，字段映射如下：

| 应用的字段 | 模板里的变量 |
| --- | --- |
| 名称 | `link.siteName` |
| 链接 | `link.siteLink` |
| 头像 | `link.avatar` |
| 描述 | `link.description` |

> **头像建议填外链**（如 `https://github.com/xxx.png`）。应用内的友链卡片是
> 直接把 `avatar` 当作图片地址用的，写本地相对路径在应用里显示不出来。
> 也可以填 `data:image/...;base64,…` 这类内嵌图片。

## 评论

评论由站点级设置统一控制。主题只在文章页与关于页挂载评论区，并根据
`commentSetting.commentPlatform` 渲染对应平台。切平台不需要改主题。

## 特殊页面机制

引擎渲染文章时，如果文章的**文件名**恰好等于某个模板名（如 `about`、`gallery`），
就会用那个模板来渲染这篇文章，并且不显示上一篇/下一篇。

因此「关于」和「相册」是这样来的：

1. 新建一篇文章，把**文件名**设为 `about`（或 `gallery`）；
2. 设为「不在列表中显示」（`hideInList`）；
3. 新建菜单指向 `/post/about`（或 `/post/gallery`）。

`about.html` 会输出这篇文章的正文；`gallery.html` 则忽略正文，改为输出主题设置里的相册。

## 自定义样式与布局

### 改配色 / 字体

主题样式是 `assets/styles/main.less`，构建时编译为 `/styles/main.css`。
不建议直接大改，推荐在「自定义 CSS」里覆盖，例如：

```css
/* 圆角更大、文章更宽 */
.tiles article > .image { border-radius: 12px; }
#mainpage-wrapper > * > .inner { max-width: 64em; }

/* 顶部导航选中/悬停色 */
#header .site-nav ul li a:hover { color: #6366f1 !important; }
```

### 顶部导航

菜单直接平铺在页头 `.site-nav` 中，窄屏自动换行；不再是右上角的滑出菜单。
菜单项来自 Gridea Pro 的「菜单」设置，外链菜单会自动 `target="_blank"`。

### 封面图规格

首页/博客/标签/分类的磁贴都使用统一比例（16:10）裁切，所以封面图**规格统一**时观感最好。

## 从旧版 Phantom 迁移的差异

如果你用过旧版 `gridea-theme-phantom`，这是主要变化：

| 旧版（EJS） | 现在的 Phantom Pro（Jinja2） |
| --- | --- |
| 友链写在主题配置的数组里 | 改为 Gridea Pro 原生「友链」 |
| 日常外挂哔哔脚本 | 改为 Gridea Pro 原生「闪念」 |
| 主题里配 Twikoo/Waline 开关 | 改为站点级「评论」设置 |
| KaTeX 开关 + 手动加载 | 引擎在含公式页面自动注入 |
| 右上角滑出菜单 | 顶部平铺导航 |
| `.ejs` 模板 | `.html`（Jinja2 / Pongo2）模板 |

## 常见问题

**Q：首页/相册图片不显示怎么办？**
A：确认图片路径符合约定——文章封面用 `/post-images/…`，主题设置里的相册用
`/images/theme/…`，友链头像用外链。路径前缀写错是图片不显示的头号原因。

**Q：访问 `/blog` 是 404？**
A：博客列表实际在 `/post/`，菜单请链接到 `/post`。

**Q：页面顶部出现黄色横幅 / 某页样式全乱了？**
A：那是某个模板渲染抛错后的降级视图（HTML 里含 `fallback-banner`）。
多半是变量名或过滤器写法问题，对照官方变量表检查模板。

**Q：改了主题设置面板的选项，但界面没变化？**
A：改动的是主题 `config.json` 的 `customConfig` 声明时需要重启应用；只是切换开关、
重新渲染的话不必重启。

**Q：文章页没有目录？**
A：目录来自正文里的 `h2/h3`，正文太短或没有二级标题时就不会生成。

---

想自己动手改主题，可以配合 `theme-builder-skill` 的变量参考与 Jinja2 指南使用。