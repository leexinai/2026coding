# week01-4.py 學習計畫 Array/String 第3題
# LeetCode 1431. Kids With the Greatest Number of Candies
#你給額外的 extraCandies後, 小朋友手上的糖果 會不會變多
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #(請庫存 救命用)只要 test result有綠色 accept 就好
        ans = [] #答案的True和False將塞在裡面
        best =max(candies) #目前小朋友[最多有幾顆]
        for candie in candies: #逐一檢查 如果把extraCandies 給小朋友
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False) #他會不會 >= 最多的 依序塞入ans
        return ans
