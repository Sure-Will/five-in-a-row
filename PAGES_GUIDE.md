# GitHub Pages 启用详细步骤

在完成Pull Request合并后，按照以下步骤启用GitHub Pages。

## 📖 什么是 GitHub Pages？

GitHub Pages 可以把你的HTML文件变成一个在线网站，让任何人都可以通过网址访问，完全免费！

---

## 🔍 详细操作步骤

### 第一步：打开仓库设置

1. 在你的仓库主页 https://github.com/Sure-Will/five-in-a-row

2. 找到页面顶部的选项卡，点击最右边的 **"Settings"**（设置）
   ```
   < > Code    Issues    Pull requests    ...    Settings
   ```

3. 注意：Settings 选项卡只有仓库所有者才能看到

### 第二步：找到 Pages 设置

1. 进入 Settings 后，你会看到左侧有一个菜单栏

2. 向下滚动左侧菜单，找到 **"Pages"** 选项
   - 它通常在 "Code and automation" 部分
   - 位置大概在中下部

3. **点击 "Pages"**

### 第三步：配置 GitHub Pages

进入 Pages 页面后：

1. 你会看到 **"Source"** （源）部分

2. 第一个下拉框（Branch）：
   - 默认可能显示 "None"
   - **点击这个下拉框**
   - **选择 "main"** （或你的默认分支）

3. 第二个下拉框（Folder）：
   - 会自动出现在 Branch 选择后
   - **保持默认的 "/ (root)"**
   - 意思是使用根目录的文件

4. 点击旁边的蓝色按钮 **"Save"**（保存）

### 第四步：等待部署

1. 保存后，页面顶部会出现一个蓝色提示框：
   ```
   ✅ Your site is ready to be published at https://sure-will.github.io/five-in-a-row/
   ```

2. **等待 1-3 分钟**，GitHub 会自动构建和部署你的网站

3. 刷新页面，蓝色提示框会变成绿色：
   ```
   ✅ Your site is live at https://sure-will.github.io/five-in-a-row/
   ```

### 第五步：访问你的游戏

1. 点击提示框中的链接，或直接在浏览器输入：
   ```
   https://sure-will.github.io/five-in-a-row/
   ```

2. 你应该能看到你的五子棋游戏了！

3. 🎉 恭喜！现在你可以把这个网址分享给任何人了！

---

## 🎯 完整配置示意

在 Pages 设置页面，最终应该看到：

```
Source
├─ Branch: main
└─ Folder: / (root)
[Save]

✅ Your site is live at https://sure-will.github.io/five-in-a-row/
```

---

## ⚠️ 常见问题

### Q1: 找不到 Settings 选项卡？

**A**: 只有仓库的所有者才能看到 Settings。确保：
- 你已经登录GitHub
- 你在自己的仓库页面（URL包含你的用户名）

### Q2: 没有 "main" 分支选项？

**A**:
- 确认你已经完成了 Pull Request 的合并
- 检查你的默认分支名称，可能是 "master"
- 选择包含 index.html 文件的分支

### Q3: 保存后看不到提示框？

**A**:
- 刷新页面
- 检查是否选择了正确的分支
- 确保分支中有 index.html 文件

### Q4: 访问网址显示 404？

**A**:
- 等待 5-10 分钟再试（首次部署可能需要更长时间）
- 确认 index.html 文件在仓库根目录
- 在 Pages 设置中检查是否显示 "live"

### Q5: 仓库是私有的？

**A**:
- 免费账户的 GitHub Pages 只支持公开仓库
- 需要将仓库设为 Public，或升级到 GitHub Pro

---

## 🔧 如果还是不行

### 方法1：检查文件
1. 在仓库主页点击 "Code" 选项卡
2. 确认能看到 `index.html` 文件
3. 点击它，确保内容正确

### 方法2：查看部署状态
1. 在仓库主页点击 "Actions" 选项卡
2. 查看 "pages build and deployment" 的状态
3. 如果显示红色 ❌，点击查看错误信息

### 方法3：重新部署
1. 回到 Settings → Pages
2. 将 Branch 改为 "None"，保存
3. 再改回 "main"，保存
4. 强制重新部署

---

## ✅ 成功的标志

当一切正常时，你会看到：

1. Pages 设置页面显示：
   ```
   ✅ Your site is live at https://sure-will.github.io/five-in-a-row/
   ```

2. Actions 页面显示绿色的 ✅

3. 访问网址能看到你的五子棋游戏

---

## 📤 分享你的游戏

成功后，你可以：

1. **复制链接**：
   ```
   https://sure-will.github.io/five-in-a-row/
   ```

2. **分享给朋友**：
   - 微信/QQ 发送链接
   - 社交媒体分享
   - 邮件发送

3. **添加到简历/作品集**：
   - 这是一个可展示的项目！

---

## 🎮 试试看

现在打开链接试试：
- 在电脑浏览器打开
- 在手机浏览器打开
- 都应该能正常玩游戏！

有任何问题随时问我！
