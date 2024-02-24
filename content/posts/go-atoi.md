---
title: "Go strconv"
date: 2024-02-17T16:13:15+09:00
draft: false
tags: ["Go", "strconv"]
---

## strconv 文字列と基本的なデータ型との変換

### 基本的な使い方

* `strconv.Atoi(s string) (int, error)`
  * 文字列を整数に変換する

* `strconv.Itoa(i int) string`
  * 整数を文字列に変換
  
* `strconv.ParseFloat(s string, bitSize int) (float64, error)`
  * 文字列を浮動小数点型に変換

* `strconv.FormatFloat(f float64, fmt byte, prec, bitSize int) string`
  * 浮動小数点数を文字列に変換
  * `fmt`はフォーマット
    * b: 2進数表記の指数形式
    * e: 指数形式
    * f: 通常の小数点形式
    * g:  数値の有効桁数を基に非指数形式または指数形式を自動選択
  * `prec`は精度
    * 指定したフォーマットに対応して、小数点以下の桁数、有効数字などを指定する

* `strconv.ParseBool(str string) (bool, error)`
  * 文字列を論理値に変換
  * bool型と認識される文字列はtrue、false、1、0、t、fなど

### 参考

* [strconv](https://pkg.go.dev/strconv)
