class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt={}

        for x in nums:
            dt[x]=dt.get(x,0)+1

        count=[[] for _ in range(len(nums)+1)]

        for key,val in dt.items():
            count[val].append(key)

        output=[]

        for item in reversed(count):
            for num in item:
                output.append(num)
                if len(output)==k:
                    return output
    
# Time Complexity: O(n)
#   - Counting frequencies (first loop): O(n)
#   - Filling buckets (second loop): O(n)
#   - Collecting top k (final loop): O(n) in worst case
#   Overall: O(n), where n = len(nums)

# Space Complexity: O(n)
#   - Hashmap `dt` stores up to n keys
#   - Bucket array `count` has n+1 lists
#   - Output list stores up to k elements
#   Overall: O(n)
