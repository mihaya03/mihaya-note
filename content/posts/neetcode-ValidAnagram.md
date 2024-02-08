---
title: "Neetcode ValidAnagram"
date: 2024-02-08T16:54:19+09:00
draft: true
tags: ["Neetcode"]
---
### 概要

```Python
def isAnagram(s1, s2):
    # 両方の文字列をソートして比較
    return sorted(s1) == sorted(s2)
```

### 解答2
```Go
func isAnagram(s string, t string) bool {
    s_map := make(map[rune]int)
    for _, char := range s {
        s_map[char]++
    }
    t_map := make(map[rune]int)
    for _, char := range t {
        t_map[char]++
    }
    if len(s_map) != len(t_map){
        return false
    }
    for key, value1 := range s_map {
        if value2, ok := t_map[key]; !ok || value2 != value1 {
            return false
        }
    }
    return true
}
```

