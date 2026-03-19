#week04-5.py學習計畫 Prefix Sum第2題
#724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums) #陣列長度

        prefix = [0] #一開始 prefix sum 只有1個[0]
        for i in range(N):
            prefix.append( prefix[-1] + nums[i] )#陣列變了
        #print(prefix)

        postfix = [0] * (N+1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        #print(postfix)

        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        #print(postfix)
        return -1
