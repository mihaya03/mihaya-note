---
title: "Go Functional Option Pattern"
date: 2024-03-02T17:56:50+09:00
draft: false
tags: ["Go", "design pattern "]
---

## 概要

* `Functional Options` パターンは、Go言語での設定管理を柔軟に行うためのデザインパターンである
* このパターンを使用すると、設定のデフォルト値を維持しながら、必要に応じて設定を柔軟に変更できる

## 基本なアプローチ

* 設定項目をフィールドとして持つ構造体を定義する
* 設定項目をフィールドに持つ構造体へのポインタを受け取り、対象項目の値を設定する関数の型`Option`を定義する
* 各設定項目ごとに、それぞれ実装した`Option()`関数を返す関数を定義する
* Option型の関数を引数として受け取り、それらを新しく生成されたインスタンスに適用するようなコンストラクタ関数を定義する

## 使用例

```Go
package main

// 設定項目をフィールドとして持つ構造体
type ImageProcessor struct {
	width, height int
	filter        string
}

//「設定項目をフィールドに持つ構造体へのポインタを受け取り、対象項目の値を設定する関数の型を定義
type Option func(*ImageProcessor)

// 各設定項目に対応する`Option()`関数を実装(1)
func Resize(width, height int) Option {
	return func(ip *ImageProcessor) {
		ip.width = width
		ip.height = height
	}
}

// 各設定項目に対応する`Option()`関数を実装(2)
func Filter(filter string) Option {
	return func(ip *ImageProcessor) {
		ip.filter = filter
	}
}

// コンストラクタ関数を定義
func NewImageProcessor(opts ...Option) *ImageProcessor {
	ip := &ImageProcessor{}
	for _, opt := range opts {
		opt(ip)
	}
	return ip
}

func main() {
	ip := NewImageProcessor(Resize(800, 600), Filter("grayscale"))
	// ipを使用した処理
}

```

## 参考

* [Functional options for friendly APIs](https://dave.cheney.net/2014/10/17/functional-options-for-friendly-apis)
