# 最简单的部署方法 - 一步一步来

你的仓库现在只有一个分支，我们需要先设置它为默认分支，然后才能启用 GitHub Pages。

## 🎯 方法一：设置默认分支（推荐）

### 第 1 步：设置默认分支

1. **打开你的仓库**：https://github.com/Sure-Will/five-in-a-row

2. **点击 Settings**（设置）选项卡

3. **在左侧菜单中，点击最上面的 "General"**（通用）

4. **向下滚动，找到 "Default branch"（默认分支）部分**
   - 你会看到一个分支名称和一个 **切换/更改** 按钮

5. **点击 ⇄ 按钮**（或者 "Switch to another branch" 按钮）

6. **在弹出的下拉框中选择**：
   ```
   claude/implement-gomoku-game-011CUMZStsdSdAnwEkLNY6Mk
   ```

7. **点击 "Update"** 或 **"I understand, update the default branch"**

8. **完成！** 现在这个分支就是你的默认分支了

### 第 2 步：启用 GitHub Pages

现在回到 Pages 设置：

1. **还在 Settings 页面**，左侧找到 **"Pages"**

2. **在 "Branch" 下拉框中**，现在应该能看到你的分支了

3. **选择**：`claude/implement-gomoku-game-011CUMZStsdSdAnwEkLNY6Mk`

4. **Folder 保持** `/ (root)`

5. **点击 "Save"**

6. **等待 1-3 分钟**

7. **访问**：https://sure-will.github.io/five-in-a-row/

---

## 🎯 方法二：重命名分支为 main（更简单）

如果上面的方法还是不行，我们可以把分支重命名为 main：

### 在 GitHub 网页上操作：

1. **打开仓库主页**：https://github.com/Sure-Will/five-in-a-row

2. **点击左上角的分支按钮**（显示当前分支名称的地方）
   ```
   claude/implement-gomoku-game-011CUMZStsdSdAnwEkLNY6Mk ▼
   ```

3. **在搜索框中输入**：`main`

4. **点击下面的 "Create branch: main from claude/implement..."**
   - 这会创建一个新的 main 分支

5. **现在去 Settings → Pages**

6. **Branch 选择 "main"**

7. **点击 Save**

---

## 🎯 方法三：直接通过 URL 访问设置

如果你觉得找不到设置在哪里，直接访问这个链接：

```
https://github.com/Sure-Will/five-in-a-row/settings/pages
```

这会直接打开 GitHub Pages 设置页面。

---

## ⚠️ 如果 Branch 下拉框还是空的

可能的原因：

### 1. 仓库是私有的？
- **解决方法**：Settings → General → 找到 "Danger Zone" → "Change visibility" → 改为 Public

### 2. 分支没有提交？
- **检查方法**：在仓库主页，看能不能看到文件列表
- 如果看不到，说明分支是空的

### 3. 需要刷新页面
- **解决方法**：按 Ctrl+F5 强制刷新页面

---

## 📞 还是不行？

告诉我：

1. 你在 Settings → General → Default branch 那里看到什么？
2. 在仓库主页（Code 选项卡），你能看到文件吗？（比如 index.html, README.md）
3. Branch 下拉框是完全空的，还是显示 "None"？

我会根据你的情况给出更具体的解决方案！

---

## ✅ 成功标志

设置成功后，在 Pages 设置页面你应该能看到：

```
Source
Branch: [你的分支名称] ▼
Folder: / (root) ▼
[Save]

✅ Your site is live at https://sure-will.github.io/five-in-a-row/
```
