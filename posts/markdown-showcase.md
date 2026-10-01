---
id: ugJx3R
title: Markdown 排版示例
createdAt: "2026-03-01 09:00:00"
updated: "2026-10-01 15:33:33"
tags:
    - 示例
tag_ids:
    - yrrC0D
categories:
    - 默认分类
category_ids:
    - DfCat0
published: true
hideInList: false
feature: /post-images/cover-markdown.png
isTop: false
---

这是一篇用来检查排版的草稿：标题、列表、引用、代码、表格、公式、图片，一次看全。

## 二级标题

正文里的**加粗**、*斜体*、`行内代码` 和 [链接](/post/hello-phantom/)。

### 三级标题

无序列表：

- 第一项
- 第二项
  - 嵌套一项
- 第三项

有序列表：

1. 先这样
2. 再那样
3. 最后收尾

## 引用

> 写作最难的部分，永远是坐下来写第一句话。
>
> —— 某个拖延了很久的人

## 代码

行内代码：`theme_config.photos`。

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet('Phantom');
```

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Gridea Pro")
}
```

## 表格

| 变量 | 说明 | 示例 |
| --- | --- | --- |
| `post.title` | 文章标题 | 你好，Phantom |
| `post.feature` | 特色图 | `/post-images/cover.svg` |
| `post.stats.text` | 阅读时长 | 5 min read |

## 公式

行内公式：质能方程 $E = mc^2$。

块级公式：

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

## 图片

![示例图片](/post-images/cover-essay.png)

---

到这里，正文排版基本都过了一遍。