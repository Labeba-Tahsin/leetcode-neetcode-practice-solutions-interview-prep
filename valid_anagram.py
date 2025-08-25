class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter={}
        for item in s:
            counter[item]=counter.get(item,0)+1

        for item in t:
            if counter.get(item) and counter[item]>0:
                counter[item]-=1
            else:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
