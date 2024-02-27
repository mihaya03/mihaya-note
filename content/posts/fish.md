---
title: "Fish"
date: 2024-02-24T14:50:34+09:00
draft: true
tags: ["shell"]
---

## fishの使い方

以下、fishに関するメモ書き

* `$`によって変数を扱う
* 変数はダブルクォート内では置換されるが、シングルクオート内では置換されない
* `set $変数 [value]`: 変数に値をセットする
* `$status`: 終了ステータス
* `set -X $変数 [value]`: 変数のエクスポート
* `set -e $変数`: 変数の削除

* リストのデータ構造をサポート
* `count $変数`: リストの要素数を取得する
* 要素の追加は `set $変数 [value]`で行う
* リストの要素は`[$変数名][index]で`アクセスできる
  * なお、indexは1から、スライスにも対応

* ワンライナーで書く場合は、`;`を使用する 
* andの&&、orの||, notの!をサポート

* `if test "$変数" = "value"`
* `switch`

* 関数の定義は`~/.config/fish/functions`に記載

関数の定義例
`
function mdl
    markdownlint-cli2 $argv --fix --config .markdownlint-cli2.jsonc
end
`

* Command substitutions (コマンド置換)
  * あるコマンドの出力を別のコマンドの引数や入力として使用すること

* 

### 参考

* [fish tutorial](https://natsukium.github.io/fish-docs-jp/tutorial.html)
