# 如何启用在线访问（GitHub Pages）

按照以下步骤，你就可以让其他人直接通过网址访问你的五子棋游戏，无需下载任何文件！

## 📝 启用步骤

### 1. 合并代码到主分支

首先需要将当前分支的代码合并到main分支：

1. 在GitHub网站上打开你的仓库
2. 点击 "Pull requests"
3. 点击 "New pull request"
4. 选择将 `claude/implement-gomoku-game-011CUMZStsdSdAnwEkLNY6Mk` 合并到 `main`
5. 点击 "Create pull request"
6. 填写标题和描述，然后点击 "Create pull request"
7. 最后点击 "Merge pull request" 完成合并

### 2. 启用GitHub Pages

1. 在GitHub仓库页面，点击 **Settings**（设置）
2. 在左侧菜单找到 **Pages**
3. 在 "Source" 部分：
   - Branch: 选择 `main`
   - Folder: 选择 `/ (root)`
4. 点击 **Save**（保存）
5. 等待几分钟，GitHub会自动部署你的网站

### 3. 访问你的游戏

部署完成后，你的游戏将在以下网址可用：

```
https://sure-will.github.io/five-in-a-row/
```

或者直接访问：

```
https://sure-will.github.io/five-in-a-row/index.html
```

## 🎉 完成！

现在你可以：
- 把这个网址分享给朋友
- 他们可以直接在浏览器中玩游戏
- 不需要下载任何文件
- 支持手机、平板、电脑访问

## 📱 分享建议

你可以这样告诉朋友：

```
嘿！我做了个五子棋游戏，来玩玩吧！
🎮 https://sure-will.github.io/five-in-a-row/

支持：
✅ 双人对战
✅ AI对战（简单/中等/困难）
✅ 手机也能玩
```

## ⚠️ 注意事项

- 每次更新代码后，GitHub Pages会自动重新部署
- 通常需要1-5分钟才能看到更新
- 确保仓库是公开的（Public），私有仓库需要付费才能使用GitHub Pages
