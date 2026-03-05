#week02-4.py
#11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0 #一開始沒答案
        i,j = 0,len(height)-1
        while i<j: #只咬左右沒撞一起
            area = (j-i)* min( height[i],height[j])
            ans = max(ans,area)#更新答案
            if height[i] < height[j]: i+= 1 #小的i往右
            else: j-=1 #小的j往左
        return ans
