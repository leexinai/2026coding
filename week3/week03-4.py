#week03-4.py學習計畫Sliding Window 第3題
#1004. Max Consecutive Ones III
#你可以把k個0翻轉變成1,那最長的一堆1,有幾個1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0#一開始的蛇 肚子裡沒有0
        N = len(nums)#陣列的長度N
        ans = 0 #尾巴最長的 毒不死的蛇,有多長
        tail = 0 # 尾巴一開始黏在0的位置 只有拉肚子時 才會往右縮
        for head in range(N):#蛇的頭 慢慢往右吃
            if nums[head]==0:#吃到1個[有毒的0]
                zeros += 1 #身體內毒素增加
                #if zeros > k:#超過身體可容忍上限
                while zeros > k:#要用while迴圈
                    if nums[tail]==0:#現在尾巴吐掉的是[有毒的0]
                        zeros -=1 #毒素減少
                    tail += 1#尾巴拉完後 往右縮
            ans = max(ans, head - tail + 1)#更新答案]
        return ans #最長的,不會中毒死的蛇,長度是ans
