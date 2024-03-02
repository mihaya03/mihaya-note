---
title: "Go Functional Options"
date: 2024-03-02T17:56:50+09:00
draft: false
tags: ["Go", "design pattern "]
---

## 概要

* `Functional Options` パターンは、Go言語での設定管理を柔軟に行うためのデザインパターンである
* このパターンを使用すると、設定のデフォルト値を維持しながら、必要に応じて設定を柔軟に変更できる

## 基本なアプローチ

* 設定項目をフィールドとして持つ構造体を定義する。
* 「設定項目をフィールドに持つ構造体へのポインタを受け取り、対象項目の値を設定する関数を返す」関数の型Option()`を定義する。この戻り値となる関数が実際に設定を適用する役割を担う。
* 各設定項目に対応する`Option()`関数を実装する。
* 実装した`Option`型の関数を引数として受け取り、それらを新しく生成されたインスタンスに適用するようなコンストラクタ関数を定義する。

## 使用例

```Go
package main

// 設定項目をフィールドとして持つ構造体
type ImageProcessor struct {
	width, height int
	filter        string
}

//「設定項目をフィールドに持つ構造体へのポインタを受け取り、対象項目の値を設定する関数を返す」関数の型Option()
type Option func(*ImageProcessor)

// 各設定項目に対応する`Option()`関数を実装
func Resize(width, height int) Option {
	return func(ip *ImageProcessor) {
		ip.width = width
		ip.height = height
	}
}

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
	// ここでipを使用する
}

```

## 参考

* [Functional options for friendly APIs](https://dave.cheney.net/2014/10/17/functional-options-for-friendly-apis)
