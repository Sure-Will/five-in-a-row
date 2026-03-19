# Pull Request 协作指南

这份文档说明如何把工作分支的改动通过 Pull Request 合并到稳定分支。它不依赖某一个固定分支名，所以后续继续迭代时也能复用。

## 什么情况下需要 PR

下面这些场景建议走 Pull Request：

- 你在单独的工作分支上开发
- 你想先检查 diff 再合并
- 你准备把临时分支整理进稳定分支
- 你想保留一条更清晰的项目修改记录

如果你只是自己维护一个单分支仓库，也可以直接在同一个分支继续工作，不一定非要走 PR。

## 推荐分支角色

- 工作分支：日常开发、实验性修改
- 稳定分支：准备发布、准备给 GitHub Pages 使用

常见做法是把工作分支合并到 `main`，但也可以合并到你自己的发布分支。

## 创建 Pull Request 的基本流程

1. 先把本地改动提交到工作分支
2. 把工作分支推送到 GitHub
3. 在 GitHub 仓库页面进入 `Pull requests`
4. 点击 `New pull request`
5. 选择：
   - base: 目标分支
   - compare: 你的工作分支
6. 确认 diff 没问题
7. 填写标题和说明
8. 创建 PR
9. 审查完成后执行合并

## PR 标题怎么写

标题最好直接说明结果，而不是过程。

示例：

- `Improve mobile layout for the Gomoku frontend`
- `Rewrite project docs to match the current static implementation`
- `Fix touch interaction on mobile devices`

## PR 描述建议包含什么

建议至少写这三块：

1. 改了什么
2. 为什么改
3. 怎么验证

一个足够实用的模板：

```md
## Summary

- improve mobile layout
- add touch interaction on the board
- rewrite outdated markdown docs

## Why

The previous docs and UI behavior no longer matched the current project state.

## Verification

- opened the page locally with `python3 -m http.server 8080`
- verified board init and move interaction
- checked mobile-sized layout in browser responsive mode
```

## 合并前检查

创建或合并 PR 前，建议看这几项：

- 页面能不能正常打开
- 棋盘和交互有没有回归
- README 和实际实现是否一致
- 部署相关说明是否仍然准确
- GitHub Pages 需要的入口文件是否还在根目录

## 什么时候可以删除源分支

如果这些条件都满足，通常可以删除：

- 改动已经合并
- 你不再需要继续在这个分支上开发
- 稳定分支已经包含最终内容

如果这个分支还会继续承载后续工作，就先不要删。

## 如果没有稳定分支怎么办

如果仓库暂时只有一个工作分支，你可以先：

1. 继续在当前分支完成改动
2. 等准备上线时再创建稳定分支
3. 再把当前内容合并或整理过去

这样比一开始就把临时分支写死在文档里更灵活。

## 和 GitHub Pages 的关系

Pull Request 本身不会自动让站点更新。真正影响线上内容的是：

- 你最终把哪些代码放进了远端发布分支
- GitHub Pages 当前指向哪个分支

也就是说，PR 是协作和审查机制，Pages 是发布机制，它们不是同一个东西。
