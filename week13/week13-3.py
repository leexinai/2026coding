# week13-3.py 學習計畫 Heap / Priority Queue 第1題
# LeetCode 215. Kth Largest Element in an Array (圖片中對應之題目)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # --- 思路 1：先用作弊的寫法示範一次 ---
        # nums.sort(reverse=True) # 先大到小排好 O(N*logN)
        # return nums[k-1] # 第 k 大的數，是 0...k-1

        # --- 思路 2：要用 Heap 資料結構，可以找出最小的數 ---
        # heapify(nums) # 變成 heap 資料結構
        # while nums:
        #     print( heappop(nums) )

        # --- 最後用這個版本 ---
        heapify(nums) # 變成 heap 資料結構 O(logN)
        for i in range(len(nums) - k):
            heappop(nums) # 吐掉不用的 N-k 個數

        return heappop(nums) # 剩下的那個，就是第 k 大的
