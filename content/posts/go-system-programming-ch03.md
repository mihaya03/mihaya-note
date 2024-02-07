---
title: "Goならわかるシステムプログラミング 演習問題の解答"
date: 2024-02-07T23:06:14+09:00
draft: false
---

### Q3.1：ファイルのコピー

```Go
package main

import (
	"flag"
	"io"
	"os"
)

func main() {
	oldFileName := flag.String("old", "", "古いファイルのパス")
	newFileName := flag.String("new", "", "新しいファイルのパス")
	flag.Parse()

	oldFilePath := *oldFileName
	newFilePath := *newFileName

	oldFile, err := os.Open(oldFilePath)
	if err != nil {
		panic(err)
	}
	defer oldFile.Close()

	newFile, err := os.Create(newFilePath)
	if err != nil {
		panic(err)
	}
	defer newFile.Close()

	if _, err := io.Copy(newFile, oldFile); err != nil {
		panic(err)
	}
}
```

### Q3.2：テスト用の適当なサイズのファイルを作成

```Go
package main

import (
	"crypto/rand"
	"io"
	"os"
)

func main() {
	file, err := os.Create("test.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	io.CopyN(file, rand.Reader, 1024)
}
```

### Q3.3：zipファイルの書き込み

```Go
package main

import (
	"archive/zip"
	"io"
	"os"
	"strings"
)

func main() {
	file, err := os.Create("test.zip")
	if err != nil {
		panic(err)
	}
	zipwriter := zip.NewWriter(file)
	defer zipwriter.Close()
	
	writer, err := zipwriter.Create("file01.txt")
	if err != nil {
		panic(err)
	}
	io.Copy(writer, strings.NewReader("This is a test"))
}
```

### 3.5：CopyN

```Go
func CopyN(dst Writer, src Reader, n int64) (written int64, err error) {
	written, err = Copy(dst, LimitReader(src, n))
	if written == n {
		return n, nil
	}
	if written < n && err == nil {
		err = EOF
	}
	return
}
```


### 3.6：ストリーム総集編
```Go
package main

import (
	"io"
	"os"
	"strings"
)

var (
	computer = strings.NewReader("COMPUTER")
	system   = strings.NewReader("SYSTEM")
	program  = strings.NewReader("PROGRAMMING")
)

func main() {
	var stream io.Reader

	A := io.NewSectionReader(program, 5, 1)
	S := io.NewSectionReader(system, 0, 1)
	C := io.NewSectionReader(computer, 0, 1)
	I := io.NewSectionReader(program, 8, 1)

	II, writer := io.Pipe()
	multiWriter := io.MultiWriter(writer, writer)
	go func() {
		io.Copy(multiWriter, I)
		writer.Close()
	}()
	stream = io.MultiReader(A, S, C, II)
	io.Copy(os.Stdout, stream)
}

```

### 参考

* [Goならわかるシステムプログラミング 第2版](https://www.lambdanote.com/products/go-2)