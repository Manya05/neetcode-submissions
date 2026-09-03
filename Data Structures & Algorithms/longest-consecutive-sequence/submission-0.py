class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length =0

        for num in numSet:
            if num -1 not in numSet:
                current = num
                length =1
                while current+1 in numSet:
                    current+=1
                    length +=1
                max_length = max(max_length, length)
        return max_length