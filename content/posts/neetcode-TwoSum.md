---
title: "Neetcode Twosum"
date: 2024-02-08T17:41:23+09:00
draft: true
---

``` Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j] 
```

```Go
func twoSum(nums []int, target int) []int {
    ans := make([]int,2)
    for i:=0; i<len(nums);i++ {
        for j:=i+1; j<len(nums); j++{
            if nums[i]+nums[j]==target {
                ans[0] = i
                ans[1] = j
                return ans
            }
        }
    }
    return nil
}
```