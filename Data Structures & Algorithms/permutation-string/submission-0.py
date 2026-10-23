class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 ={}
        count2 ={}

        for ch in s1:
            count1[ch] = count1.get(ch, 0)+1
        i=0
        for j in range(len(s2)):
            count2[s2[j]] = count2.get(s2[j], 0)+1

            window = j-i+1
            if window > len(s1):
                count2[s2[i]] -=1
                if count2[s2[i]]==0:
                    del count2[s2[i]]
                i+=1
            if count1== count2:
                return True
        return False