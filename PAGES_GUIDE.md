# GitHub Pages 详细说明

这份文档专门讲 GitHub Pages 的配置细节。如果你只想最快把页面发布出去，看 [`SIMPLE_DEPLOY.md`](./SIMPLE_DEPLOY.md) 即可。

## GitHub Pages 会发布什么

对于这个仓库，GitHub Pages 会直接把你选择的分支根目录里的静态文件发布出去。

因为项目入口是 [`index.html`](./index.html)，所以最关键的一点只有一个：

你在 Pages 设置里选中的那个分支，根目录必须包含 `index.html`。

## 建议的分支策略

### 稳定方案

使用一个长期稳定的发布分支，例如 `main`。

适合：

- 你准备长期维护这个仓库
- 你会继续迭代 UI 或 AI
- 你希望工作分支和线上分支分离

### 临时方案

直接选择当前工作分支发布。

适合：

- 先把页面挂上去
- 还没整理出稳定分支
- 当前远端分支里已经有完整页面

## GitHub 网页端操作路径

1. 打开仓库主页
2. 点击 `Settings`
3. 在左侧菜单中进入 `Pages`
4. 找到 Pages 的来源设置区域
5. 选择：
   - Branch: 你要发布的分支
   - Folder: `/ (root)`
6. 点击 `Save`

如果界面更新过，GitHub 的文案可能写成 `Build and deployment`，但核心设置项不变。

## 成功后的站点地址

项目仓库的 GitHub Pages 地址通常是：

```text
https://<username>.github.io/<repo-name>/
```

对这个仓库来说，格式是：

```text
https://sure-will.github.io/five-in-a-row/
```

## 怎么确认它真的发布成功

你可以从这几个地方确认：

1. `Settings -> Pages` 页面会显示已发布状态
2. 仓库的 `Actions` 里通常能看到 Pages 部署记录
3. 直接访问站点地址，确认页面能加载

## Pages 更新机制

GitHub Pages 不是实时读取你本地文件，而是根据远端仓库重新部署。

所以每次上线更新都必须满足：

1. 本地改动已经提交
2. 改动已经推送到远端分支
3. Pages 指向的就是这个远端分支

## 推荐的发布前检查

上线前建议至少确认：

- 页面能正常打开
- `Initialize Sequence` 能启动对局
- AI 先手逻辑正常
- 玩家点击或触摸落子正常
- 手机端没有明显布局错位

本地快速验证命令：

```bash
cd five-in-a-row
python3 -m http.server 8080
```

## 常见问题

### 找不到 Settings

只有仓库所有者或有足够权限的协作者才能看到完整设置项。

### 找不到 Pages

GitHub 后台布局会调整，但一般都在仓库设置页左侧菜单中。

### Branch 选项里没有你想要的分支

通常是因为：

- 这个分支还没有推到 GitHub
- GitHub 还没刷新到最新状态
- 你当前账号对仓库权限不够

### 选好了分支，还是打不开页面

优先检查：

- 站点入口文件是不是 `index.html`
- 文件是不是在根目录
- 部署是不是还在进行中
- 浏览器是不是缓存了旧页面

## 什么时候应该改成 `main`

如果你现在只是临时发布当前工作分支，后面最好还是整理成一个稳定发布分支，比如 `main`。这样仓库结构更清楚，文档也更容易长期维护。
