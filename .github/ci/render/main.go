// ci_render 用 Gridea Pro 的真实渲染引擎，把一个站点源目录渲染成静态站点。
//
// 用法：
//
//	go run ./backend/cmd/ci_render <站点源目录>
//
// 产物写入 <站点源目录>/output。该文件由 demo 仓库的 CI 在克隆 Gridea Pro 源码后
// 临时放入 backend/cmd/ci_render/，因此必须与 Gridea Pro 主仓库的模块路径保持一致。
package main

import (
	"context"
	"fmt"
	"os"

	"gridea-pro/backend/internal/engine"
	"gridea-pro/backend/internal/repository"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("usage: ci_render <appDir>")
		os.Exit(2)
	}
	appDir := os.Args[1]

	postRepo := repository.NewPostRepository(appDir, nil)
	tagRepo := repository.NewTagRepository(appDir)
	categoryRepo := repository.NewCategoryRepository(appDir)
	menuRepo := repository.NewMenuRepository(appDir)
	linkRepo := repository.NewLinkRepository(appDir)
	themeRepo := repository.NewThemeRepository(appDir)
	settingRepo := repository.NewSettingRepository(appDir)
	memoRepo := repository.NewMemoRepository(appDir)
	commentRepo := repository.NewCommentRepository(appDir)
	seoSettingRepo := repository.NewSeoSettingRepository(appDir)
	cdnSettingRepo := repository.NewCdnSettingRepository(appDir)

	e := engine.New(appDir, postRepo, themeRepo, settingRepo)
	e.SetMenuRepo(menuRepo)
	e.SetLinkRepo(linkRepo)
	e.SetTagRepo(tagRepo)
	e.SetMemoRepo(memoRepo)
	e.SetCommentRepo(commentRepo)
	e.SetCategoryRepo(categoryRepo)
	e.SetSeoSettingRepo(seoSettingRepo)
	e.SetCdnSettingRepo(cdnSettingRepo)

	if err := e.RenderAll(context.Background()); err != nil {
		fmt.Println("RENDER ERROR:", err)
		os.Exit(1)
	}
	fmt.Println("RENDER OK ->", appDir+"/output")
}
