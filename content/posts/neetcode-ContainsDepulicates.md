---
title: "Neetcode Contains Depulicates"
date: 2024-02-08T16:44:57+09:00
draft: true
---

### 概要
* https://leetcode.com/problems/contains-duplicate/ 

``` Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = False
        if len(nums) != len(set(nums)):
            ans = True
        return ans
```

```Go
func containsDuplicate(nums []int) bool {
    numMap := make(map[int]bool)
    for _, num := range nums {
        if _, exists := numMap[num]; exists {
            return true
        }
        numMap[num] = true
    }
    return false
}
```
        