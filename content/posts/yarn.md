---
title: "Yarn"
date: 2024-02-24T10:29:21+09:00
draft: false
tags: ["package manager", "yarn"]
---

## Yarnの使い方

### プロジェクトの新規作成

```
yarn init
```

* プロジェクト情報を格納する`package.json`が生成される
  * `package.json`におけるバージョンの記載形式は、[公式ドキュメントのセマンティックバージョニングの項目)](https://chore-update--yarnpkg.netlify.app/ja/docs/dependency-versions)を参照する

### 依存関係の追加

```
yarn add [package]
yarn add [package]@[version]
yarn add [package]@[tag] 
```

`yarn add`のオプションは代表例は下記の通りである。

* `--dev`      : devDependenciesに依存関係を追加
* `--peer`     : peerDependenciesに依存関係を追加
* `--optional` : optionalDependenciesに依存関係を追加

なお、各依存関係の特徴を以下の通りである。

* `devDependencies`: コード実行時には不要で、プロジェクトの開発時にのみ必要とされるパッケージ（テストフレームワーク、ビルドツールなど）の依存関係
* `peerDependencies`: あるパッケージが動作するために必要となる他のパッケージの依存関係
* `optionalDependencies`: 省略可能であるが存在すると何らかの追加機能や性能向上が期待できる依存関係

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

### インストール済みのパッケージを一覧表示

```
yarn list
```

### 参考

* [Yarn 公式ドキュメント](https://chore-update--yarnpkg.netlify.app/ja/docs)
