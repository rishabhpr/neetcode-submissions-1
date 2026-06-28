class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        left = 0

        for right in range(len(s2)):

            # add s[right]
            window[s2[right]] +=1

            # check if window is valid

            if right-left+1 > len(s1):
                window[s2[left]] -=1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left+=1
            
            if need == window:
                return True
        
        return False



        