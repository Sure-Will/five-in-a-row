# 部署指南

这份文档说明如何把 `five-in-a-row` 部署成一个可公开访问的静态网页。

项目是纯静态前端，入口文件就是 [`index.html`](./index.html)，所以部署方式很简单：只要把包含它的分支发布到静态托管平台即可。

## 推荐部署方式

推荐优先使用 GitHub Pages，因为这个仓库天然适合：

- 没有构建步骤
- 没有后端服务
- 没有依赖安装要求
- 一次配置后，后续更新成本低

如果你不想用 GitHub Pages，也可以用 Netlify、Vercel 静态托管，或者任意基础文件服务器。

## 部署前确认

开始前先确认这几件事：

1. 远端仓库里已经有 `index.html`
2. 你准备发布的分支已经推送到 GitHub
3. 仓库对外可访问，或者你的 Pages 配置支持当前可见性

注意：本地改动不会自动出现在线上。只有提交并推送到远端之后，GitHub Pages 才能部署到新版本。

## GitHub Pages 部署

### 方案一：发布稳定分支

更推荐长期使用的方式，是准备一个稳定发布分支，例如 `main`。

流程通常是：

1. 在本地完成修改
2. 提交到你的工作分支
3. 合并到发布分支
4. 推送发布分支
5. 在 GitHub Pages 中选择该分支作为站点来源

这样做的好处是：

- 线上分支更稳定
- 工作分支和发布分支职责更清楚
- 后续 PR 和回滚更容易管理

### 方案二：直接发布当前工作分支

如果你只是想尽快上线，也可以直接发布当前包含 `index.html` 的分支。

适合这种情况：

- 仓库还没有整理出 `main`
- 你暂时只有一个可用分支
- 你只是先把页面挂上去验证

缺点是分支名可能比较临时，不利于长期维护。

## GitHub Pages 设置步骤

1. 打开仓库主页
2. 进入 `Settings`
3. 在左侧找到 `Pages`
4. 在 `Build and deployment` 或 `Source` 区域选择：
   - Branch: 选择你要发布的分支
   - Folder: 选择 `/ (root)`
5. 点击 `Save`
6. 等待 GitHub 完成部署

成功后，项目页通常会出现在：

```text
https://<你的用户名>.github.io/five-in-a-row/
```

对于当前仓库用户名，历史地址模式是：

```text
https://sure-will.github.io/five-in-a-row/
```

## 本地验证再部署

建议先在本地确认页面正常，再做线上发布：

```bash
cd five-in-a-row
python3 -m http.server 8080
```

然后访问：

```text
http://localhost:8080
```

重点检查：

- 页面是否能正常加载
- `Initialize Sequence` 是否能开始对局
- 棋盘点击和手机触控是否正常
- 页面在小屏上是否有横向溢出

## 更新线上版本

后续更新时，基本流程不变：

1. 本地修改代码
2. 本地验证页面
3. 提交到你要发布的分支
4. 推送到 GitHub
5. 等待 Pages 自动重新部署

GitHub Pages 一般会在几分钟内完成更新。

## 常见问题

### Pages 下拉框里没有可选分支

通常说明：

- 分支还没推到远端
- 远端分支里没有站点文件
- 仓库页面缓存还没刷新出来

### 访问地址是 404

优先检查：

- `index.html` 是否在分支根目录
- Pages 选择的是否是正确分支
- 部署是否已经成功
- 是否给了 GitHub 足够的构建时间

### 改了本地文件但线上没更新

这是正常现象。GitHub Pages 只看远端仓库，不看你本地工作区。

## 相关文档

- [`README.md`](./README.md)
- [`README.zh-CN.md`](./README.zh-CN.md)
- [`PAGES_GUIDE.md`](./PAGES_GUIDE.md)
- [`SIMPLE_DEPLOY.md`](./SIMPLE_DEPLOY.md)
