#week02-3.py LeetCode學習計畫 Two Pointers 第2題
#392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1,N2 = len(s),len(t) #字串長度
        if N1==0: return True #有陷阱
        i = 0 #重0開始
        for k in range(N2): #右邊一個個式
            if s[i] ==t[k]:#找到一個左右符合
                i += 1#左邊的i往右生意點
            if i == N1:#左邊的i有往左邊結束
                return True#成功
        return False#失敗
        #i = 0 # s[i] vs. t[j]
        #for c in t: #逐一比對 看s[i]是否相同
         #   if i<len(s) and s[i]==c: #還沒走完 巧遇一個符合的
          #      i += 1 #就在走一步
        #return i==len(s) #是否走到最後
