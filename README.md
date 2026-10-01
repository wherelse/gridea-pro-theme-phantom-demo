# Phantom Demo

[`gridea-pro-theme-phantom`](https://github.com/wherelse/gridea-pro-theme-phantom) 的演示站，
内容为原创 demo 数据。

- **在线预览**：<https://wherelse.github.io/gridea-pro-theme-phantom-demo/>
- **使用指南**：<https://wherelse.github.io/gridea-pro-theme-phantom-demo/post/theme-guide/>
- **主题仓库**：<https://github.com/wherelse/gridea-pro-theme-phantom>

[![Build & Deploy Demo](https://github.com/wherelse/gridea-pro-theme-phantom-demo/actions/workflows/deploy-demo.yml/badge.svg)](https://github.com/wherelse/gridea-pro-theme-phantom-demo/actions/workflows/deploy-demo.yml)

## 目录

```
config/      站点配置（themeName 指向 gridea-pro-theme-phantom）
posts/       演示文章（含 about.md / gallery.md 两个隐藏页）
post-images/ 文章封面（PNG）
images/      站点头像与主题相册图片
themes/
  gridea-pro-theme-phantom/   主题副本，使本站自成一体
.github/
  workflows/deploy-demo.yml   构建 + 部署到 GitHub Pages
  ci/render/main.go           调用 Gridea Pro 真实引擎渲染
  ci/prefix_paths.py          为项目 Pages 子路径补全绝对路径前缀
```

## 本地预览

用 Gridea Pro 打开本目录（设置里的「站点源文件路径」指向本目录即可），
`config/config.json` 的 `sourceFolder` 若因移动位置失效，改一下该字段。

## 自动部署

推送到 `main` 后，`.github/workflows/deploy-demo.yml` 会：

1. 克隆 [Gridea Pro](https://github.com/Gridea-Pro/gridea-pro) 源码，注入一个渲染命令；
2. 用其**真实渲染引擎**把本仓库渲染成静态站点（产物在 `output/`）；
3. 把站内绝对路径（`/styles/...` 等）补上 `/<repo>/` 前缀——因为 GitHub 项目 Pages 部署在子路径下；
4. 通过 GitHub Pages（build_type=workflow）发布。

> 因为使用的是官方引擎，演示站与本地 Gridea Pro 渲染结果一致。
