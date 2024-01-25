---
title: "Go System Programming Ch02"
date: 2024-02-07T14:51:54+09:00
draft: true
tags: ["go", "book"]
---

# Goならわかるシステムプログラミング2章の解答

### 2.1 

```Go
package main
import(
    "fmt"
    "os"
    "time"
)
func main() {
	fmt.Fprintfでio.Wwiterに数字、小数、文字列を書き込む
	fmt.Fprintf(os.Stdout, "integer: %d, float: %f, string: %s\n", 10, 12.3, "test")
}
```

### 2.2 
```go
package main
import (
    "fmt"
    "os"
)
func main() {
	file, err := os.Create("test.csv")
	if err != nil {
		panic(err)
	}
    defer file.close()
	csv_writer := csv.NewWriter(file)
    stdout_writer.Write([]string{"a", "b", "c"})
	stdout_writer.Write([]string{"d", "e", "f"})
	stdout_writer.Flush()
}
```
