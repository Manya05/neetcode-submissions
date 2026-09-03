class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        i=0
        ans =0
        max_freq=0

        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0)+1
            max_freq = max(max_freq, freq[s[j]])
            window_length = j-i+1
            while window_length - max_freq >k:
                freq[s[i]] -=1
                i+=1
                window_length = j-i+1
            ans = max(ans , window_length)
        return ans