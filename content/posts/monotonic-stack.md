---
title: "Monotonic Stack"
date: 2024-02-22T22:34:38+09:00
draft: false
---
## Monotonic Stack

### 概要

* 格納される要素が単調増加または単調減少のいずれかの順序を保つスタックである

### 性質

* スタック内の要素は、単調増加または単調減少の順序を保つ
* ある要素より大きい（または小さい）次の要素を見つけるなど、特定の条件における検索を効率的に実施できる。これは、各要素がスタックにプッシュされたり、ポップされたりする操作が各1回、計2回しか行われないため、全体の計算量が O(n) となることによる。

### 実装例

各要素について、次に大きい要素を求め、そのインデックスを要素とする配列を作成する。次に大きい要素が存在しない場合は -1 とする。

```Python
def nextGreaterElement(inputs: list[int]) -> list[int]:
    stack = [] 
    ans = [-1] * len(inputs)
    for i in range(len(inputs)):
        while stack and inputs[i] > inputs[stack[-1]]:
            idx = stack.pop()
            ans[idx] = i
        stack.append(i)
    return ans
```

### 参考

* [Introduction to Monotonic Stack – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/)
