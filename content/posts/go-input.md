---
title: "Goの標準入力"
date: 2024-02-04T17:22:37+09:00
draft: true
tags: ["Go", "標準入力", ""]
---

### 1行1要素の場青

```Go
func readInput[T any]() T {
	var input T
	fmt.Scan(&input)
	return input
}
// int型の入力を受け取る場合：intValue := readInput[int]()
```

### 

```Go
// 1行1要素の標準入力を受け取り、その要素が文字列の場合に1文字ずつ別の変数に格納
func readStringAndStoreChars() []rune {
	var input string
	fmt.Scan(&input)
	var chars []rune
	for _, char := range input {
		chars = append(chars, char)
	}
	return chars 
}
```

### 1行多要素
```Go


```

```Go

```
