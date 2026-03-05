#week02-5.py
#1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() #小到大排好 等一下 左邊挑一個 右邊挑一個 看能不組合
        ans=0
        i,j = 0,len(nums) -1 #最左邊i對應最小 最右邊j對應最大
        while i<j:#還沒有撞一起 就可以左右挑1
            if nums[i]+ nums[j]==k:#剛好
                ans+=1
                i,j=i+1,j-1#右邊用了 往右 右邊用了往左
            if nums[i]+nums[j]<k:#加起來太小了 左邊小的i+1
                i=i+1
            if nums[i]+nums[j]>k:#加起來太大了 右邊大的j-1
                j=j-1
        return ans
