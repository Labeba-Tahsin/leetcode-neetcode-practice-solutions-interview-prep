class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt=defaultdict(list)

        for st in strs: 
            count=[0]*26

            for ch in st:
                count[ord(ch)-ord("a")]+=1

            dt[tuple(count)].append(st)

        output=[]

        for d in dt:
            output.append(dt[d])

        return output


# Time Complexity: O(n * k) 
#   n = number of strings
#   k = average length of each string
#   Counting characters for each string takes O(k),
#   so for n strings → O(n * k)

# Space Complexity: O(n * k)
#   Dictionary stores all strings grouped → O(n * k)
#   Each count array is fixed size 26 → O(1) per string
