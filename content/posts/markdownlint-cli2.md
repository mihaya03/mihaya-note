---
title: "markdownlint-cli2"
date: 2024-02-24T10:53:13+09:00
draft: false
tags: ["linter", "markdown"]
---

## markdownlint-cli2の使い方

### 概要

* `markdownlint-cli2`はCLIで操作可能なmarkdown用のlinterである

### インストール

```
npm install markdownlint-cli2 --global
```

### コマンドの形式

```
markdownlint-cli2 glob0 [glob1] [...] [globN] [--config file] [--fix] [--help]
```

* `[glob]`：linterの対象となるファイルを指定する
* `[--config file]`：lintのルールなどを記載した設定ファイルを指定する
  * 設定ファイルは`.markdownlint-cli2.jsonc`、`.markdownlint-cli2.yaml`などの形式で記述する
  * コマンドを実行するディレクトリまたは、その上位のディレクトリに設定ファイルが存在する場合、markdownlint-cli2はそれを自動的に検出して適用する
* `[--fix]`: lint実行時に誤りの検知とともに、修正を行う

### 設定ファイルの形式

設定ファイルのフォーマットに関する詳細は[スキーマ](https://github.com/DavidAnson/markdownlint-cli2/tree/main/schema)を参照する。
以下では設定ファイル(.jsonc)の例を提示する。

```
{
    // markdownlintの設定オブジェクト
    "config": {
      "fenced-code-language":false, // code blockの言語指定を許容
    }
}
```

### 参考

* [markdownlint-cli2 (GitHub)](https://github.com/DavidAnson/markdownlint-cli2)
