#week07-2.py 學習計畫 stack 第2題
#735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a>0: #正的往左會跟左邊相撞
                ans.append(a)
            else: #負的向右 可能與[ans]裡的東西相撞很多次
                while ans and ans[-1]>0: #目前存有
                    if abs(ans[-1]) == abs(a):
                        ans.pop()
                        a = 0
                        break
                    elif abs(ans[-1]) > abs(a):
                        a = 0
                        break
                    else:
                        ans.pop()
                if a != 0: ans.append(a)
        return ans
