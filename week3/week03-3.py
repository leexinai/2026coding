#week03-3.py 學習計畫Sliding Window 第2題
#1456. Maximum Number of Vowels in a Substring of Given Length
#母音 Vowels: a,e,i,o,u長度k的小字串,最多幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把5個字母,變成set()
        #以後用if c in vowels:就可以快速確認他是母音
        #以前 if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        count = 0 # 紀錄目前有幾個母音
        for i in range(k):
            if s[i] in vowels: count += 1 #找到1個母音,當答案
        ans = count #離開迴圈時 確認前k個字母,有count個母音,先當答案
        N = len(s) #全部字串的長度N
        for i in range(k,N): #右邊每一個字母 逐一檢查
            if s[i] in vowels: count += 1 #右邊的頭 s[i]右吃掉1個母音
            if s[i-k] in vowels: count -= 1 #左邊的尾巴 s[i-k]吐掉 失去1個母音
            ans = max(ans,count) #更新答案 找最大值
        return ans
