---
title: "Python itertools"
date: 2024-01-30T08:57:20+09:00
draft: false
tags: ["python", "itertools"]
---

### chains
  
- 複数のイテラブルを1つのイテラブルに連結する
  - 全要素を一度に保持する必要がないためメモリ効率が向上する

```python
from itertools import chain

iterable1 = [1, 2, 3]
iterable2 = ['a', 'b', 'c']
iterable3 = (4, 5)
combined = chain(iterable1, iterable2, iterable3)

for item in combined:
    print(item)
# 1 2 3 a b c 4 5
```

### 参考

- [itertools --- 効率的なループ実行のためのイテレータ生成関数](https://docs.python.org/ja/3/library/itertools.html#module-itertools)
