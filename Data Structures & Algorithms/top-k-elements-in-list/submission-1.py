class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num] = freq.get(num, 0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            bucket[count].append(num)
        result =[]
        for count in range(len(bucket)-1, 0, -1):
            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
