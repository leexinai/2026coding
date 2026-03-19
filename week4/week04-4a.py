#week04-4a.py 學習計畫 Prefix Sum第1題
#1732. Find the Highest Altitude
#找到最高的海拔高度(一直加就好了)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0
        for gg in gain:
            H += gg
            ans = max(ans,H)
        return ans
#week04-2.py
#        N = len(gain)#陣列的長度
#       ans = H = 0#一開始的高度是0
#        #答案一開始是0 因為一開始高度是0
#        for i in range(N):#逐個加起來
#            H += gain[i]#先在增減的量gain[i]加強H
#            ans = max(ans,H)#更新最高的答案
#        return ans
