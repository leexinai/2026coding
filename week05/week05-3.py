#week05-3.py
#1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) #参璸计瞷Ω计
        s = set()
        #代刚
        for c in counter:#盢计硋ㄓ
            #print(c, counter[c])#计 瞷碭Ω
            #拜counter[c]琌縒礚
            if counter[c] in s:
                return False
            s.add( counter[c] )
        return True #繦獽return 
