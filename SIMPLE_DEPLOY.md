# 最简部署

如果你只想尽快把这个项目挂到线上，用这一页就够了。

## 三步完成

1. 确保远端某个分支里有 [`index.html`](./index.html)
2. 在 GitHub 仓库里打开 `Settings -> Pages`
3. 选择那个分支，并把目录设为 `/ (root)`

保存后，等 GitHub 部署完成即可。

## 对这个项目最重要的一点

这是一个纯静态项目，没有构建命令，也没有打包步骤。

所以部署的关键不是“怎么编译”，而是：

- 你选对了分支
- 这个分支根目录下有 `index.html`

## 推荐做法

长期维护时，建议用稳定分支发布，例如 `main`。

如果你现在还没有稳定分支，也可以先直接发布当前工作分支，后面再整理。

## 本地先看一眼

发布前可以先本地确认页面没问题：

```bash
cd five-in-a-row
python3 -m http.server 8080
```

打开：

```text
http://localhost:8080
```

## 发布后的地址

项目仓库的 GitHub Pages 地址通常是：

```text
https://<username>.github.io/<repo-name>/
```

这个仓库对应的地址格式是：

```text
https://sure-will.github.io/five-in-a-row/
```

## 如果打不开

先按这个顺序检查：

1. 远端分支里有没有 `index.html`
2. Pages 选的是不是正确分支
3. 目录是不是 `/ (root)`
4. 部署是不是还没完成
5. 浏览器是不是缓存了旧页面

## 需要更详细的版本

看这里：

- [`DEPLOY.md`](./DEPLOY.md)
- [`PAGES_GUIDE.md`](./PAGES_GUIDE.md)
- [`PR_GUIDE.md`](./PR_GUIDE.md)
