class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0
        have = 0

        window = defaultdict(int)
        need_count = len(need)

        best_len = 1001
        best = [-1,-1]

        for right in range(len(s)):
            char = s[right]
            window[char] +=1

            if char in need and window[char] == need[char]:
                have+=1
            
            if have == need_count and (right-left+1) < best_len:
                best = [left, right+1]
                best_len = (right-left+1)
            
            while have == need_count:
                if (right-left+1) < best_len:
                    best = [left, right+1]
                    best_len = (right-left+1)

                window[s[left]] -=1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -=1
                left +=1
            
        
        if best_len == 1001:
            return ""
        
        return s[best[0]: best[1]]
