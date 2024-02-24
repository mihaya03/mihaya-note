---
title: "Yarn"
date: 2024-02-24T10:29:21+09:00
draft: false
tags: ["package manager", "yarn"]
---

## Yarn

### プロジェクトの新規作成

```
yarn init
```

* プロジェクト情報を格納する`package.json`が生成される

### 依存関係の追加

```
yarn add [package]
yarn add [package]@[version]
yarn add [package]@[tag]
```

* yarn addのオプション
  * `--dev`      : devDependenciesに依存関係を追加
  * `--peer`     : peerDependenciesに依存関係を追加
  * `--optional` : optionalDependenciesに依存関係を追加

### 依存関係のアップグレード

```
yarn upgrade [package]
yarn upgrade [package]@[version]
yarn upgrade [package]@[tag]
```

### 依存関係の削除

```
yarn remove [package]
```

### 依存関係のインストール

```
yarn install
```
